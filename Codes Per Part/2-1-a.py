def filterOfChannel(channel, mask_type, cutoff):
    dft = np.fft.fft2(channel)
    dft_shift = np.fft.fftshift(dft)
    rows, cols = channel.shape
    crow, ccol = rows // 2, cols // 2 # center
    mask = np.ones((rows, cols), np.uint8) if mask_type == "HPF" else np.zeros((rows, cols), np.uint8)
    if mask_type == "LPF":
        mask[crow - cutoff:crow + cutoff, ccol - cutoff:ccol + cutoff] = 1
    else:
        mask[crow - cutoff:crow + cutoff, ccol - cutoff:ccol + cutoff] = 0 
    dft_shift *= mask
    dft_ishift = np.fft.ifftshift(dft_shift)
    filtered_channel = np.fft.ifft2(dft_ishift)
    filtered_channel = np.abs(filtered_channel)
    return filtered_channel

def lowPassFilter(image, cutoff):
    b, g, r = cv2.split(image)
    b_filtered = filterOfChannel(b, "LPF", cutoff)
    g_filtered = filterOfChannel(g, "LPF", cutoff)
    r_filtered = filterOfChannel(r, "LPF", cutoff)
    return cv2.merge([b_filtered, g_filtered, r_filtered])

def highPassFilter(image, cutoff):
    b, g, r = cv2.split(image)
    b_filtered = filterOfChannel(b, "HPF", cutoff)
    g_filtered = filterOfChannel(g, "HPF", cutoff)
    r_filtered = filterOfChannel(r, "HPF", cutoff)
    return cv2.merge([b_filtered, g_filtered, r_filtered])