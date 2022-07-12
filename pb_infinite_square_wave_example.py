# example: pulse blaster pin cycles high / low indefinitely

from pulseblaster.PBInd import PBInd
import pulseblaster.spinapi

cycle_length = 10 * pulseblaster.spinapi.us  # micro seconds
hardware_pins = [23] # using pin 23 (AOM modulation)
delays = []          # delays for each individual channel
N=float('inf')       # number of loops (N = float('inf') to repeat indefinitely

pb=PBInd(pins=hardware_pins,
		 on_time=cycle_length,
		 DEBUG_MODE=0,
		 auto_stop=0) # default resolution is 50 ns


# select board 1
pb.spinapi.pb_select_board(1)

# initialize board
if pb.spinapi.pb_init() != 0:
	print("Error initializing board: %s" % pb.spinapi.pb_get_error())
	input("Please press a key to continue.")
	exit(-1)

# Configure the core clock
pb.spinapi.pb_core_clock(100 * pulseblaster.spinapi.MHz) # MHz
pb.spinapi.pb_reset()
# initialize PBInd object to individually program pulse blaster pins

#program hardware_pins to be on from t0=0 to tend=cycle_length
pb.spinapi.pb_start_programming(0)
pb.on(hardware_pins[0],0,cycle_length//2)
pb.program(delays,N)
pb.spinapi.pb_stop_programming()


#trigger the board
pb.spinapi.pb_reset()
pb.spinapi.pb_start()

#to stop, use pb_stop()
pb.spinapi.pb_stop()

#to close connection to pulseblaster
pb.spinapi.pb_close()
