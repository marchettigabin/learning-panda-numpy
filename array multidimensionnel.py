import numpy as np

hugo = [1800, 21, 0]
richard = [1500, 54, 2]
emilie = [2200, 28, 3]
pierre = [3000, 37, 1]
paul = [2172, 37, 2]
deborah = [5000, 32, 0]
yohann = [1400, 23, 0]
anne = [1200, 25, 1]
thibault = [1100, 19, 0]
emmanuel = [1300, 31, 2]

tableau = [hugo, richard, emilie, pierre, paul, deborah,
           yohann, anne, thibault, emmanuel]

data = np.array(tableau)
print(data)

print(data[4, :])

louise = [1900, 31, 1]

data2 = np.insert(data, 4, louise, axis=0)

revenus = data[:, 0]
print(revenus)