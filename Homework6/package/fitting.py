import numpy as np
def runge_kutta(x,y,func,a,b,c,d,e,t_0,t_f,increments):
    increments = 10000
    step = (t_f-t_0)/increments
    time_range = np.arange(t_0,t_f,step)
    r = [x,y]
    positional_x = []
    positional_y = []
    for i in time_range:
        positional_x.append(r[0])
        positional_y.append(r[1])
        k_1 = step*func(r,a,b,c,d,e)
        k_2 = step*func(r+(k_1/2),a,b,c,d,e)
        k_3 = step*func(r+(k_2/2),a,b,c,d,e)
        k_4 = step*func(r+(k_3),a,b,c,d,e)
        r += (1/6)*(k_1+(2*k_2)+(2*k_3)+k_4)
    return [positional_x,positional_y]