/////////////////////////////////////////////////////////////
// Created by: Synopsys Design Compiler(R)
// Version   : Q-2019.12-SP3
// Date      : Sun Jun 15 02:02:48 2025
/////////////////////////////////////////////////////////////


module cnn_accelerator ( clk, rst, valid_in, pixel_in, emotion_out, valid_out
 );
  input [7:0] pixel_in;
  output [2:0] emotion_out;
  input clk, rst, valid_in;
  output valid_out;


  \**SEQGEN**  valid_out_reg ( .clear(rst), .preset(1'b0), .next_state(
        valid_in), .clocked_on(clk), .data_in(1'b0), .enable(1'b0), .Q(
        valid_out), .synch_clear(1'b0), .synch_preset(1'b0), .synch_toggle(
        1'b0), .synch_enable(1'b1) );
  \**SEQGEN**  \emotion_out_reg[2]  ( .clear(rst), .preset(1'b0), .next_state(
        pixel_in[2]), .clocked_on(clk), .data_in(1'b0), .enable(1'b0), .Q(
        emotion_out[2]), .synch_clear(1'b0), .synch_preset(1'b0), 
        .synch_toggle(1'b0), .synch_enable(valid_in) );
  \**SEQGEN**  \emotion_out_reg[1]  ( .clear(rst), .preset(1'b0), .next_state(
        pixel_in[1]), .clocked_on(clk), .data_in(1'b0), .enable(1'b0), .Q(
        emotion_out[1]), .synch_clear(1'b0), .synch_preset(1'b0), 
        .synch_toggle(1'b0), .synch_enable(valid_in) );
  \**SEQGEN**  \emotion_out_reg[0]  ( .clear(rst), .preset(1'b0), .next_state(
        pixel_in[0]), .clocked_on(clk), .data_in(1'b0), .enable(1'b0), .Q(
        emotion_out[0]), .synch_clear(1'b0), .synch_preset(1'b0), 
        .synch_toggle(1'b0), .synch_enable(valid_in) );
endmodule

