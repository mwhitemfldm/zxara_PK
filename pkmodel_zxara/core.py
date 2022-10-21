from input import *
from model import Model
import PK_model_setup as pkmod
from output import *

plot_data = []

# Collect model input data 
central = central_input()
peripherals = peripheral_input()
dosage = dosage_input()

sys_model = Model(central, peripherals, dosage) # Create Model object

# Collect protocol input data
dosing_array = input_doses()
TMAX = max_time_input()

sol_values = pkmod.PK_solver(sys_model=sys_model, TMAX=TMAX, DOSE_REGIME=dosing_array)

plot_data.append([sol_values[0], sol_values[1], sys_model.dosage])

add_model = check_error_string_input(add_model, ['Y','N'],'Do you want to compare another model? ')

plotPK(plot_data)
# Add plotting here

# Add return graphs and CSV here (CSV currently only outputs model input parameters)

save_csv(sys_model, dosing_array, TMAX, filename='prototypemodel')
