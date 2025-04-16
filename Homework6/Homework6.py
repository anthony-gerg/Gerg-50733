from package.pendulum_notebook import pendulum, main_pend
from package.central_diff import central_difference
from package.fitting import runge_kutta
import numpy as np
import matplotlib.pyplot as plt

#Testing different types of initial parameters for the pendulum problem 
#from Homework 4

pos_theta,pos_omega = main_pend(10,2,g=20,l=2.5,Const=1) #pretty interesting initial plot with high gravity

def weird_function(x):
    return (0.5*np.sin(x))*x

def weird_func_derivative(x):
    return (0.5*np.sin(x))+(0.5*np.cos(x)*x)

time, derivatives = central_difference(-30,30,0.25,weird_function)
time_der = np.arange(-30,30,0.05)
y_vals = weird_func_derivative(time_der)

def ODE_list(li,a,b,c,d,e):
    x= li[0]
    y = li[1]
    dx = (a*(x**(2*(b))))/e - c*e*x#random arbitrary function with some compartmentalizaiton
    dy = d*y - e*c*y + c*e*x - x
    return np.array([dx,dy])

pos_x, pos_y = runge_kutta(1,1,ODE_list,a=10,b=0.01,c=0.1,d=10,e=5,t_0=0,t_f=10,increments=1000)
weird_time = np.arange(0,10,0.01)
fig,axs = plt.subplots(nrows=3,ncols=2,layout='tight',figsize=(20,20))
axs[0,0].plot(np.arange(0,10,0.01),pos_theta)
axs[0,0].set_xlabel('time')
axs[0,0].set_ylabel('THETA')
axs[0,0].set_title(f'Theta over time')
axs[0,1].plot(np.arange(0,10,0.01),pos_omega)
axs[0,1].set_xlabel('time')
axs[0,1].set_ylabel('OMEGA')
axs[0,1].set_title(f'Omega over time')
axs[1,0].scatter(time,derivatives,label='Central Difference')
axs[1,0].plot(time_der,y_vals,label='Actual Derivative',color='r')
axs[1,0].set_xlabel('time')
axs[1,0].set_ylabel('y')
axs[1,0].set_title(f'Central Difference of 0.5*sin(x)*x')
axs[1,0].legend()
axs[2,0].plot(np.arange(0,10,0.001),pos_x)
axs[2,0].set_xlabel('time')
axs[2,0].set_ylabel('x-values')
axs[2,0].set_title('x-values vs time (Runge-Kutta)')
axs[2,1].plot(np.arange(0,10,0.001),pos_y)
axs[2,1].set_xlabel('time')
axs[2,1].set_ylabel('y-values')
axs[2,1].set_title('y-values vs time (Runge-Kutta)')
plt.show()