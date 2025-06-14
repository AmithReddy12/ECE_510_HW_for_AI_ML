#include "Vcnn_accelerator.h"
#include "verilated.h"
#include <iostream>
#include <fstream>
#include <vector>

vluint64_t main_time = 0;
double sc_time_stamp() { return main_time; }

int main(int argc, char **argv) {
    Verilated::commandArgs(argc, argv);
    Vcnn_accelerator* top = new Vcnn_accelerator;

    std::ifstream fin("input_image.txt");
    float val;
    std::vector<int> pixels;

    while (fin >> val)
        pixels.push_back((int)(val * 255));

    top->rst = 1;
    top->clk = 0;
    top->eval();
    top->clk = 1;
    top->eval();
    top->rst = 0;

    for (int i = 0; i < pixels.size(); ++i) {
        top->pixel_in = pixels[i];
        top->valid_in = 1;

        top->clk = 0;
        top->eval();
        main_time++;

        top->clk = 1;
        top->eval();
        main_time++;

        if (top->valid_out) {
            std::cout << (int)top->emotion_out << std::endl;
            break; // Output once
        }
    }

    delete top;
    return 0;
}
