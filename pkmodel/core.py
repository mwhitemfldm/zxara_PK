from input import *
from model import Model
from protocol import Protocol

# # Collect user input data for model
# central = central_input()
# peripherals = peripheral_input()
# dosage = dosage_input()

# sys_model = Model(central, peripherals, dosage) # Create Model object

# Collect protocol input data
dosing_array = protocol_input()
MAX_TIME = max_time_input()

sys_protocol = Protocol(dosing_array, MAX_TIME)

print(sys_protocol.dosing_array)

# Add solver here

# Add plotting here

# Add return graphs and CSV here