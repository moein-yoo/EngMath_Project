a = 0.2
L = 10000
N1 = noise(a, L, "Normal")
N2 = noise(a, L, "Uniform")
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1), plt.hist(N1, bins=100, density=True, color='b', alpha=0.7), plt.title('Normal Noise')
plt.subplot(1, 2, 2), plt.hist(N2, bins=100, density=True, color='r', alpha=0.7), plt.title('Uniform Noise')
plt.grid(True)
plt.show()