# q_accel_driver.py
"""
Tiny MMIO wrapper for the hardware Q‑update accelerator.

Usage
-----
from q_accel_driver import QAccel
accel = QAccel(mmio)                 # 'mmio' is a pynq.MMIO or any class
accel.update(s, a, r, sp)            # one call per environment step
q_sa = accel.read_q(s, a)            # optional (slow) read‑back

The driver assumes:
* AXI‑Lite register map defined in q_update_axi_wrap.sv
    0x00 : { state[9:0], action[1:0] }
    0x04 : reward   (Q8.8 signed)
    0x08 : next_state[9:0]
    0x0C : launch   (write 1)
* BRAM depth = ROWS*COLS*ACTIONS, 16‑bit words
"""

BOARD_ROWS = 5          # keep in sync with frozenlake_sw.py
BOARD_COLS = 5
ACTIONS    = 4
FIX_SCALE  = 256        # 2**FRAC_W (Q8.8)

class QAccel:
    def __init__(self, mmio):
        """
        Parameters
        ----------
        mmio : object
            Something that provides .write(addr, data) and .read(addr).
            • PYNQ boards   -> pynq.MMIO
            • Zynq PS Linux -> /dev/uio + mmap (simple wrapper)
            • Verilator sim -> a Bus Functional Model with same API
        """
        self.mmio = mmio
        self.cols = BOARD_COLS

    # ------------------------------------------------------------------
    #  Public API
    # ------------------------------------------------------------------
    def update(self, s, a, r, sp):
        """
        Ship one tuple (s, a, r, sp) to the RTL core.

        Parameters
        ----------
        s  : int   flattened current state   (0 .. ROWS*COLS‑1)
        a  : int   action (0 .. 3)
        r  : int/float   reward (e.g. ‑5, ‑1, +1) – *not* scaled
        sp : int   flattened next state      (0 .. ROWS*COLS‑1)
        """
        # word‑aligned AXI writes
        self.mmio.write(0x00,  (s << 2) | (a & 0b11))
        self.mmio.write(0x04,  (int(r * FIX_SCALE) & 0xFFFF))
        self.mmio.write(0x08,  sp & 0x3FF)
        self.mmio.write(0x0C,  1)                         # launch pulse

    def read_q(self, s, a):
        """
        Optional helper – read back Q(s,a) as float.
        Slower than keeping a software copy but handy for debugging.
        """
        addr16 = ((s << 2) | a) << 1          # each entry is 16 bits
        raw = self.mmio.read(addr16) & 0xFFFF
        if raw & 0x8000:                      # sign‑extend negatives
            raw -= 0x10000
        return raw / FIX_SCALE
