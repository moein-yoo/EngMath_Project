a = 0.2
L = np.arange(0, 1000, 1)
energy_normal = []
energy_uniform = []
for l in L:
    N1 = noise(a, l, "Normal")
    N2 = noise(a, l, "Uniform")
    energy_normal.append(np.sum(N1 ** 2) / l)
    energy_uniform.append(np.sum(N2 ** 2) / l)
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1), plt.plot(L, energy_normal, color='b'), plt.title('Normal Noise')
plt.subplot(1, 2, 2), plt.plot(L, energy_uniform, color='r'), plt.title('Uniform Noise')
plt.grid(True)
plt.show()