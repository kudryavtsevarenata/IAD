import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(r"C:\Users\123\Desktop\3 курс\course\14.11\populations.txt")
year, hares, lynxes, carrot= data.T
populations = data[:,1:]
dataT = data.T

print("hares, lynxes, carrots")
print("mean:", dataT[1:,:].mean(axis=1))

print("std:", dataT[1:,:].std(axis=1))

max_years = np.argmax(populations, axis=0)
print("max year:", year[max_years])

max_species = np.argmax(populations,axis=1)
species = np.array(['hare', 'lynx', 'carrot'])
print("max species")
print(np.vstack((year, species[max_species])))

above = np.any(populations > 50000, axis=1)
print("population above 50000", year[above])

top2 = np.argsort(populations, axis=0)[:2]
print("Top 2 on less population")
print(year[top2])

haregrade = np.gradient(hares, 1.0)
print("difference(haregrade, lynxes)", np.corrcoef(haregrade, lynxes)[0,1])


plt.legend(('Hare', 'Lynx', 'Carrot'), loc=(1.05, 0.5))
plt.plot(year, hares, year, lynxes, year, carrot)

plt.savefig('plot.png')