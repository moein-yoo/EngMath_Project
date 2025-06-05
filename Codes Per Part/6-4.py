results = []
results.append({
    'Image': 'Adaptive Filter',
    'Brain MRI (SNR)': calculate_snr(brain_img, filtered_brain_image),
    'Brain MRI (PSNR)': calculate_psnr(brain_img, filtered_brain_image),
})
results.append({
    'Image': 'Adaptive Filter',
    'Spine MRI (SNR)': calculate_snr(spine_img, filtered_spine_image),
    'Spine MRI (PSNR)': calculate_psnr(spine_img, filtered_spine_image),
})
df = pd.DataFrame(results)
print(df)

fig, axes = plt.subplots(2, 4, figsize=(15, 8))
plt.grid(False)


axes[0,0].imshow(brain_img_original, cmap='gray')
axes[0,0].set_title('Original')
axes[0,1].imshow(filtered_brain_image, cmap='gray')
axes[0,1].set_title('Adaptive')
axes[0,2].imshow(brain_img, cmap='gray')
axes[0,2].set_title('Noisy')
axes[1,0].imshow(spine_img_original, cmap='gray')
axes[1,0].set_title('Original')
axes[1,1].imshow(filtered_spine_image, cmap='gray')
axes[1,1].set_title('Adaptive')
axes[1,2].imshow(spine_img, cmap='gray')
axes[1,2].set_title('Noisy')

for ax in axes.flatten():
    ax.axis('off')

plt.axis('off')

plt.show()