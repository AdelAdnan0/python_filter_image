import cv2
import numpy as np
from .filter_functions import mean, median
from utils.file_utils import save_filtered_image
from utils.time_utils import unique_id

def apply_action_for_color_img(image, action_func, filter_func, kernel_size):
    """Apply a filter to each color channel of an image."""
    b_channel, g_channel, r_channel = cv2.split(image)

    b_filtered = action_func(b_channel, filter_func, kernel_size)
    g_filtered = action_func(g_channel, filter_func, kernel_size)
    r_filtered = action_func(r_channel, filter_func, kernel_size)

    return cv2.merge([b_filtered, g_filtered, r_filtered])

def apply_filter(img, filter_func, kernel_size):
    """Apply the specified filter to the image."""
    h, w = img.shape
    pad = kernel_size // 2
    padded_img = cv2.copyMakeBorder(img, pad, pad, pad, pad, cv2.BORDER_REFLECT)
    filtered_img = np.zeros((h, w), dtype=np.uint8)

    for i in range(h):
        for j in range(w):
            window = padded_img[i : i + kernel_size, j : j + kernel_size]
            value = filter_func(window)
            filtered_img[i, j] = value

    return filtered_img

def apply_all_filters(image_path):
    """Apply all filters (mean, median) with all kernel sizes (3, 5, 9, 15)."""
    filters = [mean, median]
    filter_names = ["mean", "median"]
    kernel_sizes = [3, 5, 9, 15]

    output_original = True
    unique_image_id = unique_id()

    image = cv2.imread(image_path)
    if image is None:
        print("Error: Unable to load image.")
        return

    for idx, filter_func in enumerate(filters):
        filter_type = filter_names[idx]
        for kernel_size in kernel_sizes:
            print(f"Applying {filter_type} filter with kernel size {kernel_size}x{kernel_size}")

            filtered_image = apply_action_for_color_img(image, apply_filter, filter_func, kernel_size)
            save_filtered_image(filtered_image, filter_type, kernel_size, image_path, unique_image_id, output_original)
            output_original = False
