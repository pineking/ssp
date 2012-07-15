#!/usr/bin/env python2
#
# Copyright 2012 by Idiap Research Institute, http://www.idiap.ch
#
# See the file COPYING for the licence associated with this software.
#
# Author(s):
#   Phil Garner, July 2012
#
from ssp import *

fig = Figure(2,1)
ax1 = fig.subplot()
ax2 = fig.subplot()

F0 = 150
period = 16000/F0
x = np.arange(period)
#for t in ('trig', 'poly', 'gamma', 'igamma', 'lf'):
for t in ('gamma', 'lf'):
    if t != 'lf':
        ax1.plot(x, pulse(period, t, derivative=False))
    ax2.plot(x, pulse(period, t))

ax1.set_xlim(0, period)
ax2.set_xlim(0, period)
plt.show()
