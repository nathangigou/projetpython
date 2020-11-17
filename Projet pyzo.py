import pandas as pd
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import datetime

data = pd.read_csv("/Users/carll/Documents/EIVP/IVP1/Python/Projet/EIVP_KM.csv",delimiter=";")


def Converttime(n):
     L=len(data[data.id==n].sent_at)
     # Nb de mesures prises par le capteur n
     l=[]
     # Création de la liste des dates
     for i in range(L):
         l.append(datetime.datetime.strptime(data.sent_at.loc[data[data.id==n].index[i]], "%Y-%m-%d %H:%M:%S%z"))
         # Ajout à la liste la chaine de caractère sent_at convertie en un objet datetime
     return l

def courbes(v,capteur):
    ld=Converttime(capteur)
    x=matplotlib.dates.date2num(ld)
    y=data[data.id==capteur][v]
    matplotlib.pyplot.plot_date(x,y,linestyle='solid', markersize=0)
    plt.xticks(rotation='vertical')
    plt.xlabel("temps")
    plt.ylabel(v)
    plt.title(v+" en fonction du temps")
    plt.show()

# x=matplotlib.dates.date2num(ld)
# y=data[data.id==2].lum
# matplotlib.pyplot.plot_date(x,y)
# plt.show()
# plt.title("")
# plt.xlabel("")
# plt.ylabel("")
# plt.legend()
# plt.xticks("")

def max(v,capteur):
    if capteur==0:
        L=data[v]
        maxi=L[0]
        for i in range(1,len(L)):
            if L[i]>=maxi:
                maxi=L[i]
        return maxi
    else:
        L=data[data.id==capteur][v]
        lr=data[data.id==capteur].index[0]
        maxi=L[0+lr]
        for i in range(1+lr,len(L)+lr):
            if L[i]>=maxi:
                maxi=L[i]
        return maxi

def min(v,capteur):
    if capteur==0:
        L=data[v]
        mini=L[0]
        for i in range(1,len(L)):
            if L[i]<=mini:
                mini=L[i]
        return mini
    else:
        L=data[data.id==capteur][v]
        lr=data[data.id==capteur].index[0]
        mini=L[0+lr]
        for i in range(1+lr,len(L)+lr):
            if L[i]<=mini:
                mini=L[i]
        return mini


def moyenne(v,capteur):
    if capteur==0:
        s=0
        M=data[v]
        for i in range(len(M)):
            s+=M[i]
        return s/(len(M))
    else:
        s=0
        M=data[data.id==capteur][v]
        lr=data[data.id==capteur].index[0]
        for i in range(len(M)):
            s+=M[i+lr]
        return s/(len(M))


def variance(v,capteur):
    if capteur==0:
        L=data[data.id==capteur][v]
        a=0
        moy=moyenne(v,capteur)
        if len(L)==0 or len(L)==1:
            return 0
        else:
            for i in range(1,len(L)):
                a+=(L[i]-moy)**2
            return a/len(L)
    else:
        L=data[data.id==capteur][v]
        lr=data[data.id==capteur].index[0]
        a=0
        moy=moyenne(v,capteur)
        if len(L)==0 or len(L)==1:
            return 0
        else:
            for i in range(1,len(L)):
                a+=(L[i+lr]-moy)**2
            return a/len(L)

def ecart_type(v,capteur):
    return (variance(v,capteur))**(0.5)

# def quicksort(t):
#     if t == []:
#         return []
#     else:
#         pivot = t[0]
#     t1 = []
#     t2 = []
#     for x in t[1:]:
#         if x<pivot:
#            t1.append(x)
#         else:
#            t2.append(x)
#     return quicksort(t1)+[pivot]+quicksort(t2)

def mediane(v,capteur):
    sdata=data.sort_values(v)
    if capteur==0:
        y=data[v].loc[int(np.around((len(sdata[v])+1)/2,0))]
        return y
    else:
        y=data[v].loc[int(np.around((len(sdata[sdata.id==capteur][v])+1)/2,0))]
        return y

def caracteristiques(v,capteur):
    print ("max="+str(max(v,capteur)))
    print ('min='+str(min(v,capteur)))
    print ('moyenne='+str(moyenne(v,capteur)))
    print ('variance='+str(variance(v,capteur)))
    print ('écart-type='+str(ecart_type(v,capteur)))
    print ('médiane='+str(mediane(v,capteur)))
    plt.axhline(moyenne(v,capteur),color='red')
    plt.axhline(mediane(v,capteur), color='pink')
    for i in range(len(data[data[v]==max(v,capteur)][data.id==capteur].index)):
        matplotlib.pyplot.plot_date(matplotlib.dates.date2num(datetime.datetime.strptime(data.sent_at.loc[data[data[v]==max(v,capteur)][data.id==capteur].index[i]],"%Y-%m-%d %H:%M:%S%z")),max(v,capteur),color='brown')
    for i in range(len(data[data[v]==min(v,capteur)][data.id==capteur].index)):
        matplotlib.pyplot.plot_date(matplotlib.dates.date2num(datetime.datetime.strptime(data.sent_at.loc[data[data[v]==min(v,capteur)][data.id==capteur].index[i]],"%Y-%m-%d %H:%M:%S%z")),min(v,capteur),color='grey')
    plt.show()

# for row in data:
#     print(row)
# # row correspond aux colonnes qui composent le fichier (data)

# for index,row in data.iterrows():
#     print (row['temp'])
