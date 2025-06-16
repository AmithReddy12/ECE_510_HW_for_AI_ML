/**
 * saxpy_bench.cu  -- CUDA SAXPY micro‑benchmark
 * Measures total vs kernel‑only runtime for N = 2^15 … 2^25.
 * Compile: nvcc -O3 saxpy_bench.cu -o saxpy_bench
 * Run:     ./saxpy_bench > saxpy_times.csv
 */
#include <cstdio>
#include <cuda_runtime.h>

__global__ void saxpy(int n, float a, float* x, float* y)
{
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i < n) y[i] = a * x[i] + y[i];
}

int main()
{
    const int first_pow = 15, last_pow = 25;            // 2^15 … 2^25
    for (int p = first_pow; p <= last_pow; ++p)
    {
        int    N     = 1 << p;
        size_t bytes = N * sizeof(float);

        // host buffers
        float *h_x = (float*)malloc(bytes);
        float *h_y = (float*)malloc(bytes);
        for (int i = 0; i < N; ++i) { h_x[i] = 1.0f; h_y[i] = 2.0f; }

        // device buffers
        float *d_x, *d_y;
        cudaMalloc(&d_x, bytes);
        cudaMalloc(&d_y, bytes);

        cudaMemcpy(d_x, h_x, bytes, cudaMemcpyHostToDevice);
        cudaMemcpy(d_y, h_y, bytes, cudaMemcpyHostToDevice);

        dim3 block(256);
        dim3 grid((N + block.x - 1) / block.x);

        cudaEvent_t t0, t1;
        cudaEventCreate(&t0);  cudaEventCreate(&t1);

        // --- TOTAL time (H2D + kernel + D2H) -------------------------
        cudaEventRecord(t0);
        saxpy<<<grid, block>>>(N, 2.0f, d_x, d_y);
        cudaMemcpy(h_y, d_y, bytes, cudaMemcpyDeviceToHost);
        cudaEventRecord(t1);  cudaEventSynchronize(t1);
        float total_ms = 0.0f;
        cudaEventElapsedTime(&total_ms, t0, t1);

        // --- KERNEL‑ONLY time ---------------------------------------
        cudaEventRecord(t0);
        saxpy<<<grid, block>>>(N, 2.0f, d_x, d_y);
        cudaEventRecord(t1);  cudaEventSynchronize(t1);
        float kernel_ms = 0.0f;
        cudaEventElapsedTime(&kernel_ms, t0, t1);

        printf("%d,%.6f,%.6f\n", N, total_ms, kernel_ms);   // CSV line

        cudaFree(d_x); cudaFree(d_y); free(h_x); free(h_y);
        cudaEventDestroy(t0); cudaEventDestroy(t1);
    }
    return 0;
}
