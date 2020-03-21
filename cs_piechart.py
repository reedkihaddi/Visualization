import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
import matplotlib.patches as mpatches

circle = mpatches.Circle((0.5, 0.5), 0.5, facecolor="#003f5c",
                    edgecolor="black", linewidth=1.25,label='A chutiya going AFK')
circle2 = mpatches.Circle((0.5, 0.5), 0.25, facecolor="#58508d",
                    edgecolor="black", linewidth=1.25,label='Bhai galti se buy krlia')
circle3 = mpatches.Circle((0.5, 0.5), 0.25, facecolor="#bc5090",
                    edgecolor="black", linewidth=1.25,label='Samne hacker hai')
circle4 = mpatches.Circle((0.5, 0.5), 0.25, facecolor="#ff6361",
                    edgecolor="black", linewidth=1.25,label='Mic ke sath sex')
circle5 = mpatches.Circle((0.5, 0.5), 0.25, facecolor="#ffa600",
                    edgecolor="black", linewidth=1.25,label='Constant Gaben abuse')
circle6 = mpatches.Circle((0.5, 0.5), 0.25, facecolor="#ff4000",
                    edgecolor="black", linewidth=1.25,label='Because I suck')




plt.rcParams['font.family'] = "Courier New"
sizes = [24, 24, 25, 12.5, 12.5, 2]

labels = ['A chutiya going AFK', 'Bhai galti se buy krlia', 'Samne hacker hai', 'Mic ke sath sex', 'Constant Gaben abuse', 'Because I suck']

explode = (0.05, 0.05, 0.05, 0.05, 0.05, 0.05)
#add colors
colors = ['#003f5c', '#58508d', '#bc5090', '#ff6361', '#ffa600', '#ff4000']
fig1, ax = plt.subplots()
ax.pie(sizes, explode=explode,  colors=colors,
        shadow=True, startangle=90)
# Equal aspect ratio ensures that pie is drawn as a circle
ax.axis('equal')
plt.title("WHY I DON'T RANK UP",fontsize=25,fontweight='bold',fontfamily='Courier New')
plt.legend(labels, loc='center right', fontsize=15, frameon=False,
           handles=[circle, circle2, circle3, circle4, circle5, circle6])

plt.show()
