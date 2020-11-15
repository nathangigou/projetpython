import pandas as pd
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import datetime

data = pd.read_csv("/Users/carll/Documents/EIVP/IVP1/Python/Projet/EIVP_KM.csv",delimiter=";")


# def Converttime(n):
#     L=len(data[data.id==n].sent_at)
#     # Nb de mesures prises par le capteur n
#     l=[]
#     # Création de la liste des dates
#     for i in range(L):
#         l.append(datetime.datetime.strptime(data.sent_at.loc[i+data[data.id==n].index[0]], "%Y-%m-%d %H:%M:%S %z"))
#         # Ajout à la liste la chaine de caractère sent_at convertie en un objet datetime
#     return l

def courbes(v,capteur):
    ld=Converttime(capteur)
    x=matplotlib.dates.date2num(ld)
    y=data[data.id==capteur][v]
    matplotlib.pyplot.plot_date(x,y)
    plt.show()

# x=matplotlib.dates.date2num(ld)
# y=data[data.id==2].lum
# matplotlib.pyplot.plot_date(x,y)
# plt.show()