module lif_neuron #(
    parameter W       = 8,    // total bits  (Q W-F . F)
    parameter FRACT   = 4,    // fractional bits
    parameter signed [W-1:0] LAMBDA = 8'sd12, // 0.75  in Q4.4
    parameter signed [W-1:0] THRESH = 8'sd16  // 1.0   in Q4.4
)(
    input  logic clk, rst_n,
    input  logic I,          // binary input 0/1
    output logic S           // spike output
);
    logic signed [W-1:0] P;  // membrane potential

    always_ff @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            P <= '0;
            S <= 1'b0;
        end else begin
            // leak & integrate
            P <= (LAMBDA * P) >>> FRACT  +  (I << FRACT);

            if (P >= THRESH) begin
                S <= 1'b1;
                P <= P - THRESH;   // reset (could also set to 0)
            end else begin
                S <= 1'b0;
            end
        end
    end
endmodule
