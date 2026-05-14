import numpy as np
import matplotlib.pyplot as plt


t = np.linspace(0,1,1000)

A = 2*np.cos(2*np.pi*10*t+np.pi/4)
B = 0.5*np.sin(2*np.pi*5*t+np.pi/4)

plt.subplot(2,2,1)
plt.plot(t,A,'#FFC1CC')
plt.xlabel("time")
plt.ylabel("amplitude")

plt.subplot(2,2,2)
plt.plot(t,B,'y')
plt.xlabel("time")
plt.ylabel("amplitude")

plt.subplot(2,2,3)
plt.plot(t,(A+B),'black')
plt.xlabel("time")
plt.ylabel("amplitude")

plt.subplot(2,2,4)
plt.plot(t,(A*B),'b')
plt.xlabel("time")
plt.ylabel("amplitude")

plt.show()