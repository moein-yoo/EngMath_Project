print("The SNR of the signal with normal noise is: ", signal_energy / N1_energy)
print("The SNR of the signal with uniform noise is: ", signal_energy / N2_energy)
a = np.arange(0.05, 0.5, 0.01)
SNR_normal = []
SNR_uniform = []
for i in a:
    N1 = noise(i, len(t), "Normal")
    N2 = noise(i, len(t), "Uniform")
    signal_noised = signal + N1
    signal_energy = energyCalculator(signal)
    noise_energy1 = energyCalculator(N1)
    noise_energy2 = energyCalculator(N2)
    SNR_normal.append(signal_energy / noise_energy1)
    SNR_uniform.append(signal_energy / noise_energy2)
    
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1), plt.plot(a, SNR_normal, color='b'), plt.title('Normal Noise SNR'), plt.axhline(y=100, color='g', linestyle='--')
SNR_normal = np.array(SNR_normal)
index = np.argmin(np.abs(SNR_normal-100))
x_intercept2 = a[index]
plt.axvline(x=x_intercept2, color='g', linestyle='--')
plt.text(x_intercept2, 100, f'a={x_intercept2:.2f}', color='g', verticalalignment='bottom')
plt.subplot(1, 2, 2), plt.plot(a, SNR_uniform, color='r'), plt.title('Uniform Noise SNR'), plt.axhline(y=100, color='g', linestyle='--')
SNR_uniform = np.array(SNR_uniform)
index = np.argmin(np.abs(SNR_uniform-100))
x_intercept1 = a[index]
plt.axvline(x=x_intercept1, color='g', linestyle='--')
plt.text(x_intercept1, 100, f'a={x_intercept1:.2f}', color='g', verticalalignment='bottom')
plt.grid(True)
plt.show()