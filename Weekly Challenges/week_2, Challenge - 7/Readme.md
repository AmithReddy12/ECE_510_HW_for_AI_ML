# Week 2 — Challenge 7: Perceptron Learning Visualization 🧠✏️

**Course:** ECE 410/510 · Spring 2025  
**Instructor:** Prof. Christof Teuscher  
**Student:** Amith Reddy  
**Revision:** 1 (2025-06-16)

## 🎯 Challenge Brief
1. **Draw the decision boundary** of a single‑layer perceptron in a 2‑D plane as it learns.
2. **Animate** every weight‑update step using the perceptron learning rule.

The supplied script `percept.py` generates synthetic, linearly separable data, trains a perceptron
for ten epochs, and captures each intermediate separating line.  
The result is exported as both **MP4** and **GIF** animations.

## 📂 Repository Contents
```
.
├── percept.py                 ← main script (numpy + matplotlib)
├── perceptron_learning.mp4    ← pre‑rendered demo video (H.264, 2 fps)
└── README.md                  ← (this file)
```

## 🔧 Requirements
| Tool / Library | Purpose | Install Hint |
|----------------|---------|--------------|
| Python ≥ 3.10  | runtime | <https://www.python.org/downloads/> |
| numpy         | vector maths | `pip install numpy` |
| matplotlib    | plotting & animation | `pip install matplotlib` |
| Pillow        | GIF writer (optional) | `pip install pillow` |
| FFmpeg        | MP4 encoding | `sudo apt install ffmpeg` (Linux) / <https://ffmpeg.org/download.html> |

## 🚀 Quick Start
```bash
# 1. Install dependencies (conda or venv recommended)
pip install numpy matplotlib pillow

# 2. Run the script
python percept.py

# 3. Enjoy the output
vlc perceptron_learning.mp4          # or open the GIF in any browser
```
The console will confirm: `🎬 Video saved as perceptron_learning.mp4`.

## 📝 How It Works
1. **Data generation** – 100 random 2‑D points, labelled by the sign of (x₁ + x₂).  
2. **Initialisation** – random weight vector **w** ∈ ℝ² and bias *b*.  
3. **Learning loop**  
   ```text
   update = η · (target − sign(w·x + b))
   w ← w + update·x
   b ← b + update
   ```
   Whenever a sample is mis‑classified, the separating line shifts toward the correct side.
4. **Animation** – after every update, the current line is stored in `weight_history`;  
   `matplotlib.animation.FuncAnimation` iterates through the list and renders frames.
5. **Export** – the animation is encoded with `FFMpegWriter` (MP4) and `PillowWriter` (GIF).

## ⚙️ Customisation
| Parameter | Location | Effect |
|-----------|----------|--------|
| `epochs`  | top of `percept.py` | more or fewer training passes |
| `learning_rate` | ″ | convergence speed & path |
| `np.random.seed` | ″ | reproduce runs |
| `fps` / `bitrate` | writer instantiation | smoother or smaller video |

## 📚 Further Reading
* Rosenblatt, F. (1958). *The Perceptron: A Probabilistic Model for Information Storage and Organization in the Brain.*
* Nielsen, M. (2015). *Neural Networks and Deep Learning*, Ch. 1.

---
