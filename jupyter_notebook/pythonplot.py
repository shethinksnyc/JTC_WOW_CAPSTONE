import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('3CitiesCombo.csv')
year = ['2015', '2016', '2017', '2018', '2019']
dataset = df.groupby('city')

indx = np.arange(len(year))
amount_awarded = np.arange(0, 300000000, 50000000)
chicago = list(dataset.T['Chicago'])
miami = list(dataset.T['Miami'])
los_angeles = list(dataset.T['Los Angeles'])

bar_width = 0.35

fig, ax = plt.subplots()
chicagoBar = ax.bar(indx - bar_width/2, chicago, bar_width, label='Chicago')
miamiBar = ax.bar(indx + bar_width/2, miami, bar_width, label='Miami')
laBar = ax.bar(2 + indx + bar_width/2, los_angeles, bar_width, label='Los Angeles')

# inserting x axis label
ax.set_xticks(indx)
ax.set_xticklabels(year)

# inserting y axis label
ax.set_yticks(amount_awarded)
ax.set_yticklabels(amount_awarded)

# inserting legend
ax.legend()

def insert_data_labels(bars):
	for bar in bars:
		bar_height = bar.get_height()
		ax.annotate('{0:.0f}'.format(bar.get_height()),
			xy=(bar.get_x() + bar.get_width() / 2, bar_height),
			xytext=(0, 3),
			textcoords='offset points',
			ha='center',
			va='bottom'
		)

insert_data_labels(chicagoBar)
insert_data_labels(miamiBar)
insert_data_labels(laBar)

plt.show()