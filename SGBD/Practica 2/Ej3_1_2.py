#!/usr/bin/python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('properati-AR-2018-02-01-properties-sell.csv')

filtro_CABA = (data.ix[(data.state_name == 'Capital Federal'), ['rooms']])

ocurrenciasPorAmbiente = filtro_CABA.groupby('rooms').size()[0:8]

print (ocurrenciasPorAmbiente)

ocurrenciasPorAmbiente.plot.bar()

plt.show()


