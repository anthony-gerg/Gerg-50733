import numpy as np
import matplotlib.pyplot as plt

def pendulum(r,t,g,l,Const):
    theta = r[0]
    omega = r[1]
    d_theta = omega
    d_omega = - (g / l) * np.sin(theta) + Const*np.cos(theta) * np.sin(omega*t)
    return np.array([d_theta, d_omega], float)

def main_pend(theta,omega,g=9.81,l=0.1,Const=2,t_0=0,t_f=10,increments=1000):
    step = (t_f-t_0)/increments 
    time_range = np.arange(t_0,t_f,step)   
    r = [theta,omega]
    positional_theta = []
    positional_omega = []
    for i in time_range:
        positional_theta.append(r[0])
        positional_omega.append(r[1])
        k_1 = step*pendulum(r,i,g,l,Const)
        k_2 = step*pendulum(r+(k_1/2),i+(step/2),g,l,Const)
        k_3 = step*pendulum(r+(k_2/2),i+(step/2),g,l,Const)
        k_4 = step*pendulum(r+(k_3),i+(step),g,l,Const)
        r += (1/6)*(k_1+(2*k_2)+(2*k_3)+k_4)
    return [positional_theta,positional_omega]

