from input import *
from model import Model

# # Collect user input data for model
# central = central_input()
# peripherals = peripheral_input()
# dosage = dosage_input()

# sys_model = Model(central, peripherals, dosage) # Create Model object

# Collect dosage protocol input data
STEADY_DOSAGE, dosage_protocol = dosage_protocol_input()

print(STEADY_DOSAGE)
print(dosage_protocol)

# Add solver here

# Add plotting here

# Add return graphs and CSV here