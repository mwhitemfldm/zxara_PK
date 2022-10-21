from input import central_input, peripheral_input, dosage_input, input_doses, max_time_input, check_error_string_input
from model import Model
from solver import PK_solver
from output import plotPK, save_data, save_params

plot_data = []
add_model = None

while add_model != 'N':

    model_name = input('Enter model name: ')

    # Collect model input data 
    central = central_input()
    peripherals = peripheral_input()
    dosage = dosage_input()

    sys_model = Model(central, peripherals, dosage)  # Create Model object

    # Collect protocol input data
    dosing_array = input_doses()
    TMAX = max_time_input()

    sol_values = PK_solver(sys_model=sys_model, TMAX=TMAX, DOSE_REGIME=dosing_array) 

    save_data(sol_values, dosage, model_name)
    save_params(sys_model, dosing_array, TMAX, model_name)

    plot_data.append([sol_values[0], sol_values[1], dosage])

    add_model = check_error_string_input(add_model, ['Y', 'N'], 'Do you want to compare another model? ')

graph_name = input('Enter graph name: ')
plotPK(plot_data, graph_name)

# Add return graphs and CSV here (CSV currently only outputs model input parameters)
# TODO: modify to save multiple data
# TODO: allow user to choose save directory for CSV and PNG


