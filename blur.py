import cv2

def calculate_blurriness(image_path):
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur_score = cv2.Laplacian(gray_image, cv2.CV_64F).var()
    image_size = image.shape[0] * image.shape[1]
    blurriness_percentage = (1 - (blur_score / image_size)) * 100
    return blurriness_percentage

# Input image path from the user
image_path = input("Enter the path to the image: ")

# Calculate blurriness percentage
blurriness = calculate_blurriness(image_path)

print(f"The image is {blurriness:.2f}% blurry.")
