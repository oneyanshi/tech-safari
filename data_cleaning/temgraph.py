import matplotlib as mpl

import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('envdata313.csv', delimiter=',', dtype=None, skip_header=5, names=('time', 'Tempature', 'Barometric_Pressure','Humidity','Gas','Altitude'))


plt.title("DATA313")
plt.xlabel("time")
plt.ylabel('temperature')
# plt.bar(data['time']/10000.0, data['Tempature'], color="blue")
plt.ylim(15,30)
plt.plot(data['Tempature'])
plt.show()
