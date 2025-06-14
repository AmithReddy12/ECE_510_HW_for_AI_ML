import subprocess
import numpy as np
import time

# Prepare dummy or real input (48x48 normalized face)
frame = np.random.rand(48, 48)  # Replace this with your actual CNN input
np.savetxt("frame_input.txt", frame, fmt='%.4f')

# Run Verilator simulation
start = time.time()
subprocess.run(["./obj_dir/Vcnn_accelerator"])
end = time.time()

print("[Python] Hardware Inference Time: {:.6f} sec".format(end - start))