a = 0.2
L = np.arange(0, 1000, 1)
correlation = []
for l in L:
    N1 = noise(a, l, "Normal")
    N2 = noise(a, l, "Uniform")
    correlation.append(np.dot(N1, N2.T) / l)
plt.figure(figsize=(12, 5))
plt.plot(L, correlation, color='r'), plt.title('Correlation')
plt.grid(True)
plt.show()