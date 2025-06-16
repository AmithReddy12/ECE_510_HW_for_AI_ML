import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter

# Step 1: Create linearly separable data
np.random.seed(42)
X = np.random.randn(100, 2)
y = np.where(X[:, 0] + X[:, 1] > 0, 1, -1)  # simple linear boundary

# Step 2: Initialize weights and bias
weights = np.random.randn(2)
bias = np.random.randn()
learning_rate = 0.1

# Store weight history for animation
weight_history = [(weights.copy(), bias)]

# Step 3: Perceptron learning rule
for epoch in range(10):
    for xi, target in zip(X, y):
        update = learning_rate * (target - np.sign(np.dot(weights, xi) + bias))
        if update != 0:
            weights += update * xi
            bias += update
            weight_history.append((weights.copy(), bias))

# Step 4: Visualization setup
fig, ax = plt.subplots()
colors = ['red' if label == -1 else 'blue' for label in y]
scat = ax.scatter(X[:, 0], X[:, 1], c=colors)
line, = ax.plot([], [], 'k--', lw=2)

def init():
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    return line,

def update_plot(frame):
    w, b = weight_history[frame]
    x_vals = np.array(ax.get_xlim())
    if w[1] != 0:
        y_vals = -(w[0] * x_vals + b) / w[1]
    else:
        x_vals = [-b / w[0]] * 2
        y_vals = np.array(ax.get_ylim())
    line.set_data(x_vals, y_vals)
    return line,

ani = FuncAnimation(fig, update_plot, frames=len(weight_history),
                    init_func=init, blit=True, repeat=False)

# --- Save as MP4 ---
writer = FFMpegWriter(fps=2, metadata=dict(artist='Amith'), bitrate=1800)
ani.save("perceptron_learning.mp4", writer=writer)

plt.close()
print("🎬 Video saved as perceptron_learning.mp4")




































































































































import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter, FFMpegWriter

# Step 1: Create linearly separable data
np.random.seed(42)
X = np.random.randn(100, 2)
y = np.where(X[:, 0] + X[:, 1] > 0, 1, -1)  # simple linear boundary

# Step 2: Initialize weights and bias
weights = np.random.randn(2)
bias = np.random.randn()
learning_rate = 0.1

# Store weight history for animation
weight_history = [(weights.copy(), bias)]

# Step 3: Perceptron learning rule
for epoch in range(10):
    for xi, target in zip(X, y):
        update = learning_rate * (target - np.sign(np.dot(weights, xi) + bias))
        if update != 0:
            weights += update * xi
            bias += update
            weight_history.append((weights.copy(), bias))

# Step 4: Visualization setup
fig, ax = plt.subplots()
colors = ['red' if label == -1 else 'blue' for label in y]
scat = ax.scatter(X[:, 0], X[:, 1], c=colors)
line, = ax.plot([], [], 'k--', lw=2)

def init():
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    return line,

def update_plot(frame):
    w, b = weight_history[frame]
    x_vals = np.array(ax.get_xlim())
    if w[1] != 0:
        y_vals = -(w[0] * x_vals + b) / w[1]
    else:
        x_vals = [-b / w[0]] * 2
        y_vals = np.array(ax.get_ylim())
    line.set_data(x_vals, y_vals)
    return line,

ani = FuncAnimation(fig, update_plot, frames=len(weight_history),
                    init_func=init, blit=True, repeat=False)

# --- Saving the animation ---

# Option 1: Save as GIF (requires ImageMagick or Pillow)
ani.save("perceptron_animation.gif", writer=PillowWriter(fps=2))

# Option 2: Save as MP4 (requires ffmpeg)
# ani.save("perceptron_animation.import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter, FFMpegWriter

# Step 1: Create linearly separable data
np.random.seed(42)
X = np.random.randn(100, 2)
y = np.where(X[:, 0] + X[:, 1] > 0, 1, -1)  # simple linear boundary

# Step 2: Initialize weights and bias
weights = np.random.randn(2)
bias = np.random.randn()
learning_rate = 0.1

# Store weight history for animation
weight_history = [(weights.copy(), bias)]

# Step 3: Perceptron learning rule
for epoch in range(10):
    for xi, target in zip(X, y):
        update = learning_rate * (target - np.sign(np.dot(weights, xi) + bias))
        if update != 0:
            weights += update * xi
            bias += update
            weight_history.append((weights.copy(), bias))

# Step 4: Visualization setup
fig, ax = plt.subplots()
colors = ['red' if label == -1 else 'blue' for label in y]
scat = ax.scatter(X[:, 0], X[:, 1], c=colors)
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter, FFMpegWriter

# Step 1: Create linearly separable data
np.random.seed(42)
X = np.random.randn(100, 2)
y = np.where(X[:, 0] + X[:, 1] > 0, 1, -1)  # simple linear boundary

# Step 2: Initialize weights and bias
weights = np.random.randn(2)
bias = np.random.randn()
learning_rate = 0.1

# Store weight history for animation
weight_history = [(weights.copy(), bias)]

# Step 3: Perceptron learning rule
for epoch in range(10):
    for xi, target in zip(X, y):
        update = learning_rate * (target - np.sign(np.dot(weights, xi) + bias))
        if update != 0:
            weights += update * xi
            bias += update
            weight_history.append((weights.copy(), bias))

# Step 4: Visualization setup
fig, ax = plt.subplots()
colors = ['red' if label == -1 else 'blue' for label in y]
scat = ax.scatter(X[:, 0], X[:, 1], c=colors)
line, = ax.plot([], [], 'k--', lw=2)

def init():
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    return line,

def update_plot(frame):
    w, b = weight_history[frame]
    x_vals = np.array(ax.get_xlim())
    if w[1] != 0:
        y_vals = -(w[0] * x_vals + b) / w[1]
    else:
        x_vals = [-b / w[0]] * 2
        y_vals = np.array(ax.get_ylim())
    line.set_data(x_vals, y_vals)
    return line,

ani = FuncAnimation(fig, update_plot, frames=len(weight_history),
                    init_func=init, blit=True, repeat=False)

# --- Saving the animation ---

# Option 1: Save as GIF (requires ImageMagick or Pillow)
ani.save("perceptron_animation.gif", writer=PillowWriter(fps=2))

# Option 2: Save as MP4 (requires ffmpeg)
# ani.save("perceptron_animation.mp4", writer=FFMpegWriter(fps=2))

plt.close()
print("Animation saved successfully.")

