#Gerg: Venus Saturn Mercury
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as an
import matplotlib
matplotlib.use("Agg") #Turn off for normal plots!!!
##############################################################################################
###                               A.U. and days                                            ###
##############################################################################################

def newtons_law(m1,m2,x1,x2,y1,y2): 
  x_displacement = x2-x1
  y_displacement = y2-y1
  r_displacement = np.sqrt(x_displacement**2 + y_displacement**2) 
  main_force_magnitude = (2.963e-4*m1*m2)/r_displacement**2 #lol ugly gravitational constant
  F_x = main_force_magnitude*x_displacement/r_displacement
  F_y = main_force_magnitude*y_displacement/r_displacement
  return np.array([F_x/m1, F_y/m1]) #returning accelerations due to the graviational force from that object

def diff_eqs(li,ax,ay,t):
  x = li[0]
  y = li[1]
  vx = li[2]
  vy = li[3]
  change_vx = ax #very obvious kinematic equations that definitely didn't take me forever to realize
  change_vy = ay #cause I'm stupid
  change_x = vx
  change_y = vy
  return np.array([change_x,change_y,change_vx,change_vy])


time = np.arange(0,12000,6)
step_size = 6
m = [1.0,1.66e-6,2.447e-6,2.857e-4]#Initial params, [sun,mercury,venus,saturn] for all vals
x = [0,-3.078656494898613E-02,-4.808415448965829E-01,9.515039809012718E+00]
y = [0,-4.682118021511205E-01,-5.503806186416326E-01,-1.164440062969584E+00]
vx = [0,2.245440929727949E-02,1.510190477427734E-02,3.680856479160571E-04]
vy = [0,-1.325988462644521E-04,-1.339902227426612E-02,5.525160539050213E-03]


r = np.array([x,y,vx,vy])
positional_x = np.zeros(2000,dtype=object)#however long your time range is, you MUST adjust these
positional_y = np.zeros(2000,dtype=object)
velocity_x = np.zeros(2000,dtype=object)
velocity_y = np.zeros(2000,dtype=object)
for i in range(len(time)):
  positional_x[i] = np.copy(r[0])
  positional_y[i] = np.copy(r[1])
  velocity_x[i] = np.copy(r[2])
  velocity_y[i] = np.copy(r[3])
  for z in range(len(x)):
    accel = np.array([0.0,0.0])
    for c in range(len(x)):
      if z != c:
        accel += newtons_law(m[z],m[c],r[0,z],r[0,c],r[1,z],r[1,c])#DO NOT TOUCH!!!!
    k_1 = step_size*diff_eqs(r[:,z],accel[0],accel[1],time[i])
    k_2 = step_size*diff_eqs(r[:,z]+(k_1/2),accel[0],accel[1],time[i]+(step_size/2))
    k_3 = step_size*diff_eqs(r[:,z]+(k_2/2),accel[0],accel[1],time[i]+(step_size/2))
    k_4 = step_size*diff_eqs(r[:,z]+(k_3),accel[0],accel[1],time[i]+(step_size))
    r[:,z] += (1/6)*(k_1+(2*k_2)+(2*k_3)+k_4)
positional_x.flatten
positional_y.flatten
velocity_x.flatten
velocity_y.flatten


plt.cla()
fig = plt.figure(figsize = (10,10))
axes = fig.add_subplot(1,1,1)
# axes.set_ylim(-2,2)
# axes.set_xlim(-2,2)
# for i in range(len(positional_x)):
#   axes.scatter(positional_x[i],positional_y[i],color=['k','r','b','g'])
# axes.text(0.0,-1.75,'Sun=Black,Mercury=Red,Venus=Blue')
# plt.savefig("C:\\Users\\gergy\\Downloads\\orbi.png")



def animation_function(i):
    plt.cla()
    axes.set_ylim(-10, 10)
    axes.set_xlim(-10,10)
    plt.scatter(positional_x[i][0],positional_y[i][0],color = 'k')
    plt.scatter(positional_x[i][3],positional_y[i][3],color='g')
    # plt.legend(['Sun','Mercury','Venus','Saturn'])
    #plt.scatter(positional_x[i],positional_y[i],color=['k','r','b','g'])
    return plt
    



animation_placeholder = an.FuncAnimation(fig, animation_function,2000)
animation_placeholder.save(filename="C:\\Users\\gergy\\Downloads\\orbit_good.gif", writer="ffmpeg")

# def energy(x,y,vx,vy,mass_list,time):
#   energy = np.zeros((300000,4),dtype=object)
#   system_energy = []
#   print(energy)
#   for z in range(len(x[0])):
#     for i in range(len(time)):
#       poten = 0
#       kinetic = 0
#       total = 0
#       for c in range(len(x[i])):
#         if c != z:
#           r = 0
#           r = np.sqrt((x[i][c]-x[i][z])**2 + (y[i][c]-y[i][z])**2+0.01**2)
#           poten += (-2.963e-4 * mass_list[z]*mass_list[c])/r
#       velo = np.sqrt(vx[i][z]**2 + vy[i][z]**2)
#       kinetic += 1/2 * mass_list[z]*velo**2
#       total += (kinetic + poten)
#       energy[i,z] = np.copy([i,total])
#   for k in range(len(energy)):
#     accum = 0
#     for g in range(len(x[0])):
#       accum += energy[k,g][1]
#     system_energy += [[k,accum/1.00002]]
#   print(system_energy)
#   return system_energy

# sys = energy(positional_x,positional_y,velocity_x,velocity_y,m,time)
# sys = np.array(sys)
# plt.cla()
# plt.plot(sys[:,0],sys[:,1])
# plt.xlabel('Time')
# plt.ylabel('Total Energy')
# plt.show()
