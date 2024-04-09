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
  dut.increase_duty.value = 0
  dut.decrease_duty.value = 0
   
  await ClockCycles(dut.clk, 20)

  # Set the input values, wait one clock cycle, and check the output
  dut._log.info("Test")
  dut.increase_duty.value = 20
  dut.decrease_duty.value = 30

  await ClockCycles(dut.clk, 1)

  assert dut.PMW_OUT.value == 50
