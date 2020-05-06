
import pandas as pd
import xlrd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['axes.spines.left'] = False
mpl.rcParams['axes.spines.right'] = False
mpl.rcParams['axes.spines.top'] = False
mpl.rcParams['axes.spines.bottom'] = True
plt.rcParams['axes.facecolor'] = '#262626'
fig, ax = plt.subplots()


'''excel_file = 'Sensex.xlsx'
df = pd.read_excel(excel_file,header=0,usecols=['Close'])
values = df.values.tolist()
price = [item for sublist in values for item in sublist]
x = np.linspace(1, 9443, 9443)
ax.fill_between(x[2632:2991], price[2632:2991], facecolor='#0983AC', alpha=0.75)
ax.fill_between(x[3799:3828], price[3799:3828], facecolor='#0983AC', alpha=0.7)
ax.fill_between(x[6417:7159], price[6417:7159], facecolor='#0983AC', alpha=0.6)
ax.fill_between(x[8614:8651], price[8614:8651], facecolor='#0983AC', alpha=0.7)
ax.fill_between(x[9350:9443], price[9350:9443], facecolor='#0983AC', alpha=0.7)'''
x = [1,2,3,4,5]
y = [200,56,45,40,30]
ax.yaxis.grid(alpha=0.2,linestyle='--')
ax.axes.xaxis.set_ticklabels([])
ax.axes.yaxis.set_ticklabels([])
ax.yaxis.tick_right()
ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')
plt.bar(x,y,color='#0983AC',alpha=0.6)
plt.savefig('pandemic.png', bbox_inches='tight',dpi=300)
plt.show()
'''plt.plot(x, price, color='#F4F2FA',linewidth=0.5,
         antialiased=True,alpha=0.8)'''
