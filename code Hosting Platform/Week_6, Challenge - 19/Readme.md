# Challenge 19 – Binary Leaky‑Integrate‑and‑Fire Neuron  
*Weekly‑Challenges / Neuromorphic Digital Logic*

## 🔍  Overview
This repository implements a **fixed‑point, binary LIF neuron** in SystemVerilog and validates it with a four‑scenario testbench.  
Everything was developed and verified online in **EDA Playground**; you can rerun or tweak the design from your browser without installing any tools.

**Live playground link (public):** <https://edaplayground.com/x/8UqP>
*(replace `XXXX` with the final share code you received after saving)*

---

## 📂  Repository Contents
| File | Purpose |
|------|---------|
| `lif_neuron.sv` | Parameterised neuron module (Q4.4 fixed‑point) |
| `lif_tb.sv` | Testbench: sub‑threshold, accumulate‑&‑spike, leak, single tick |
| `waveform.png` | Screenshot of EPWave showing membrane potential & spikes |
| `lif.vcd` | Sample VCD captured from Icarus run (optional, 30 KB) |
| `README.md` | This document |

---

## ⚙️  Design parameters
* **Width (W)** : 8 bits  
* **Fractional bits (FRACT)** : 4 (Q4.4 format)  
* **Leak factor (λ)** : 0.75 → `8'sd12`  
* **Threshold (θ)** : 1.0 → `8'sd16`

The neuron updates each clock:
P_next = (λ · P) + I // shift‑right FRACT to keep Q‑format
if (P_next ≥ θ) spike & reset

Reset is implemented as `P = P - θ` to model refractory drop; setting to zero also works.

---

## 🏃‍♂️  How to run locally (Icarus Verilog)

```bash
# install once: sudo apt install iverilog gtkwave
iverilog -g2012 lif_neuron.sv lif_tb.sv -o lif_sim
vvp lif_sim            # produces lif.vcd
gtkwave lif.vcd &      # optional waveform viewer
Simulation finishes in < 1 µs of runtime and prints no errors.
Waveforms match the four intended behaviours (see waveform.png).

🖥️ How to rerun in EDA Playground
Open the live link above

Ensure Tool = Icarus Verilog (or VCS) and Top = lif_tb

Click Run

Click the EPWave icon → Load → lif.vcd to inspect signals

📈 Results
Scenario	                   Input pattern	             Expected	                        Observed
① Constant sub‑threshold	   I = 1 for 10 cycles	      S = 0, P rises but < θ	            ✅
② Accumulate & spike	       20 cycles of I = 1	        Spike once, P reset	                ✅
③ Leak only	                 I = 0 for 30 cycles	      P decays toward 0, no spike	        ✅
④ Single strong tick	       One high cycle	            Immediate spike	                    ✅

(Captured in waveform.png)

✍️ Takeaways
A simple Q‑format (Q4.4) keeps arithmetic fully combinational; only a shift is needed for the leak term.

Parameterising LAMBDA and THRESH lets the same module explore different neuron dynamics without code edits.

EDA Playground is plenty for quick digital‑neuro prototypes—compile, run, share waveforms in < 30 seconds.

