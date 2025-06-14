module cnn_accelerator (
    input logic clk,
    input logic rst,
    input logic valid_in,
    input logic [7:0] pixel_in,
    output logic [2:0] emotion_out,
    output logic valid_out
);

    always_ff @(posedge clk or posedge rst) begin
        if (rst) begin
            emotion_out <= 0;
            valid_out <= 0;
        end else if (valid_in) begin
            // Dummy hardware prediction logic: echo lower 4 bits of pixel
            emotion_out <= pixel_in[2:0];
            valid_out <= 1;
        end else begin
            valid_out <= 0;
        end
    end
endmodule