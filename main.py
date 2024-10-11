import cv2
import argparse
from filters.image_processing import apply_action_for_color_img, apply_filter, apply_all_filters
from filters.filter_functions import mean, median
from utils.file_utils import save_filtered_image
from utils.time_utils import unique_id

def main():
    """Main function to handle command-line arguments and apply filters."""
    parser = argparse.ArgumentParser(description="Apply mean or median filter to an image.")

    # Optional filter and kernel size (ignored if --all is provided)
    parser.add_argument("-f", "--filter", choices=["mean", "median"], help="Type of filter to apply: 'mean' or 'median'")
    parser.add_argument("-k", "--kernel", type=int, choices=[3, 5, 9, 15], help="Kernel size for the filter (3, 5, 9, 15)")

    # Required image path argument
    parser.add_argument("-i", "--image", type=str, required=True, help="Path to the input image")

    # Add --all flag to apply all filters
    parser.add_argument("-a", "--all", action="store_true", help="Apply all filters and kernel sizes")

    args = parser.parse_args()

    image = cv2.imread(args.image)
    if image is None:
        print("Error: Unable to load image.")
        return

    if args.all:
        apply_all_filters(args.image)
    else:
        if not args.filter or not args.kernel:
            print("Error: You must specify both --filter and --kernel unless --all is used.")
            return

        filter_choice = args.filter
        kernel_size_choice = args.kernel
        print(f"Applying {filter_choice} filter with kernel size {kernel_size_choice}x{kernel_size_choice} to image {args.image}")

        filter_func = mean if filter_choice == "mean" else median
        filtered_image = apply_action_for_color_img(image, apply_filter, filter_func, kernel_size_choice)

        unique_image_id = unique_id()
        save_filtered_image(filtered_image, filter_choice, kernel_size_choice, args.image, unique_image_id, True)

if __name__ == "__main__":
    main()
