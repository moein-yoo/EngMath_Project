def adaptiveFilter(image, kernel_size, learning_rate, epochs, filter_method):
    h, w = image.shape
    pad_w = kernel_size // 2
    padded_image = np.pad(image, ((pad_w, pad_w), (pad_w, pad_w)), mode='reflect')
    padded_image = padded_image.astype(np.float32)
    epsilon = 1e-6
    for i in range(epochs):
        local_mean = cv2.GaussianBlur(padded_image, (kernel_size, kernel_size), 0.9)
        local_var = cv2.GaussianBlur(padded_image**2, (kernel_size, kernel_size), 0.9) - local_mean**2
        if (filter_method == 'Gaussian'):
            local_mean = cv2.GaussianBlur(padded_image, (kernel_size, kernel_size), 0.8)
            local_var = cv2.GaussianBlur(padded_image**2, (kernel_size, kernel_size), 0.8) - local_mean**2
        else:
#            local_mean = bilateralFilter(padded_image, 1, 45, kernel_size)
#           local_var = bilateralFilter(padded_image**2, 1, 45, kernel_size) - local_mean**2

            # Normalize the image to [0, 1] if necessary (for better processing with float images)
            local_mean = cv2.bilateralFilter(padded_image, kernel_size, 10, 10)
            local_var = cv2.bilateralFilter(padded_image**2, kernel_size, 10, 10) - local_mean**2
        noise_var = np.mean(local_var)  
        wien_coef = local_var / (local_var + noise_var + epsilon)
        estimate = local_mean + wien_coef * (padded_image - local_mean)
        padded_image = padded_image + learning_rate * (estimate - padded_image)

    filteredImage = padded_image[pad_w:h+pad_w, pad_w:w+pad_w]
    filteredImage = np.clip(filteredImage, 0, 255)
    return np.uint8(np.clip(filteredImage, 0, 255))

brain_img = cv2.imread('pics/noisy_image_50.jpg', cv2.IMREAD_GRAYSCALE)
brain_img_original = cv2.imread('pics/original_2.jpg', cv2.IMREAD_GRAYSCALE)
filtered_brain_image = adaptiveFilter(brain_img, kernel_size=5, learning_rate=0.09, epochs=80, filter_method='Gaussian')
spine_img = cv2.imread('pics/noisy_spine.jpg', cv2.IMREAD_GRAYSCALE)
spine_img_original = cv2.imread('pics/spine_MRI_image.jpg', cv2.IMREAD_GRAYSCALE)
filtered_spine_image = adaptiveFilter(spine_img, kernel_size=3, learning_rate=0.01, epochs=80, filter_method='Bilateral')


plt.figure(figsize=(10, 6))

plt.subplot(2, 3, 1)
plt.imshow(brain_img, cmap='gray')
plt.title('Noisy Brain MRI')
plt.axis('off')

plt.subplot(2, 3, 2)
plt.imshow(filtered_brain_image, cmap='gray')
plt.title('Filtered Brain MRI')
plt.axis('off')

plt.subplot(2, 3, 3)
plt.imshow(brain_img_original, cmap='gray')
plt.title('Original Brain MRI')
plt.axis('off')

plt.subplot(2, 3, 4)
plt.imshow(spine_img, cmap='gray')
plt.title('Noisy Spine MRI')
plt.axis('off')

plt.subplot(2, 3, 5)
plt.imshow(filtered_spine_image, cmap='gray')
plt.title('Filtered Spine MRI')
plt.axis('off')

plt.subplot(2, 3, 6)
plt.imshow(spine_img_original, cmap='gray')
plt.title('Original Spine MRI')
plt.axis('off')

plt.tight_layout()
plt.show()
