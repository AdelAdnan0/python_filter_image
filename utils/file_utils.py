import os
import cv2

def save_filtered_image(image, filter_type, kernel_size, image_path, unique_id, output_original):
    """Save the filtered image with a unique filename."""
    file_name = os.path.splitext(os.path.basename(image_path))[0]
    save_dir = f"OUTPUT/{unique_id}_{file_name}"

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    image_name = f"{unique_id}_{file_name}_[{filter_type}{kernel_size}x{kernel_size}_filter].jpg"

    if output_original:
        original_image_name = f"{unique_id}_{file_name}_[ORIGINAL].jpg"
        original_image_path = os.path.join(save_dir, original_image_name)
        original_image = cv2.imread(image_path)
        cv2.imwrite(original_image_path, original_image)
        print(f"Original image saved: {original_image_path}")

    image_path = os.path.join(save_dir, image_name)
    cv2.imwrite(image_path, image)
    print(f"Filtered image saved: {image_path}")
