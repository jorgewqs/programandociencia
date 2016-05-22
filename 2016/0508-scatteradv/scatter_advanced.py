# importing necessary packages.
import matplotlib.lines as mlines
import matplotlib.pyplot as plt
import pandas as pd

# reading data_ibge.xls
data_brazil = pd.read_excel('data_ibge.xls', sheetname=2)

# color palette 5-class Dark2, from ColorBrewer2: http://colorbrewer2.org/
colors = ['#1b9e77',
          '#d95f02',
          '#7570b3',
          '#e7298a',
          '#66a61e']


# attribute_color() points to the color correspondent to each region.
def attribute_color(region):
    colors = {
        'North': '#1b9e77',
        'Northeast': '#d95f02',
        'Southeast': '#7570b3',
        'South': '#e7298a',
        'Central-West': '#66a61e'
    }
    return colors.get(region, 'black')

# creating the color vector.
color_region = list()
qty_states = len(data_brazil['Region'])

for state in range(qty_states):
    color_region.append(attribute_color(data_brazil['Region'][state]))

# generating the plot.
plt.scatter(x=data_brazil['LifeExpec'],
            y=data_brazil['GDPperCapita'],
            s=data_brazil['PopX1000'],
            c=color_region,
            alpha=0.6)

plt.title('Brazilian development in 2013, according to each state',
          fontsize=22)
plt.xlabel('Life expectancy (years)', fontsize=22)
plt.ylabel('GDP per capita (R$)', fontsize=22)
plt.grid(True)

# inserting state abbreviation into each circle.
for state in range(len(data_brazil['UF'])):
    plt.text(x=data_brazil['LifeExpec'][state],
             y=data_brazil['GDPperCapita'][state],
             s=data_brazil['UF'][state],
             fontsize=16)

# inserting legend; the "normal" legend does not work, so we adapt a
# 2D object with the colors we defined previously.
regions = ['North',
           'Northeast',
           'Southeast',
           'South',
           'Central-West']

# legend 1
legend1_line2d = list()
for step in range(len(colors)):
    legend1_line2d.append(mlines.Line2D([0], [0],
                                        linestyle='none',
                                        marker='o',
                                        alpha=0.6,
                                        markersize=15,
                                        markerfacecolor=colors[step]))

legend1 = plt.legend(legend1_line2d,
                     regions,
                     numpoints=1,
                     fontsize=22,
                     loc='best',
                     shadow=True)

# legend 2
legend2_line2d = list()
legend2_line2d.append(mlines.Line2D([0], [0],
                                    linestyle='none',
                                    marker='o',
                                    alpha=0.6,
                                    markersize=np.sqrt(100),
                                    markerfacecolor='#D3D3D3'))
legend2_line2d.append(mlines.Line2D([0], [0],
                                    linestyle='none',
                                    marker='o',
                                    alpha=0.6,
                                    markersize=np.sqrt(1000),
                                    markerfacecolor='#D3D3D3'))
legend2_line2d.append(mlines.Line2D([0], [0],
                                    linestyle='none',
                                    marker='o',
                                    alpha=0.6,
                                    markersize=np.sqrt(10000),
                                    markerfacecolor='#D3D3D3'))

legend2 = plt.legend(legend2_line2d,
                     ['1', '10', '100'],
                     title='Population (in 100,000)',
                     numpoints=1,
                     fontsize=20,
                     loc='upper left',
                     frameon=False,  # no edges
                     labelspacing=3,  # increase space between labels
                     handlelength=5,  # increase space between objects
                     borderpad=4)  # increase the margins of the legend
plt.gca().add_artist(legend1)

plt.setp(legend2.get_title(), fontsize=22)  # increasing the legend font
plt.show()
