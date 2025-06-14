import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("emotion_predictions.csv")

# Convert time to float
df["Time (sec)"] = df["Time (sec)"].astype(float)

# Split by mode
hw_df = df[df["Inference Mode"] == "HW"]
sw_df = df[df["Inference Mode"] == "SW"]

# Summary stats
print("===== Inference Time Summary =====")
print(f"HW average time: {hw_df['Time (sec)'].mean():.6f} sec")
print(f"SW average time: {sw_df['Time (sec)'].mean():.6f} sec")
print()

print("===== Emotion Count (HW) =====")
print(hw_df["Predicted Emotion"].value_counts())
print()

print("===== Emotion Count (SW) =====")
print(sw_df["Predicted Emotion"].value_counts())
print()

# Plot average inference time
plt.figure()
plt.bar(["HW", "SW"], [hw_df["Time (sec)"].mean(), sw_df["Time (sec)"].mean()])
plt.title("Average Inference Time")
plt.ylabel("Time (sec)")
plt.grid(True)
plt.savefig("avg_inference_time.png")
plt.show()

# Plot emotion distribution
plt.figure()
hw_counts = hw_df["Predicted Emotion"].value_counts()
sw_counts = sw_df["Predicted Emotion"].value_counts()

all_emotions = sorted(set(hw_counts.index).union(set(sw_counts.index)))
hw_vals = [hw_counts.get(emotion, 0) for emotion in all_emotions]
sw_vals = [sw_counts.get(emotion, 0) for emotion in all_emotions]

x = range(len(all_emotions))
plt.bar(x, hw_vals, width=0.4, label='HW', align='center')
plt.bar([i + 0.4 for i in x], sw_vals, width=0.4, label='SW', align='center')
plt.xticks([i + 0.2 for i in x], all_emotions, rotation=45)
plt.title("Emotion Prediction Count")
plt.xlabel("Emotion")
plt.ylabel("Count")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("emotion_distribution.png")
plt.show()
