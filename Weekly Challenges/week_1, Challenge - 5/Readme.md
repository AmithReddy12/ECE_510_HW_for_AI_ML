# Week 1 — Challenge 5: Workload Analysis & Profiling

**Course:** ECE 410/510 · Spring 2025  
**Instructor:** Prof. Christof Teuscher  
**Revision:** 1 (April 1 2025)

## 🥅 Learning Goals
- Analyse and profile AI/ML (and other) Python workloads.
- Identify computational bottlenecks and intrinsic parallelism.
- Reason about candidate execution architectures for acceleration.
- Experience the pitfalls of “vibe coding” (unstructured, quick‑and‑dirty development).

## 📂 Repository Structure
```
.
├── differential_equation_solver.py
├── matrixmultiplication.py
├── quicksort.py
└── README.md   ← you are here
```
Feel free to add additional workloads (e.g. CNN, AES, TSP) in the same folder.

## 🔧 Prerequisites
| Tool | Purpose | Install Hint |
|------|---------|--------------|
| **Python ≥ 3.10** | run & compile workloads | <https://www.python.org/downloads/> |
| **snakeviz** | interactive visualisation of `cProfile` results | `pip install snakeviz` |
| **tabulate** (optional) | pretty CLI tables | `pip install tabulate` |

## 1 — Select or Generate Workloads
Three example workloads are provided.  
To swap them out, either:
1. Write your own implementation, **or**
2. Ask your favourite LLM to scaffold code, **or**
3. Download trusted open‑source snippets.

## 2 — Compile to Byte‑Code
```bash
python -m py_compile <workload>.py
#  → __pycache__/<workload>.cpython-312.pyc
```

## 3 — Disassemble Byte‑Code
```python
import dis, <workload>
dis.dis(<workload>.<entry_function>)
```
> **Q 1.** Which virtual machine does CPython employ?  
> **Q 2.** How many arithmetic op‑codes (+, -, *, /, %) do you observe?

## 4 — Instruction Histogram
```python
from collections import Counter, dis
instr = Counter(i.opname for i in dis.get_instructions(<entry_function>))
print(instr.most_common())
```
Store each histogram in `results/<workload>_opcode_hist.json` for later comparison.

## 5 — Runtime Profiling
```python
import cProfile, pstats, snakeviz, <workload>

cProfile.run('<workload>.<entry_function>()', 'prof.out')
snakeviz.profiler.Profiler('prof.out').view()   # opens in browser
```
Record **top‑5 hot functions** and **wall‑clock time** in `results/profile_<workload>.md`.

## 6 — Parallelism Detection
Ask an LLM or write a script that:
1. Builds a *call graph* and *data‑dependency graph*.
2. Flags independent loops / tasks suitable for:
   - Threading (`concurrent.futures.ThreadPoolExecutor`)
   - Multi‑processing (`multiprocessing`)
   - GPU off‑load (CUDA / CuPy / PyTorch Tensors)

Save findings in `results/parallelism_<workload>.md`.

## 7 — Candidate Execution Architectures
Based on the opcode mix, memory access patterns and profiling data, draft a short proposal for each workload, e.g.:

| Workload | Dominant Ops | Bottleneck | Suggested ISA / Accelerator |
|----------|--------------|------------|-----------------------------|
| Differential Eq. RK4 | `BINARY_OP`, FP mul/add | Tight loop over small state | SIMD FP‑ALU or DSP slices |
| Matrix Multiply      | Nested triple loop, loads/stores | Memory bandwidth | GEMM engine, systolic array |
| Quicksort            | Recursion & branching | Call‑stack depth | Out‑of‑order CPU core |

*(Edit / extend this table with your own insights.)*

## 8 — Documentation & Reflection
- Summarise **what you learned** about Python’s execution model and profiling workflow.
- List **common pitfalls** you hit while “vibe coding” and how you fixed them.
- Keep all raw artefacts (`.pyc`, profiler outputs, plots) under `results/` so peers can reproduce.

---
**Author:** Amith Reddy  
**Last Edited:** 2025-06-16

> “Premature optimisation is the root of all evil.” — Donald Knuth  
> *Profile first, optimise after.*
