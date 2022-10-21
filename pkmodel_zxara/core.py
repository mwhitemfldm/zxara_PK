from input import *
from model import Model
import PK_model_setup as pkmod
from output import save_csv

# Collect model input data 
central = central_input()
peripherals = peripheral_input()
dosage = dosage_input()

sys_model = Model(central, peripherals, dosage) # Create Model object

# Collect protocol input data
dosing_array = input_doses()
MAX_TIME = max_time_input()

# Add solver here

time_vals, conc_vals = pkmod.PK_solver(sys_model = sys_model, TMAX = MAX_TIME, DOSE_REGIME = dosing_array)
# Add plotting here

# Add return graphs and CSV here (CSV currently only outputs model input parameters)

save_csv(sys_model,dosing_array,MAX_TIME,filename = 'prototypemodel')


