import numpy as np
import csv

def plotPK(time, concentration, n_models):    
    '''Plot pharmacokinetic models.

    Plots different pharmacokinetic models next to each other.
 
    :param time: list of time points
    :param concentration: list of concentration points
    :param n_models: integer defining number of pharmacokinetic models to plot
    :returns: None, saves plot under PKplot.png
    '''

    import matplotlib.pyplot as plt
  
    fig, axes = plt.subplots(nrows= 1, ncols= n_models)

    if n_models == 1: #otherwise error that AxesSubplot object is not subscriptable

        axes.plot(time, concentration)
        axes.set_title('model 1')
        axes.set_ylabel('drug mass [ng]')
        axes.set_xlabel('time [h]')
        axes.legend(['q1', 'q2', 'q3', 'q4', 'q5'])
    
    else:

        for i in range(n_models):
            
            j = i+1 # axes and array indices start with zero while model should start with 1
            axes[i].plot(time[i], concentration[i])
            axes[i].set_title(f'model {j}')
            axes[i].set_ylabel('drug mass [ng]')
            axes[i].set_xlabel('time [h]')
            axes[i].legend(['q1', 'q2', 'q3', 'q4', 'q5'])
    
    
    fig.tight_layout()
    fig.savefig("PKplot.png")
    plt.show()

# plotPK(np.array([[1,2,3],[2,3,1],[3,1,2]]), np.array([[4,5,6],[5,6,4],[6,4,5]]), 3) this is how i thought the input would look like



def save_csv(model,dosing_array,max_time,filename):
    '''
Module to save model parameters as well as solution output
    '''
    input_dict = vars(model)

    # rename keys to make more detailed
    input_dict['Central compartment (volume in mL, clearance in mL/h)'] = input_dict.pop('central')
    input_dict['Peripheral compartment(s) (volume in mL, transition rate in mL/h)'] = input_dict.pop('peripherals')
    input_dict['Absorption rate for dosage compartment (/h) if subcutaneous dosing'] = input_dict.pop('dosage')
    input_dict['Start/end time of dose and dose amount (ng)'] = dosing_array
    input_dict['Maximum time'] = max_time

    with open(filename+'.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=input_dict.keys())
        writer.writeheader()
        writer.writerow(input_dict)
    
    # TODO: add solution output and save as csv