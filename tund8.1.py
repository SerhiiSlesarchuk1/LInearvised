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
import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 6))
plt.title("Кит")


x = np.linspace(0, 9, 300)
y = 2/27 * x**2 - 3
plt.plot(x, y, color="red")


x = np.linspace(-10, 0, 300)
y = 0.04 * x**2 - 3
plt.plot(x, y, color="magenta")


x = np.linspace( -9, -3, 300)
y = 2/3 * (x + 6)**2 + 1
plt.plot(x, y, color="orange")


x = np.linspace(-3, 9, 300)
y = -1/12 * (x - 3)**2 + 6
plt.plot(x, y, color="blue")


x = np.linspace(5, 8.3, 300)
y = 1/9 * (x - 5)**2 + 2
plt.plot(x, y, color="purple")


x = np.linspace(5, 8.5, 300)
y = 1.5 - 1/8 * (x - 7)**2
plt.plot(x, y, color="cyan")


x = np.linspace(-13, -9, 300)
y = -0.75 * (x + 11)**2 + 6
plt.plot(x, y, color="brown")


x = np.linspace(-15, -13, 300)
y = -0.5 * (x + 13)**2 + 3
plt.plot(x, y, color="green")


x = np.linspace(-15, -10, 300)
y = np.ones_like(x)
plt.plot(x, y, color="gold")


x = np.linspace(3, 4, 300)
y = 3 * np.ones_like(x)
plt.plot(x, y, color="navy")

plt.grid(True)
plt.xlabel("x")
plt.ylabel("y")
plt.show()

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
