def bilateralFilter(image, sigma_d, sigma_r, kernel_size):
    h, w = image.shape
    pad_w = kernel_size // 2
    padded_image = np.pad(image, ((pad_w, pad_w), (pad_w, pad_w)), mode='constant', constant_values=0)
    filteredImage = np.zeros((h, w))
    # Gaussian Kernel
    gaussian_kernel = np.zeros((kernel_size, kernel_size))
    for i in range(kernel_size):
        for j in range(kernel_size):
            x = i - pad_w
            y = j - pad_w
            gaussian_kernel[i, j] = np.exp(-(x**2 + y**2) / (2 * sigma_d ** 2))
    gaussian_kernel /= np.sum(gaussian_kernel)
    for i in range(h):
        for j in range(w):
            wsb = 0
            filtered_value = 0
            for ii in range(kernel_size):
                for jj in range(kernel_size):
                    spatial_weight = gaussian_kernel[ii, jj]
                    intensity_diff = padded_image[i + ii, j + jj] - padded_image[i + pad_w, j + pad_w]
                    intensity_weight = np.exp(-0.5 * (intensity_diff / sigma_r)**2)
                    weight = spatial_weight * intensity_weight
                    filtered_value += padded_image[i + ii, j + jj] * weight
                    wsb += weight
            if wsb != 0:
                filteredImage[i, j] = filtered_value / wsb
            else:
                filteredImage[i, j] = padded_image[i + pad_w, j + pad_w] 

    return filteredImage
