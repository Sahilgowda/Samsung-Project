from skimage.metrics import structural_similarity as ssim
import cv2

# Function Defined to Calculate the SSIM 
def calculate_ssim(image1, image2):
    # Check weather both image of same size :
    if image1.shape != image2.shape:
        #because the 2nd image dimension not similar so size of the First Image         
        image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))
    # Convert images to grayscale
    gray_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # Calculate SSIM inbuilt Function Which is generally available in the skimage.metrics package
    ssim_index = ssim(gray_image1, gray_image2)

    return ssim_index

# Load the two images
image1 = cv2.imread('image1.png')
image2 = cv2.imread('image2.png')

# Calculate SSIM
ssim_value = calculate_ssim(image1, image2)

print("SSIM value:",( ssim_value))
