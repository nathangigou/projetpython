import pandas as pd
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import datetime
from datetime import timedelta

data = pd.read_csv("/Users/carll/Documents/EIVP/IVP1/Python/Projet/EIVP_KM.csv",delimiter=";")


def convertdatetime(n):
     L=len(data[data.id==n].sent_at)
     # Nb de mesures prises par le capteur n
     l=[]
     # Création de la liste des dates
     for i in range(L):
         l.append(datetime.datetime.strptime(data.sent_at.loc[data[data.id==n].index[i]], "%Y-%m-%d %H:%M:%S%z"))
         # Ajout à la liste la chaine de caractère sent_at convertie en un objet datetime
     return l

def courbes(v,capteur):
    ld=convertdatetime(capteur)
    x=matplotlib.dates.date2num(ld)
    y=data[data.id==capteur][v]
    matplotlib.pyplot.plot_date(x,y,linestyle='solid', markersize=0,label='capteur'+str(capteur))
    plt.xticks(rotation=45)
    plt.xlabel("temps")
    plt.ylabel(v)
    plt.title(v+" en fonction du temps")
    plt.legend()
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


def mediane(v,capteur):
    sdata=data.sort_values(v)
    if capteur==0:
        y=data[v].loc[int(np.around((len(sdata[v])+1)/2,0))]
        return y
    else:
        y=data[v].loc[int(np.around((len(sdata[sdata.id==capteur][v])+1)/2,0))]
        return y

def caracteristiques(v,capteur):
    M=max(v,capteur)
    m=min(v,capteur)
    mo=moyenne(v,capteur)
    me=mediane(v,capteur)
    va=variance(v,capteur)
    et=ecart_type(v,capteur)
    print ("max="+str(M))
    print ('min='+str(m))
    print ('moyenne='+str(mo))
    print ('variance='+str(va))
    print ('écart-type='+str(et))
    print ('médiane='+str(me))

    plt.axhline(moyenne(v,capteur),color='red',label='moyenne')
    plt.annotate('moyenne capteur'+str(capteur),xy=(datetime.datetime(2019, 8, 18, 13, 2, 36, tzinfo=datetime.timezone(datetime.timedelta(seconds=7200))),mo),xycoords='data',xytext=(datetime.datetime(2019, 8, 18, 13, 2, 36, tzinfo=datetime.timezone(datetime.timedelta(seconds=7200))),mo+0.01*mo),textcoords='data',color='red',fontsize=5)

    plt.axhline(mediane(v,capteur), color='pink',label='médiane')
    plt.annotate('médiane capteur'+str(capteur),xy=(datetime.datetime(2019, 8, 18, 13, 2, 36, tzinfo=datetime.timezone(datetime.timedelta(seconds=7200))),me),xycoords='data',xytext=(datetime.datetime(2019, 8, 18, 13, 2, 36, tzinfo=datetime.timezone(datetime.timedelta(seconds=7200))),me+0.01*me),textcoords='data', color='pink',fontsize=5)

    for i in range(len(data[data.id==capteur][data[v]==M].index)):
        matplotlib.pyplot.plot_date(matplotlib.dates.date2num(datetime.datetime.strptime(data.sent_at[data[data.id==capteur][data[v]==M].index[i]],"%Y-%m-%d %H:%M:%S%z")),M,color='brown')
    for i in range(len(data[data.id==capteur][data[v]==m].index)):
        matplotlib.pyplot.plot_date(matplotlib.dates.date2num(datetime.datetime.strptime(data.sent_at[data[data.id==capteur][data[v]==m].index[i]],"%Y-%m-%d %H:%M:%S%z")),m,color='grey')
    plt.show()

# for row in data:
#     print(row)
# # row correspond aux colonnes qui composent le fichier (data)

# for index,row in data.iterrows():
#     print (row['temp'])

def alpha(t,h):
    return ((17.27*t)/(237.7+t))+np.log(h)

def trosee(t,h):
    return (237.7*alpha(t,h))/(17.27-alpha(t,h))

def humidex(t,h):
    return t+0.5555*(6.11*np.exp(5417.7530*(1/273.16-1/(273.15+trosee(t,h))))-10)

def Lhumidex(capteur):
    if capteur==0:
        L=[]
        for i in range(len(data)):
            L.append(humidex(data.temp[i],data.humidity[i]))
        return L
    else :
        L=[]
        pr=data[data.id==capteur].index[0]
        for i in range(len(data[data.id==capteur])):
            L.append(humidex(data[data.id==capteur].temp[i+pr],data[data.id==capteur].humidity[i+pr]))
        return L

def ccorrelation(x,y,capteur):
    sx=ecart_type(x,capteur)
    sy=ecart_type(y,capteur)
    mx=moyenne(x,capteur)
    my=moyenne(y,capteur)
    if capteur==0:
        s=0
        for i in range(len(data)):
            s+=(data[x][i]-mx)*(data[y][i]-my)
        c=s/(len(data)*sx*sy)
        return c
    else :
        s=0
        pr=data[data.id==capteur].index[0]
        for i in range(len(data[data.id==capteur])):
            s+=(data[data.id==capteur][x][i+pr]-mx)*(data[data.id==capteur][y][i+pr]-my)
        c=s/(len(data[data.id==capteur])*sx*sy)
        return c

def correlation(x,y,capteur):
    comparcourbes(x,y,capteur)
    plt.suptitle('correlation='+str(ccorrelation(x,y,capteur)),x=0.5,y=0.9,fontsize=5)
    plt.show()

def comparcourbes(x,y,capteur):
    fig, ax1 = plt.subplots()
    ld=convertdatetime(capteur)
    x1=matplotlib.dates.date2num(ld)
    y1=data[data.id==capteur][x]
    matplotlib.pyplot.plot_date(x1,y1,linestyle='solid', markersize=0, color='red')
    ax1.tick_params(axis='x', rotation=45)
    ax1.set_xlabel("temps")
    ax1.set_ylabel(x, color='red')

    ax2=ax1.twinx()
    y2=data[data.id==capteur][y]
    matplotlib.pyplot.plot_date(x1,y2,linestyle='solid', markersize=0, color='orange')
    ax2.set_ylabel(y,color='orange')

    plt.title(x+' & '+y+" en fonction du temps")
    fig.tight_layout()
    plt.show()

def timeencommun(capteur1,capteur2):
    L1=convertdatetime(capteur1)
    L2=convertdatetime(capteur2)
    while (L1[0]+timedelta(minutes=8))<=L2[0]:
        L1.pop(0)
    while (L2[0]+timedelta(minutes=8))<=L1[0]:
        L2.pop(0)
    while (L1[-1]-timedelta(minutes=8))>=L2[-1]:
        L1.pop(-1)
    while (L2[-1]-timedelta(minutes=8))>=L1[-1]:
        L2.pop(-1)
    return L1,L2

def listtimesamelength(capteur1,capteur2):
    L1,L2=timeencommun(capteur1,capteur2)
    delta=timedelta(minutes=8)
    L1b,L2b=[],[]
    for el1 in L1:
            for el2 in L2:
                if (el2-delta)<=el1 and el1<=(el2+delta):
                    L1b.append(el1)
    for el2 in L2:
            for el1 in L1:
                if (el1-delta)<=el2 and el2<=(el1+delta):
                    L2b.append(el2)
    return L1b,L2b

def convertstring(L):
    Lb=[]
    for i in range(len(L)):
        Lb.append(datetime.datetime.strftime(L[i], "%Y-%m-%d %H:%M:%S%z"))
        Lb[-1]=Lb[-1][:-2]+':'+Lb[-1][-2:]
    return Lb


def similarites(v,capteur1,capteur2):
    L1i,L2i=listtimesamelength(capteur1,capteur2)
    L1=convertstring(L1i)
    L2=convertstring(L2i)
    moy1=moyenne(v,capteur1)
    moy2=moyenne(v,capteur2)
    ecart=0.05*((moy1+moy2)/2)
    for i in range(len(L1)):
        d=abs(data[v].loc[data[v][data.id==capteur1][data.sent_at==L1[i]].index[0]]-data[v].loc[data[v][data.id==capteur2][data.sent_at==L2[i]].index[0]])
        if d<=ecart:
            moy=(data[v].loc[data[v][data.id==capteur1][data.sent_at==L1[i]].index[0]]+data[v].loc[data[v][data.id==capteur2][data.sent_at==L2[i]].index[0]])/2
            matplotlib.pyplot.plot_date(matplotlib.dates.date2num(L1i[i]),moy,color='purple')
    courbes(v,capteur1)
    courbes(v,capteur2)
    plt.show()


import sys
if sys.argv[1]=='courbes':
    return print(courbes(sys.argv[2],sys.argv[3]))
if sys.argv[1]=='caracteristiques':
    return caracteristiques(sys.argv[2],sys.argv[3])
if sys.argv[1]=='Lhumidex':
    return Lhumidex(sys.argv[2])
if sys.argv[1]=='correlation':
    return correlation(sys.argv[2],sys.argv[3],sys.argv[4])
if sys.argv[1]=='similarites':
    return similarites(sys.argv[2],sys.argv[3],sys.argv[4])







#pour annoter les max et courbes
# plt.annotate('capteur1',xy=(datetime.datetime(2019, 8, 18, 13, 2, 36, tzinfo=datetime.timezone(datetime.timedelta(seconds=7200))),max('noise',1)),xycoords='data',xytext=(datetime.datetime(2019, 8, 18, 13, 2, 36, tzinfo=datetime.timezone(datetime.timedelta(seconds=7200))),max('noise',1)),textcoords='data')