# function that plots different pharmacokinetic models as different subplots
import numpy as np

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
    
    for i in range(n_models):
        
        j = i+1 # axes and array indices start with zero while model should start with 1
        axes[i].plot(time[i], concentration[i])
        axes[i].set_title(f'model {j}')

    fig.tight_layout()
    fig.savefig("PKplot.png")
    plt.show()

plotPK(np.array([[1,2,3],[2,3,1],[3,1,2]]), np.array([[4,5,6],[5,6,4],[6,4,5]]), 3)