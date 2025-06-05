def meanFilter(image, kernel_size):
    h,w = image.shape
    pad_w = kernel_size // 2
    padded_image = np.pad(image, ((pad_w, pad_w), (pad_w, pad_w)), mode='constant', constant_values=0)
    filteredImage = np.zeros((h, w))
    for i in range(h):
        for j in range(w):
            kernel = padded_image[i:i+kernel_size, j:j+kernel_size]
            filteredImage[i, j] = np.mean(kernel)
    return filteredImage
