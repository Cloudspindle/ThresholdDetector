""" peak detector with threshold """

import numpy as np
import matplotlib.dates as mdates
import pandas as pd
from datetime import datetime
import peakutils
from peakutils.plot import plot as pplot
from matplotlib import pyplot

headers = ['ts','x','y','z','m']
df = pd.read_csv('bammo_accel.csv',names=headers)

headers = ['ts','x','y','z','m']

df['ts'] = df['ts'].map(lambda x: datetime.strptime(str(x), '%Y-%m-%d %H:%M:%S.%f'))

x = df['ts']
y = df['m']
indexes = peakutils.indexes(y, thres=0.75, min_dist=30)
xpeak = str(x[indexes]).split()[1] + " " + str(x[indexes]).split()[2]
ypeak = str(y[indexes]).split()[1] 

pyplot.figure(figsize=(10,6))
pplot(x,y,indexes)
pyplot.title("Peak at " + xpeak + " " + ypeak + " Gs "+ "max=" + str(y.max()))
pyplot.show()