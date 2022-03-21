# McKenna L. Branting
# code packages used: matplotlib, scipy, odeint, numpy
# approach to implementation:
# 1. Started with basic framework from in class activity to structure program (import statements, def model, plot, etc.)
# 2. Commented what needed to be done in the code (applying ds/dn equation of amdahl's law, etc.)
# 3. defined a function that returned the correct value for ds/dn
# 4. defined variables
# 5. developed program to plot data and list data
# 6. created labels, titles, and legend for plot

# equation being solved: Amdahl's Law where
# (speedup = (time to execute program on single processor) / (time to execute program on N parallel processors)
# speedup = (T(1-f)+Tf) / (T((1-f)+(Tf)/N) = 1 / ((1-f)+f/N)

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


# function that returns dy/dt
def model(s, n, f):
    dsdn = f / ((f - 1) * n - f) ** 2
    return dsdn


# input the initial condition of the equation
s0 = 0

# the data points for the x axis
n = np.linspace(0, 3000)

# solves the ODE for variable f = 0.95
f = 0.95
y1 = odeint(model, s0, n, args=(f,))

# solves the ODE for variable f = 0.90
f = 0.90
y2 = odeint(model, s0, n, args=(f,))

# solves the ODE for variable f = 0.85
f = 0.85
y3 = odeint(model, s0, n, args=(f,))

# solves the ODE for variable f = 0.80
f = 0.8
y4 = odeint(model, s0, n, args=(f,))

# prints the data points for line 1
print('Data for line 1 (when f = 0.95)')
print(n, y1)
# prints the data points for line 2
print('Data for line 2 (when f = 0.9)')
print(n, y2)
# prints the data points for line 3
print('Data for line 3 (when f = 0.85)')
print(n, y3)
# prints the data points for line 4
print('Data for line 4 (when f = 0.8)')
print(n, y4)

# plots the results of the ODE
plt.plot(n, y1)
plt.plot(n, y2)
plt.plot(n, y3)
plt.plot(n, y4)

# graph title
plt.title('The Impact of the Number of Processors on the Speedup of a System')
# x axis label
plt.xlabel('Number of Processors')
# y axis label
plt.ylabel('Change in Speedup (ds/dn)')

# legend for graph
labels = ['0.95', '0.90', '0.85', '0.80']
plt.legend(labels)
# shows the graph
plt.show()
