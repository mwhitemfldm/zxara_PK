import numpy as np
import csv

def plotPK(plot_data):   
    # time, concentration, dosage_comp, n_models=1
    '''Plot pharmacokinetic models.

    Plots different pharmacokinetic models next to each other.
    
    Parameters:
    plot_data: list of lists
    time (list): Array of time points / h
    concentration (list): List of concentration points # TODO: Conc? Units?
    dosage_comp (list): From Model object. Empty if no dosage compartment.
    n_models: Number of different models to plot and compare. Default value 1.

    Returns:
    None, plot saved as PKplot.png
    '''

    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(nrows=1, ncols=len(plot_data))

    ylabel = 'Drug mass / ng'  # TODO: Conc?
    xlabel = 'Time / h '
    legend = ['Dosage compartment', 'Central compartment']
    # Add peripherals to legend
    for i in range(0, plot_data[0][1].shape[1]-2):
        legend.append(f"Peripheral compartment {i+1}")

    # Strip dosage compartment data if non-existant
    if plot_data[0][2] == []:
        plot_data[0][0] = np.delete(plot_data[0][0], 0, 1)
        plot_data[0][1] = np.delete(plot_data[0][1], 0, 1)
        legend.remove('Dosage compartment')

    if len(plot_data):  # Otherwise error that AxesSubplot object is not subscriptable
        axes.plot(plot_data[0][0], plot_data[0][1])
        axes.set_title('Model 1')
        axes.set_ylabel(ylabel)
        axes.set_xlabel(xlabel)
        axes.legend(legend)
    
    # TODO: Fix for multiple models
    #  else:

    #     for i in range(n_models):
            
    #         j = i+1 # axes and array indices start with zero while model should start with 1
    #         axes[i].plot(time[i], concentration[i])
    #         axes[i].set_title(f'Model {j}')
    #         axes[i].set_ylabel(ylabel)
    #         axes[i].set_xlabel(xlabel)
    #         axes[i].legend(legend)
    
    fig.tight_layout()
    fig.savefig("PKplot.png")
    plt.show()


def save_csv(model,dosing_array,max_time,filename):
    '''
    Module to save model parameters as well as solution output
    '''
    input_dict = vars(model)

    # rename keys to make more detailed
    input_dict['Central compartment [volume in mL, clearance in mL/h]'] = input_dict.pop('central')
    input_dict['Peripheral compartment(s) [volume in mL, transition rate in mL/h]'] = input_dict.pop('peripherals')
    input_dict['Absorption rate for dosage compartment (/h) if subcutaneous dosing'] = input_dict.pop('dosage')
    input_dict['Start/end time of dose and dose amount (ng)'] = dosing_array
    input_dict['Maximum time'] = max_time

    with open(filename+'.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=input_dict.keys())
        writer.writeheader()
        writer.writerow(input_dict)

    # TODO: Modify CSV input parameters (lists are saved as strings)