def calculate_psnr(noisy_img, filtered_img):
    mse = np.mean((noisy_img - filtered_img) ** 2)
    if mse == 0:
        return 100
    max_pixel = 255.0
    psnr = 10 * np.log10((max_pixel ** 2) / mse)
    return psnr

def calculate_snr(noisy_img, filtered_img):
    noise = noisy_img - filtered_img
    signal_power = energyCalculator(filtered_img)
    noise_power = energyCalculator(noise)
    snr = signal_power / noise_power
    return snr

brain_img = cv2.imread('pics/noisy_tumor.jpg', cv2.IMREAD_GRAYSCALE)
spine_img = cv2.imread('pics/noisy_spine.jpg', cv2.IMREAD_GRAYSCALE)
brain_img_original = cv2.imread('pics/tumor_original.jpg', cv2.IMREAD_GRAYSCALE)
spine_img_original = cv2.imread('pics/spine_MRI_image.jpg', cv2.IMREAD_GRAYSCALE)
# Apply Mean Filter
mean_filtered_brain = meanFilter(brain_img, 3)
mean_filtered_spine = meanFilter(spine_img, 3)
# Apply Gaussian Filter
gaussian_filtered_brain = gaussianFilter(brain_img, 1, 4)
gaussian_filtered_spine = gaussianFilter(spine_img, 2, 10)

# Apply Bilateral Filter
bilateral_filtered_brain = bilateralFilter(brain_img, 1, 100, 5)
bilateral_filtered_spine = bilateralFilter(spine_img, 1, 45, 5)

results = []
"""
# Noisy image comparison
results.append({
    'Image': 'Noisy Image',
    'Brain MRI (SNR)': calculate_snr(brain_img_original, brain_img),
    'Brain MRI (PSNR)': calculate_psnr(brain_img_original, brain_img),
    'Spine MRI (SNR)': calculate_snr(spine_img_original, spine_img),
    'Spine MRI (PSNR)': calculate_psnr(spine_img_original, spine_img),
})
"""
# Mean Filter
results.append({
    'Image': 'Mean Filter',
    'Brain MRI (SNR)': calculate_snr(brain_img, mean_filtered_brain),
    'Brain MRI (PSNR)': calculate_psnr(brain_img, mean_filtered_brain),
    'Spine MRI (SNR)': calculate_snr(spine_img, mean_filtered_spine),
    'Spine MRI (PSNR)': calculate_psnr(spine_img, mean_filtered_spine),
})

# Gaussian Filter
results.append({
    'Image': 'Gaussian Filter',
    'Brain MRI (SNR)': calculate_snr(brain_img, gaussian_filtered_brain),
    'Brain MRI (PSNR)': calculate_psnr(brain_img, gaussian_filtered_brain),
    'Spine MRI (SNR)': calculate_snr(spine_img, gaussian_filtered_spine),
    'Spine MRI (PSNR)': calculate_psnr(spine_img, gaussian_filtered_spine),
})

# Bilateral Filter
results.append({
    'Image': 'Bilateral Filter',
    'Brain MRI (SNR)': calculate_snr(brain_img, bilateral_filtered_brain),
    'Brain MRI (PSNR)': calculate_psnr(brain_img, bilateral_filtered_brain),
    'Spine MRI (SNR)': calculate_snr(spine_img, bilateral_filtered_spine),
    'Spine MRI (PSNR)': calculate_psnr(spine_img, bilateral_filtered_spine),
})

df = pd.DataFrame(results)
print(df)

fig, axes = plt.subplots(2, 5, figsize=(15, 8))
plt.grid(False)


axes[0, 0].imshow(brain_img, cmap='gray')
axes[0, 0].set_title('Noisy Brain MRI')
axes[0, 1].imshow(mean_filtered_brain, cmap='gray')
axes[0, 1].set_title('Mean Filtered Brain MRI')
axes[0, 2].imshow(gaussian_filtered_brain, cmap='gray')
axes[0, 2].set_title('Gaussian Filtered Brain MRI')
axes[0, 3].imshow(bilateral_filtered_brain, cmap='gray')
axes[0, 3].set_title('Bilateral Filtered Brain MRI')
axes[0, 4].imshow(brain_img_original, cmap='gray')
axes[0, 4].set_title('Original Brain MRI')


axes[1, 0].imshow(spine_img, cmap='gray')
axes[1, 0].set_title('Noisy Spine MRI')
axes[1, 1].imshow(mean_filtered_spine, cmap='gray')
axes[1, 1].set_title('Mean Filtered Spine MRI')
axes[1, 2].imshow(gaussian_filtered_spine, cmap='gray')
axes[1, 2].set_title('Gaussian Filtered Spine MRI')
axes[1, 3].imshow(bilateral_filtered_spine, cmap='gray')
axes[1, 3].set_title('Bilateral Filtered Spine MRI')
axes[1, 4].imshow(spine_img_original, cmap='gray')
axes[1, 4].set_title('Original Spine MRI')
plt.axis('off')
for ax in axes.flatten():
    ax.axis('off')

plt.axis('off')

plt.show()
