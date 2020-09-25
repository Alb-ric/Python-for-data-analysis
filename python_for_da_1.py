import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#ce dataset provient de data.gouv et décrit les activités économiques des communes. Il y a 101 colonnes dans le fichier d'origine, j'en ai selectionné 4.
df = pd.read_excel(r"C:\Users\ALBERIC\Downloads\MDB-INSEE-V2.xls",usecols=["Population","Nb Pharmacies et parfumerie","Evolution Pop %","Environnement Démographique"])

print("5 premières lignes du dataset:")
print(df.head())
print(df.columns)


print("colonnes du dataset:")
for i in df.columns:
    print(i)
    
#classement du dataset par ordre de population décroissante.
df_sorted = df.sort_values(by=["Population"],ascending=False)

print(df_sorted.head())

print(df_sorted.iloc[:10,1])

print("nombre de pharmacies et parfumeries dans les 10 communes les plus peuplées:")
print(df_sorted.iloc[:10,0])

total = 0
index =0
for i in df["Evolution Pop %"]:
    total+=i
    index +=1

moy = total/index
print(index)
print("moyenne de l'évolution de la population en pourcentage")
print(moy)


print("nombre de communes pour chaque type d'environnement")
environnements = {}
for i in df["Environnement Démographique"]:
    if i in environnements.keys():
        environnements[i] += 1
    else:
        environnements[i] = 0

print(environnements)


print("courbe du nombre de pharmacies et parfumeries dans les communes classées par ordre de population décroissante:")
df_sorted.plot(x="Population",y="Nb Pharmacies et parfumerie",title="nombre de pharmacies et parfumeries en fonction de la population (échelle 10e6)")
plt.show()

print("graphique à barres du nombre de communes pour chaque type d'environnement: ")
plt.bar(environnements.keys(), environnements.values(), color='g')
plt.show()
