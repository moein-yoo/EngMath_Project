def swapMP(channel1, channel2, method):
    dft1 = np.fft.fft2(channel1)
    dft2 = np.fft.fft2(channel2)
    if method == 1:
        dft_combined = np.abs(dft1) * np.exp(1j * np.angle(dft2))
    else:
        dft_combined = np.abs(dft2) * np.exp(1j * np.angle(dft1))
    channel_reconstructed = np.fft.ifft2(dft_combined)
    channel_reconstructed = np.abs(channel_reconstructed)
    channel_reconstructed = cv2.normalize(channel_reconstructed, None, 0, 255, cv2.NORM_MINMAX)
    return channel_reconstructed.astype(np.uint8)

def createImage(image1, image2, method):
    b1, g1, r1 = cv2.split(image1)
    b2, g2, r2 = cv2.split(image2)
    b_reconstructed = swapMP(b1, b2, method)
    g_reconstructed = swapMP(g1, g2, method)
    r_reconstructed = swapMP(r1, r2, method)
    return cv2.merge([b_reconstructed, g_reconstructed, r_reconstructed])

image1 = cv2.imread("pics/pic2.jpg")  
image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
image2 = cv2.imread("pics/pic3.jpg")
image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)
image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

image1_reconstructed = createImage(image1, image2, 1)
image2_reconstructed = createImage(image1, image2, 2)

plt.figure(figsize=(12, 12))
plt.subplot(1,4,1), plt.imshow(image1), plt.title('pic2')
plt.subplot(1, 4, 2), plt.imshow(image2), plt.title('pic3')
plt.subplot(1, 4, 3), plt.imshow(image1_reconstructed.astype(np.uint8)), plt.title('Mag=pic2, Phase=pic3')
plt.subplot(1, 4, 4), plt.imshow(image2_reconstructed.astype(np.uint8)), plt.title('Mag=pic3, Phase=pic2')

plt.tight_layout()
plt.show()
