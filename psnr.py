import cv2
import numpy as np

# Function to Calculate the PSNR Value :
def psnr(img1, img2):
    # Check and adjust image dimensions if needed
    if img1.shape != img2.shape:
        #because the 2nd image dimension not similar so size of the First Image         
        img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
    # Checking the Mean Squared Error -->Error between the Original Image and Distorted Image:
    mse = np.mean((img1 - img2) ** 2)
    # Verify Weather the both images have the same psnr value 
    if mse == 0:
        return float('inf')
    max_pixel = 255.0
    # The Psnr Formula is given as :
    psnr_value = 20 * np.log10(max_pixel / np.sqrt(mse))
    return psnr_value

# Load the images
image1 = cv2.imread('image1.PNG')
image2 = cv2.imread('image2.PNG')

# Convert images to grayscale if needed
image1_gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
image2_gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

# Calculate PSNR (Function Call)
psnr_value = psnr(image1_gray, image2_gray)
print("PSNR value is:", psnr_value)