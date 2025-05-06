# import matplotlib.pyplot as plt
# x=[1, 2, 3, 4, 5]
# y=[10, 20, 25, 30, 35]
# plt.plot(x, y,linestyle="--",marker="D")
# plt.xlabel('X-telg')
# plt.ylabel('Y-telg')
# plt.title('LIhtne graafik')
# plt.show()

# plt.scatter(x, y, color='lightblue')
# plt.show()

#ÜL1 prilid
import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(-9, -1, 400)
x2 = np.linspace(1, 9, 400)
x3 = np.linspace(-9, -1, 400)
x4 = np.linspace(1, 9, 400)
x5 = np.linspace(-9, -6, 200)
x6 = np.linspace(6, 9, 200)
x7 = np.linspace(-1, 1, 200)

plt.plot(x1, -(1/16)*(x1 + 5)**2 + 2, color='blue')
plt.plot(x2, -(1/16)*(x2 - 5)**2 + 2, color='orange')
plt.plot(x3, (1/4)*(x3 + 5)**2 - 3, color='green')
plt.plot(x4, (1/4)*(x4 - 5)**2 - 3, color='red')
plt.plot(x5, -(x5 + 7)**2 + 5, color='purple')
plt.plot(x6, -(x6 - 7)**2 + 5, color='brown')
plt.plot(x7, -0.5*x7**2 + 1.5, color='magenta')

plt.title("Prilid")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

plt.show()
