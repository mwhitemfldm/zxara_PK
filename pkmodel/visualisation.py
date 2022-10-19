# function that plots different pharmacokinetic models as different subplots

def plotPK(time, concentration):    
    '''Plot pharmacokinetic models.

    Plots different pharmacokinetic models next to each other.
 
    :param time: list of time points
    :param concentration: list of concentration points
    :returns: None, saves plot under PKplot.png
    '''

    import matplotlib.pyplot as plt
    
    n_models = len(time)
  
    fig, axes = plt.subplots(nrows= 1, ncols= n_models, figsize = (20,8))
    
    for i in range(n_models):
        i = i-1
        axes[i].plot(time[i], concentration[i])

    fig.savefig("PKplot.png")
    plt.show()


plotPK([[1,2,3],[2,3,1],[3,1,2]], [[4,5,6],[5,6,4],[6,4,5]])