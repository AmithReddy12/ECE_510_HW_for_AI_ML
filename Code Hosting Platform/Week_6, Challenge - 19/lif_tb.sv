// ---------------- lif_tb.sv ----------------
`timescale 1ns/1ps
module lif_tb;
    logic clk = 0; always #5 clk = ~clk;   // 100 MHz clock
    logic rst_n = 0;
    logic I = 0;
    logic S;

    // DUT
    lif_neuron dut(
        .clk(clk),
        .rst_n(rst_n),
        .I(I),
        .S(S)
    );

    // waveform dump
    initial begin
        $dumpfile("lif.vcd");
        $dumpvars(0, lif_tb);
    end

    // stimulus
    initial begin
        // global reset
        repeat (3) @(posedge clk);
        rst_n = 1;

        // 1. constant sub‑threshold
        I = 1;  repeat (10) @(posedge clk);
        I = 0;  repeat (5)  @(posedge clk);

        // 2. accumulate until spike
        I = 1;  repeat (20) @(posedge clk);
        I = 0;  repeat (10) @(posedge clk);

        // 3. leakage only
        repeat (30) @(posedge clk);

        // 4. single strong tick
        I = 1;  @(posedge clk);
        I = 0;  repeat (10) @(posedge clk);

        $finish;
    end
endmodule
