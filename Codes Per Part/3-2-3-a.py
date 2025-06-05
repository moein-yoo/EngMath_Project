sampling_frequency = 100
frequency = 1
pi = np.pi
t = np.arange(0, 2, 1 / sampling_frequency)
signal = np.sin(2 * pi * frequency * t)
N1 = noise(0.2, len(t), "Normal")
N2 = noise(0.2, len(t), "Uniform")
signal_noised1 = signal + N1
signal_noised2 = signal + N2
plt.figure(figsize=(12, 5))
plt.subplot(1, 3, 1), plt.plot(t, signal, color='b'), plt.title('Original Signal')
plt.subplot(1, 3, 2), plt.plot(t, signal_noised1, color='r'), plt.title('Noised Signal (Normal)')
plt.subplot(1, 3, 3), plt.plot(t, signal_noised2, color='g'), plt.title('Noised Signal (Uniform)')
plt.grid(True)
plt.show()