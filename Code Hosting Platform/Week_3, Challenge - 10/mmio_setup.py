# mmio_setup.py
"""
Creates a global 'mmio' object that maps to the accelerator's AXI‑Lite regs.
Edit the bitfile name and IP path to match your Vivado block design.
"""

from pynq import Overlay, MMIO   # pip install pynq on x86 or use board image

BITFILE = "q_update_subsystem_top.bit"        # generated in step 2
IP_NAME = "q_update_subsystem_top_0"          # Vivado auto‑names this

ol   = Overlay(BITFILE)
base = ol.ip_dict[IP_NAME]["phys_addr"]
mmio = MMIO(base, 0x1000)   # 4 regs × 4 bytes = 16 B = 0x1000 fine
