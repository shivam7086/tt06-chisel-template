
`timescale 1ns / 1ps

module tb_PWM_Generator_Verilog;
 // Inputs
 reg clk;
 reg ui_increase_duty;
 reg ui_decrease_duty;
 // Outputs
 wire uo_PWM_OUT;
 // Instantiate the PWM Generator with variable duty cycle in Verilog
 tt_um_PWM_Generator_Verilog DUT(
  .clk(clk),
  .ui_increase_duty(ui_increase_duty), 
  .ui_decrease_duty(ui_decrease_duty), 
  .uo_PWM_OUT(uo_PWM_OUT)
 );
 // Create 100Mhz clock
 initial begin
 clk = 0;
 forever #5 clk = ~clk;
 end 
 initial begin
  ui_increase_duty = 0;
  ui_decrease_duty = 0;
  #100; 
    ui_increase_duty = 1; 
  #100;// increase duty cycle by 10%
    ui_increase_duty = 0;
  #100; 
    ui_increase_duty = 1;
  #100;// increase duty cycle by 10%
    ui_increase_duty = 0;
  #100; 
    ui_increase_duty = 1;
  #100;// increase duty cycle by 10%
    ui_increase_duty = 0;
  #100;
    ui_decrease_duty = 1; 
  #100;//decrease duty cycle by 10%
    ui_decrease_duty = 0;
  #100; 
    ui_decrease_duty = 1;
  #100;//decrease duty cycle by 10%
    ui_decrease_duty = 0;
  #100;
    ui_decrease_duty = 1;
  #100;//decrease duty cycle by 10%
    ui_decrease_duty = 0;
 end
endmodule
