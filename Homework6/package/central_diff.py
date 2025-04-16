import numpy as np

def central_difference(start,stop,step,func):
    plotting_values = []
    interative_data = np.arange(start,stop,step)
    plotting_values += [[i,(func(i+(step/2)) - func(i-(step/2)))/step] for i in interative_data]
    true_plotting_values = np.array(plotting_values[1:])
    return [true_plotting_values[:,0],true_plotting_values[:,1]]