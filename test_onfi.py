import cocotb
from cocotb.clock import Clock
from cocotb.triggers import FallingEdge, Timer
from commands import txn, cmds

async def generate_clock(dut):
    """Generate clock pulses."""
    cocotb.start_soon(Clock(dut.clk, 1, units="ns").start())

@cocotb.test()
async def test_reset(dut):
    """Test reset command."""
    await cocotb.start(generate_clock(dut))
    await txn('reset')
    await Timer(10, units='ns')

@cocotb.test()
async def test_read_device_id(dut):
    """Test read device ID command."""
    await cocotb.start(generate_clock(dut))
    addr = [0x00]  
    rv = await txn('read_device_id', addr=addr)
    dut._log.info(f"Read Device ID: {rv}")

@cocotb.test()
async def test_block_erase(dut):
    """Test block erase command."""
    await cocotb.start(generate_clock(dut))
    addr = [0x00, 0x00, 0x01]  
    await txn('block_erase', addr=addr)
    await Timer(10, units='ns')

@cocotb.test()
async def test_standard_read(dut):
    """Test standard read command."""
    await cocotb.start(generate_clock(dut))
    addr = [0x00, 0x00, 0x00, 0x00, 0x00]  
    rv = await txn('standard_read', addr=addr)
    dut._log.info(f"Standard Read: {rv}")
