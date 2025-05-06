import numpy as np
import matplotlib.pyplot as plt

#loeme andmed failist
with open('maed.txt', 'r') as f:
    lines = f.readlines()


nimed=[]
korgused=[]

for rida in lines:
    osad = rida.strip().split()
    nimi = osad[0]
    korgus = int(osad[1])
    nimed.append(nimi)
    korgused.append(korgus)

korgused_np = np.array(korgused)
keskmine = np.mean(korgused_np)
maksimum = np.max(korgused_np)
minimum = np.min(korgused_np)
summa = np.sum(korgused_np)

print("M�gede statistika:")
print(f"Keskmine k�rgus: {keskmine:.2f} m")
print(f"K�rgeim m�gi: {nimed[np.argmax(korgused_np)]} ({maksimum} m)")
print(f"Madalaim m�gi: {nimed[np.argmin(korgused_np)]} ({minimum} m)")
print(f"K�rguste summa: {summa} m")

plt.figure(figsize=(10,6))
plt.bar(nimed, korgused, color='skyblue')
plt.title('Maailma k�rgeimad m�ed')
plt.xlabel('M�gi')
plt.ylabel('K�rgus (m)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('maed_graafik.png')
plt.show()

nimed_sorted=[x for _, x in sorted(zip(korgused, nimed), reverse=True)]
korgused_sorted=sorted(korgused, reverse=True)

plt.figure(figsize=(10, 6))
plt.bar(nimed_sorted, korgused_sorted, color='orange')
plt.title('K�rgeimad m�ed (sorteeritud)')
plt.xlabel('M�gi')
plt.ylabel('K�rgus (m)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('maed_graafik_sorted.png')
plt.show()

