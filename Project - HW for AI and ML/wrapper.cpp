#include "Vcnn_accelerator.h"
#include "verilated.h"
#include <iostream>

class CNNAcceleratorWrapper {
public:
    Vcnn_accelerator* dut;
    vluint64_t main_time = 0;

    CNNAcceleratorWrapper() {
        dut = new Vcnn_accelerator;
        Verilated::traceEverOn(true);
    }

    void reset() {
        dut->rst = 1;
        tick();
        dut->rst = 0;
    }

    void tick() {
        dut->clk = 0;
        dut->eval();
        main_time++;

        dut->clk = 1;
        dut->eval();
        main_time++;
    }

    void load_pixel(uint8_t pixel) {
        dut->pixel_in = pixel;
        dut->valid_in = 1;
        tick();
        dut->valid_in = 0;
        tick();
    }

    uint8_t get_emotion() {
        return dut->emotion_out;
    }

    ~CNNAcceleratorWrapper() {
        delete dut;
    }
};
