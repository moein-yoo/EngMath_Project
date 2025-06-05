def gaussianFilter(image, variance, kernel_size):
    h,w = image.shape
    pad_w = kernel_size // 2
    padded_image = np.pad(image, ((pad_w, pad_w), (pad_w, pad_w)), mode='constant', constant_values=0)
    filteredImage = np.zeros((h, w))
    #Gaussian Kernel
    gaussian_kernel = np.zeros((kernel_size, kernel_size))
    for i in range(kernel_size):
        for j in range(kernel_size):
            x = i - pad_w
            y = j - pad_w
            gaussian_kernel[i, j] = np.exp(-(x**2 + y**2) / (2 * variance ** 2))
    gaussian_kernel /= np.sum(gaussian_kernel)
    for i in range(h):
        for j in range(w):
            kernel = padded_image[i:i + kernel_size, j:j + kernel_size]
            filteredImage[i, j] = np.sum(kernel * gaussian_kernel)
    return filteredImage

