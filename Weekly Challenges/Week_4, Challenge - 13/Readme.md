# CUDA SAXPY Benchmark & Visualization 🏎️💨

**Course:** ECE 410/510 · Spring 2025  
**Challenge #:** GPU Micro‑benchmark  
**Student:** Amith Reddy  
**Last Update:** 2025-06-16

---
## 📖 Overview
This mini‑project measures the performance of the SAXPY kernel (Single‑Precision A·X + Y) on an NVIDIA **Tesla T4** (Google Colab) across problem sizes 2^15 … 2^25.  
Runtimes are split into:

| label | description |
|-------|-------------|
| **total** | host → device transfer + kernel launch + device → host transfer |
| **kernel** | pure kernel execution time (device‑side only) |

Two bar charts are provided (`plot.png`, `Saxpy Run Time on Collab Tesla T4.png`) that visualise both metrics side‑by‑side on a log₂(N) x‑axis.

---
## 📂 Repository Layout
```
.
├── Saxpy.ipynb                ← Colab notebook (end‑to‑end workflow)
├── Saxpy.py                   ← Python extraction of CSV + plotting
├── saxpy_bench.cu             ← CUDA C++ benchmark (generates CSV)
├── saxpy_times.csv            ← Raw timing results (N, total_ms, kernel_ms)
├── plot.png                   ← Matplotlib bar chart
└── README.md                  ← (this file)
```

---
## 🔧 Prerequisites
| Tool | Version | Purpose |
|------|---------|---------|
| **CUDA Toolkit** | 11+ (nvcc) | compile `saxpy_bench.cu` |
| **Python** | ≥ 3.9 | run plotting script |
| numpy, matplotlib | latest | data manipulation & figure generation |

*On Colab*:  
```bash
!apt-get install -y nvidia-cuda-toolkit
!nvcc --version
pip install matplotlib numpy
```

---
## 🚀 Quick Start
```bash
# 1. Compile and run benchmark
nvcc -O3 saxpy_bench.cu -o saxpy_bench
./saxpy_bench > saxpy_times.csv

# 2. Plot
python Saxpy.py           # outputs plot.png

# 3. View results
display plot.png          # Jupyter / Colab
```

---
## 📝 Methodology
1. Allocate X, Y arrays on host & device (`float`).
2. Warm‑up run removed to avoid first‑launch overhead.
3. For each power‑of‑two size **N** in 2^15 … 2^25:
   - Record **total** time with `cudaEvent`s surrounding H2D copy + kernel + D2H copy.
   - Record **kernel** time with events around kernel only.
   - Emit CSV row: `N,total_ms,kernel_ms`.
4. Use `numpy` to ingest CSV and `matplotlib` to create a grouped‑bar figure.

---
## 🔍 Findings
*  **Kernel latency ≪ PCIe latency** for small N — data transfer dominates.
*  For N ≥ 2^22, kernel time begins to contribute noticeably, reflecting higher ALU load.
*  Peak throughput on the T4 reaches ~3 GB/s effective on‑device bandwidth for the largest size.

---
## 🔄 Reproducibility Tips
* Set `CUDA_VISIBLE_DEVICES=0` to pin to a single GPU.
* Use `nvidia‑smi --query‑gpu=power.limit --format=csv` to record power cap.
* Append `--csv` to `./saxpy_bench` execution if multiple runs are needed; aggregate with pandas.

---
## 📚 References
* CUDA C++ Programming Guide — SAXPY example.  
* NVIDIA Developer Blog — *An easy introduction to CUDA*.

---
