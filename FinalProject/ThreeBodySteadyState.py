#Gerg: Venus Saturn Mercury
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as an
import matplotlib
#matplotlib.use("Agg")
##############################################################################################
###                               A.U. and days                                            ###
##############################################################################################

def newtons_law(m1,m2,x1,x2,y1,y2): 
  x_displacement = x2-x1
  y_displacement = y2-y1
  r_displacement = np.sqrt(x_displacement**2 + y_displacement**2)
  # if r_displacement < 0.1:
  #   r_displacement = 0
  #   F_x = 0 
  #   F_y = 0
  # else:
  main_force_magnitude = (1*m1*m2)/(r_displacement**2)
  F_x = (main_force_magnitude*x_displacement)/r_displacement
  F_y = (main_force_magnitude*y_displacement)/r_displacement
  return np.array([F_x/m1, F_y/m1]) #returning accelerations due to the graviational force from that object

def diff_eqs(li,ax,ay,t):
  x = li[0]
  y = li[1]
  vx = li[2]
  vy = li[3]
  change_vx = ax
  change_vy = ay
  change_x = vx
  change_y = vy
  return np.array([change_x,change_y,change_vx,change_vy])


time = np.arange(0,20,0.002)
step_size = 0.002
m = [1.0,1.0,1.0]
x = [-1,1,0]
y = [0,0,0]
vx = [0.347111,0.347111,-2*0.347111]
vy = [0.532728,0.532728,-2*0.532728]

r = np.array([x,y,vx,vy])
positional_x = np.zeros(10000,dtype=object)
positional_y = np.zeros(10000,dtype=object)
velocity_x = np.zeros(10000,dtype=object)
velocity_y = np.zeros(10000,dtype=object)
for i in range(len(time)):
  positional_x[i] = np.copy(r[0])
  positional_y[i] = np.copy(r[1])
  velocity_x[i] = np.copy(r[2])
  velocity_y[i] = np.copy(r[3])
  for z in range(len(x)):
    accel = np.array([0.0,0.0])
    for c in range(len(x)):
      if z != c:
        accel += newtons_law(m[z],m[c],r[0,z],r[0,c],r[1,z],r[1,c])
    k_1 = step_size*diff_eqs(r[:,z],accel[0],accel[1],time[i])
    k_2 = step_size*diff_eqs(r[:,z]+(k_1/2),accel[0],accel[1],time[i]+(step_size/2))
    k_3 = step_size*diff_eqs(r[:,z]+(k_2/2),accel[0],accel[1],time[i]+(step_size/2))
    k_4 = step_size*diff_eqs(r[:,z]+(k_3),accel[0],accel[1],time[i]+(step_size))
    r[:,z] += (1/6)*(k_1+(2*k_2)+(2*k_3)+k_4)
positional_x.flatten
positional_y.flatten
velocity_x.flatten
velocity_y.flatten

#plt.cla()
figs = plt.figure(figsize = (10,10))
axes = figs.add_subplot(1,1,1)
axes.set_ylim(-2, 2)
axes.set_xlim(-2,2)
for i in range(len(positional_x)):
  axes.scatter(positional_x[i],positional_y[i],color=['k','r','b'])
plt.savefig("C:\\Users\\gergy\\Downloads\\threebody.png")


# def animation_function(i):
#     axes.set_ylim(-5, 5)
#     axes.set_xlim(-5,5)
#     plt.scatter(positional_x[i],positional_y[i],color=['k','r','b'])
#     return plt
    



# animation = an.FuncAnimation(figs, animation_function,1000,interval = 0.1)
# # mywriter = an.FFMpegFileWriter(fps=60)
# animation.save(filename="C:\\Users\\gergy\\Downloads\\threebody.gif", writer="pillow")

# def energy(x,y,vx,vy,mass_list,time):
#   energy = np.zeros((10000,4),dtype=object)
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
#           poten += (1) *( mass_list[z]*mass_list[c])/r
#       velo = np.sqrt(vx[i][z]**2 + vy[i][z]**2)
#       kinetic += 1/2 * mass_list[z]*velo**2
#       total += (kinetic + poten)
#       energy[i,z] = np.copy([i,total])
#   for k in range(len(energy)):
#     accum = 0
#     for g in range(len(x[0])):
#       accum += energy[k,g][1]
#     system_energy += [[k,accum/1.0002]]
#   print(system_energy)
#   return system_energy

# sys = energy(positional_x,positional_y,velocity_x,velocity_y,m,time)
# sys = np.array(sys)
# plt.cla()
# plt.plot(sys[:,0],sys[:,1])
# plt.show()
