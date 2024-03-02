import cv2
import numpy as np

def extract_border(image_path, output_path):
    # Read the image
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Apply GaussianBlur to reduce noise and improve edge detection
    blurred = cv2.GaussianBlur(img, (5, 5), 0)

    # Use the Canny edge detector to find edges
    edges = cv2.Canny(blurred, 50, 150)

    # Invert the image to get white lines on a black background
    edges_inv = cv2.bitwise_not(edges)

    # Save the result
    cv2.imwrite(output_path, edges_inv)

if __name__ == "__main__":
    input_image_path = "OIG3.jpeg"
    output_image_path = "blank.jpeg"

    extract_border(input_image_path, output_image_path)
