from input import *
from model import Model
import PK_model_setup as pkmod
from output import *

# # Collect model input data 
# central = central_input()
# peripherals = peripheral_input()
# dosage = dosage_input()

# sys_model = Model(central, peripherals, dosage) # Create Model object

# # Collect protocol input data
# dosing_array = input_doses()
# TMAX = max_time_input()

# # Add solver here

# time_vals, conc_vals = pkmod.PK_solver(sys_model=sys_model, TMAX=TMAX, DOSE_REGIME=dosing_array)

sys_model = Model([10,10], [[5,5]], []) # Create Model object
TMAX = 10
dosing_array = [[1,1,10]]
time_vals, conc_vals = pkmod.PK_solver(sys_model=sys_model, TMAX=TMAX, DOSE_REGIME=dosing_array)

plotPK(time_vals, conc_vals, sys_model.dosage)
# Add plotting here

# Add return graphs and CSV here (CSV currently only outputs model input parameters)

save_csv(sys_model, dosing_array, TMAX, filename='prototypemodel')


