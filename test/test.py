# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: MIT

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles

@cocotb.test()
async def test_project(dut):
  dut._log.info("Start")
  
  # Our example module doesn't use clock and reset, but we show how to use them here anyway.
  clock = Clock(dut.clk, 20, units="ns")
  cocotb.start_soon(clock.start())

  # Reset
  dut._log.info("Reset")
  dut.ena.value = 1
  dut.ui_increase_duty.value = 1
  dut.ui_decrease_duty.value = 0

   
  await ClockCycles(dut.clk, 20)
  
  # Set the input values, wait one clock cycle, and check the output
  dut._log.info("Test")
  dut.ui_increase_duty.value = 1
  dut.ui_decrease_duty.value = 0

  await ClockCycles(dut.clk, 1)

  assert dut.uo_PWM_OUT.value == 1
