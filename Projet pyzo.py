import pandas as pd
import numpy as np
import matplotlib
from matplotlib import pyplot as plt

data = pd.read_csv("/Users/carll/Documents/EIVP/IVP1/Python/Projet/EIVP_KM.csv",delimiter=";")

x=data[data.id==1].sent_at
y=data[data.id==1].lum

data.plot(x,y)
plt.show()