import matplotlib.pyplot as plt
x=[1, 2, 3, 4, 5]
y=[10, 20, 25, 30, 35]
plt.plot(x, y,linestyle="--",marker="D")
plt.xlabel('X-telg')
plt.ylabel('Y-telg')
plt.title('LIhtne graafik')
plt.show()

plt.scatter(x, y, color='lightblue')
plt.show()