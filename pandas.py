import pandas as pd

import matplotlib.pyplot as plt

titanic =pd.read_csv('https://vincentarelbundock.github.io/Rdataset/csv/carData/TitanicSurvival.csv')
pd.set_option('precision',2)

#Age Histogram

plt.hist(titanic.age)
plt.axvline(titanic.age.mean(),color='k',linestyle='dashed',linewidth=1)
plt.title('Ages of Passengers on Titanic')
plt.ylabel('Count')
plt.xlabel('Age(In Years)')
plt.show()

#histogram =titanic.hist('age')
