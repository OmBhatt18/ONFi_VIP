module dummy_dut(input clk);
    initial begin
        $display("Dummy DUT");
        $dumpfile("waveform.vcd"); 
        $dumpvars(0, dummy_dut); 
    end
endmodule
