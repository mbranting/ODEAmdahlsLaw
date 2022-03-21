readme.md
McKenna L. Branting
-------------------
Included:
-------------------
this README, 
ODEAmdahlsLaw.py file, 
output from executing python file (graph),
Visualize ODE of Amdahl.docx documentation

-------------------
Packages 
------------------
Install packages for 
- numpy 
Using pip (sudo apt install python-pip) 
Install numpy (pip install numpy or pip3 install numpy (depending on version of Python))
Verify numpy installation (pip show numpy / pip3 show numpy)
(program code includes importing the package -- import numpy as np)
- scipy
Using pip install scipy (pip install scipy)
- matplotlib
Using pip (pip install matplotlib)
(program code includes importing the package -- import matplotlib.pyplot as plt)
- odeint
(program code imports the package using scipy from scipy.integrate import odeint)

------------------
Design Decisions & Project Issues
------------------
From the flowchart shown in the documentation, the code was modeled based on this layout. 
The model function was implemented to provide the change of speedup given the number of processors. 
4 different constant values for f (the amount of the code that was parallelizable), were examined in the program.
The data for these various constants were shown, as well as graphed. 

Various project issues that were encountered involved designing the program to model not one constant, but four. 
Another issue involved figuring out how to implement a graph legend.

-------------------
Results 
-------------------
Running the code will result in:
- data for the different values of the constant (f = 0.95, 0.9, 0.85, 0.8)
- graph modeling the results

