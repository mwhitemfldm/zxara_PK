from input import *
from model import Model

# Collect user input data for model
central = central_input()
peripherals = peripheral_input()
dosing = dosing_input()

sys_model = Model(central, peripherals, dosing) # Create Model object

# # Collect dosage function input data
# dosage_fn = dosage_function_input()