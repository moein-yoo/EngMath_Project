a = 0.2
L = np.arange(0, 1000, 1)
means_normal = []
means_uniform = []
for l in L:
    N1 = noise(a, l, "Normal")
    N2 = noise(a, l, "Uniform")
    means_normal.append(np.mean(N1))
    means_uniform.append(np.mean(N2))
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1), plt.plot(L, means_normal, color='b'), plt.title('Normal Noise')
plt.subplot(1, 2, 2), plt.plot(L, means_uniform, color='r'), plt.title('Uniform Noise')
plt.grid(True)
plt.show()