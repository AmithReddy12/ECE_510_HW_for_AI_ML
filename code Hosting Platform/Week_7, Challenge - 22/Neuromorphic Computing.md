#Hardest Research Challenge
Scalability—combining billions of neurons, sparse connectivity, and low power while maintaining ecosystem support. The paper emphasizes tight compute–memory integration, event-driven sparsity, and local learning. It states “scale is one of the critical dimensions” 
gwern.net, highlighting that current prototypes like Intel’s Loihi (1.15B neurons) are insufficient.

#“AlexNet” Moment Potential
A neuromorphic breakthrough akin to AlexNet would be deploying a large-scale vision model or LLM on neuromorphic hardware (e.g., heterogeneous event-based Vision Transformer on Loihi 3 or SpiNNaker 2) achieving general-purpose AI with energy efficiency at scale.

#Interoperability Solution
Propose an “Event-ONNX” standardized schema. Developers could train ANN/Transformer networks, convert them to spiking equivalents via meta-compilers, and deploy them across neuromorphic platforms with unified AER messaging and toolchains (e.g., Lava, NEST, SpiNNTools).

#Unique Benchmark Specification
A benchmark suite that measures:

Energy-per-inference (J/inference)

Latency (ms)

Scalability: inference vs. neuron count (1M–10B)

Ecosystem maturity (library support, standard formats like Event-ONNX)

#Emerging Memory Synergy
Memristor crossbars, as part of analog-in-memory arrays, match the event-driven and sparse design principles. Figure 3 (ecosystem diagram) highlights in-memory compute; combining memristors with local STDP-like local learning yields co-designed synergies.
