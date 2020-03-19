import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
import pandas as pd
import xlrd
import numpy as np

y = [6, 9, 32, 33, 34, 37, 43, 50, 65, 65, 77, 85, 100,
     110, 114, 140, 170, 195]

mpl.rcParams['axes.spines.left'] = True
mpl.rcParams['axes.spines.right'] = False
mpl.rcParams['axes.spines.top'] = False
mpl.rcParams['axes.spines.bottom'] = True
plt.style.use('seaborn-white')
plt.rcParams['font.family'] = "MS Gothic"

fig, ax = plt.subplots()

x_date = np.arange(1, 19, 1)

plt.plot(x_date, y, linewidth=1.5)
plt.xlabel('')

plt.vlines(3, 32, 100, alpha=0.4, linestyles='dashed', hatch='o')
plt.text(1, 106, 'Compulsory screening of ALL\nthe international passengers\narriving in India.', fontsize=6.5)
plt.plot(2.98, 102, 'o', alpha=0.6, markersize=5, color='#660000')

plt.vlines(10, 65, 100, alpha=0.4, linestyles='dashed', hatch='o')
plt.text(7.48, 110, 'Compulsory quarantine for 14 day \nfor Indians arriving in India,\nvisas suspended to India.', fontsize=6.5)
plt.plot(9.98, 102, 'o', alpha=0.6, markersize=5, color='#660000')

plt.vlines(13, 100, 150, alpha=0.4, linestyles='dashed', hatch='o')
plt.text(11.08, 160, 'Govt. declared pandemic \nas notified disaster.\nTested 5900 samples.', fontsize=6.5)
plt.plot(12.98, 152, 'o', alpha=0.6, markersize=5, color='#660000')

plt.vlines(15, 114, 70, alpha=0.4, linestyles='dashed', hatch='o')
plt.text(11.08, 48, 'Countrywide lock-down of schools and colleges.\nSecond worst fall in Sensex history.\nIndia obtains pure sample of virus.', fontsize=6.5)
plt.plot(14.98, 68, 'o', alpha=0.6, markersize=5, color='#660000')

plt.vlines(17, 170, 150, alpha=0.4, linestyles='dashed', hatch='o')
plt.text(15.88, 113, 'Entry of travellers from\nthe European Union banned.\nCBSE and JEE main\nexams postponed', fontsize=6.45)
plt.plot(16.98, 148, 'o', alpha=0.6, markersize=5, color='#660000')

plt.vlines(18, 195, 205, alpha=0.4, linestyles='dashed', hatch='o')
plt.text(18.18, 208, 'PM Modi\naddress to\n the nation.', fontsize=6.45)
plt.plot(17.98, 208, 'o', alpha=0.6, markersize=5, color='#660000')

plt.text(0.5, 190, 'Total cases: 195\nTotal samples: 14175\n', fontsize=8.45, weight='bold')
plt.text(0.5, 185, 'Recovered: 20', fontsize=8.45, weight='bold', color='#2F7109')
plt.text(0.5, 177.5, 'Deaths: 4', fontsize=8.45, weight='bold', color='#970A0A')

ax.axes.xaxis.set_ticklabels(['Mar 1', 'Mar 4', 'Mar 7', 'Mar 10', 'Mar 13', 'Mar 16', 'Mar 19'])
ax.xaxis.set_major_locator(ticker.MultipleLocator(3))

plt.ylabel('COVID-19 Cases in India')

plt.title('Coronavirus Timeline (India)')
plt.savefig('corona.png', bbox_inches='tight')
plt.show()
