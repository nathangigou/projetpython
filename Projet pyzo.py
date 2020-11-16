import pandas as pd
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import datetime

data = pd.read_csv("/Users/natha/Documents/EIVP/Algorithmique/Projet python/projetpython/EIVP_KM.csv",delimiter=";")


def Converttime(n):
     L=len(data[data.id==n].sent_at)
     # Nb de mesures prises par le capteur n
     l=[]
     # Création de la liste des dates
     for i in range(L):
         l.append(datetime.datetime.strptime(data.sent_at.loc[i+data[data.id==n].index[0]], "%Y-%m-%d %H:%M:%S %z"))
         # Ajout à la liste la chaine de caractère sent_at convertie en un objet datetime
     return l

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
 
def convertisseur(CSV):

    #On veut une matrice à 3 variables (6( pour capteurs) listes (parametres) de listes(donnees des relevés au cours du temps)) 
    #sous la forme:
    #[donnees n][du parametre m][du capteur o]

    Matrice = []
    Capteur[o] = []
    Parametre[m] = []
    Temps[n] = []
     
    m=[1,2,3,4,5] #numéro des paramètres noise, temp, hum,lum,co2
    n= []         #tableau des nombres de relevés malheureusement inégaux
    
    len(n[1])=1337
    len(n[2])=1346
    len(n[3])=1345
    len(n[4])=1344
    len(n[5])=1165
    len(n[6])=1344
    
    o=[1,2,3,4,5,6]  #numéro capteur
    
    for (n in range(1337)):       #pour chaque valeur de relevé du capteur 1
        for(m in range(5))        # pour chaque paramètre
        CSV.append(Matrice[m][n][1])  # la matrice du capteur 1 prend la valeur m-ième(param),n-ième(relevé) du CSV
    
    for(n from 1338 to 2783):
        for(m in range(5))
        CSV.append(Matrice[m][n][2])  # la matrice du capteur 2 prend la valeur m-ième(param),n-ième(relevé) du CSV
    
    #... logique identique
    
    return Matrice

    # apres on peut facilement a partir de liste trouver les min,max etc

