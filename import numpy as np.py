import numpy as np
liste = [1800, 1500, 2200, 3000, 2172, 5000, 1400, 1200, 1100, 1300]

revenu = np.array(liste)

haut_revenus = [revenu>=3000]

somme_month = revenu.sum()
somme = somme_month*12
moyenne = revenu.mean()

revenu[6] = 1600

print(revenu, somme, moyenne)