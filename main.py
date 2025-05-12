import cv2
from google.colab.patches import cv2_imshow
from google.colab import files
import numpy as np
from matplotlib import pyplot as plt

# Upload an image
uploaded = files.upload()

# Load the uploaded image from the buffer
file_name = next(iter(uploaded))
image = cv2.imdecode(np.frombuffer(uploaded[file_name], np.uint8), cv2.IMREAD_GRAYSCALE)

# Function to preprocess the image
def preprocess_image(image):
    """Apply preprocessing steps like noise reduction and normalization."""
    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(image, (5, 5), 0)
    # Normalize the image for better contrast
    normalized = cv2.normalize(blurred, None, 0, 255, cv2.NORM_MINMAX)
    return normalized

# Function for edge detection
def edge_detection(image):
    """Detect edges using the Canny edge detector."""
    edges = cv2.Canny(image, 50, 150)
    return edges

# Function for image segmentation
def segment_image(image):
    """Segment the image using thresholding."""
    _, thresholded = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)
    return thresholded

# Function to display multiple images
def display_images(images, titles):
    """Display multiple images with titles."""
    plt.figure(figsize=(12, 6))
    for i in range(len(images)):
        plt.subplot(1, len(images), i + 1)
        plt.imshow(images[i], cmap='gray')
        plt.title(titles[i])
        plt.axis('off')
    plt.show()

# Main processing
preprocessed_image = preprocess_image(image)
edges = edge_detection(preprocessed_image)
segmented_image = segment_image(preprocessed_image)

# Display results
display_images(
    [image, preprocessed_image, edges, segmented_image],
    ["Original Image", "Preprocessed Image", "Edges", "Segmented Image"]
)
