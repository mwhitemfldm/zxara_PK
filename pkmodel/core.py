from input import *
from model import Model
from protocol import Protocol
import PK_model_setup as pkmod 

# Collect model input data 
central = central_input()
peripherals = peripheral_input()
dosage = dosage_input()

sys_model = Model(central, peripherals, dosage) # Create Model object

# Collect protocol input data
dosing_array = protocol_input_steady()
dosing_array = protocol_input_instantaneous(dosing_array)
MAX_TIME = max_time_input()

sys_protocol = Protocol(dosing_array, MAX_TIME)

# Add solver here

time_vals, conc_vals = pkmod.PK_solver(sys_model = sys_model, TMAX = MAX_TIME, DOSE_REGIME = dosing_array)
# Add plotting here

# Add return graphs and CSV here