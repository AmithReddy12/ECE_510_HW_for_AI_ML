# Challenge #28: Memristor Modeling and Simulation

## 🎯 Objective
The objective of this challenge was to model and simulate a memristor—an essential component in neuromorphic computing—demonstrating its characteristic pinched hysteresis loop.

## 🧠 What is a Memristor?
A memristor (memory resistor) is a passive two-terminal electronic component whose resistance varies based on the amount and direction of electrical charge that has previously passed through it. Memristors exhibit a distinctive **pinched hysteresis loop** in their current-voltage (I-V) relationship.

## 🔧 Implementation Details
- **Model Used:** Biolek memristor model
- **Environment:** Python, NumPy, Matplotlib
- **Simulation:**  
  - Applied sinusoidal voltage (1 Hz)  
  - Computed current and resistance over time  
  - Visualized the resulting pinched hysteresis loop

## 🚀 How to Run
### Requirements:
```bash
pip install numpy matplotlib
python memristor_model.py

📁 Files Included
memristor_model.py: Python implementation of Biolek memristor model simulation.

memristor_hysteresis.png: Generated plot showing the memristor's characteristic pinched hysteresis loop (I-V curve).

📊 Results
Upon running the simulation, you will obtain a clear plot (memristor_hysteresis.png) illustrating the memristor's characteristic pinched hysteresis loop, confirming the correct behavior of the Biolek model.

📝 Conclusion
This simulation demonstrates the fundamental behavior of a memristor and its unique I-V characteristics essential for neuromorphic computing applications. The Biolek model provides an intuitive and practical framework for understanding memristive dynamics.
