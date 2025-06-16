#include <cstdio>
#include <cuda_runtime.h>

constexpr int IN  = 4;
constexpr int HID = 5;
constexpr int OUT = 1;
constexpr int BATCH = 1<<20;          // 1 M samples for timing

__global__ void hidden(const float* W, const float* b,
                       const float* x, float* h){
    int idx = blockIdx.x * blockDim.x + threadIdx.x;
    if(idx >= BATCH * HID) return;
    int sample = idx / HID, neuron = idx % HID;
    float s = b[neuron];
    #pragma unroll
    for(int i=0;i<IN;++i)
        s += W[neuron*IN+i] * x[sample*IN+i];
    h[idx] = s > 0.f ? s : 0.f;       // ReLU
}
__global__ void output(const float* W, const float* b,
                       const float* h, float* y){
    int sample = blockIdx.x * blockDim.x + threadIdx.x;
    if(sample >= BATCH) return;
    float s = b[0];
    #pragma unroll
    for(int i=0;i<HID;++i)
        s += W[i] * h[sample*HID+i];
    y[sample] = s;                    // linear output
}

int main(){
    size_t xBytes = BATCH*IN*sizeof(float);
    size_t hBytes = BATCH*HID*sizeof(float);

    float *dx,*dWh,*dbh,*dWo,*dbo,*dh,*dy;
    cudaMalloc(&dx,xBytes);   cudaMalloc(&dh,hBytes);  cudaMalloc(&dy,BATCH*sizeof(float));
    cudaMalloc(&dWh,HID*IN*sizeof(float));
    cudaMalloc(&dbh,HID*sizeof(float));
    cudaMalloc(&dWo,HID*sizeof(float));
    cudaMalloc(&dbo,OUT*sizeof(float));

    // fill with junk data once (random on host, memcpy is fine)
    float *dummy = (float*)malloc(hBytes> xBytes? hBytes: xBytes);
    cudaMemcpy(dx, dummy, xBytes, cudaMemcpyHostToDevice);
    cudaMemcpy(dWh,dummy,HID*IN*sizeof(float),cudaMemcpyHostToDevice);
    cudaMemcpy(dbh,dummy,HID*sizeof(float),cudaMemcpyHostToDevice);
    cudaMemcpy(dWo,dummy,HID*sizeof(float),cudaMemcpyHostToDevice);
    cudaMemcpy(dbo,dummy,OUT*sizeof(float),cudaMemcpyHostToDevice);

    dim3 block(256);
    cudaEvent_t t0,t1; cudaEventCreate(&t0); cudaEventCreate(&t1);
    cudaEventRecord(t0);
    hidden<<<(BATCH*HID+255)/256,block>>>(dWh,dbh,dx,dh);
    output<<<(BATCH+255)/256,block>>>(dWo,dbo,dh,dy);
    cudaEventRecord(t1); cudaEventSynchronize(t1);
    float ms=0; cudaEventElapsedTime(&ms,t0,t1);
    printf("CUDA forward pass: %.3f ms\\n",ms);
    return 0;
}
