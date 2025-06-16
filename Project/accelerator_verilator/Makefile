# Default to using hardware unless overridden
USE_HARDWARE ?= True

# Name of the Python script
PYTHON_SCRIPT = ../emotion_detector_with_model.py

# Name of the Verilator C++ simulation binary
SIM_BINARY = ./obj_dir/Vcnn_accelerator

# Default target
all: verilate run

# Verilate the hardware design
verilate:
	verilator -Wall --Wno-fatal --cc cnn_accelerator.sv --exe sim_main.cpp
	make -C obj_dir -f Vcnn_accelerator.mk Vcnn_accelerator

# Run the emotion detection script with USE_HARDWARE passed as env var
run:
	USE_HARDWARE=$(USE_HARDWARE) python $(PYTHON_SCRIPT)

# Clean build files
clean:
	rm -rf obj_dir *.log *.csv frame_input.txt input_image.txt

.PHONY: all verilate run clean
