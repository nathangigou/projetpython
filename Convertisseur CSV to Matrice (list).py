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

    for n in range 1337:       #pour chaque valeur de relevé du capteur 1
        for(m in range(5))        # pour chaque paramètre
        CSV.append(Matrice[m][n][1])  # la matrice du capteur 1 prend la valeur m-ième(param),n-ième(relevé) du CSV

    for n from 1338 to 2783:
        for m in range(5))
        CSV.append(Matrice[m][n][2])  # la matrice du capteur 2 prend la valeur m-ième(param),n-ième(relevé) du CSV

    #... logique identique

    return Matrice