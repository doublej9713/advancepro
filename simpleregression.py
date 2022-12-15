import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

from scipy import stats

#nyc = pd.read_csv('ave_hi_nyc_jan_1895-2018.csv')
nyc = pd.read_csv('https://raw.githubusercontent.com/pdeitel/IntroToPython/master/examples/ch10/ave_hi_nyc_jan_1895-2018.csv')
nyc.Date = nyc.Date.floordiv(100)
nyc.colums = ['Date', 'Temperature', 'Anomaly']

linear_regression = stats.linregress(x=nyc.Date, y=nyc.Temperature)
axes = sns.regplot(x=nyc.Date, y=nyc.Temperature)
#sns.set_style('whitegrid')
axes.set_ylim(5,80)
plt.title('Simple Regression using Scripy by Zool')
#axes.set_xlim(2000,2022)
plt.show()
