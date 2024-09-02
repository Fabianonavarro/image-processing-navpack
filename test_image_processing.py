import numpy as np
from skimage.color import rgb2gray
from skimage.exposure import match_histograms
from skimage.metrics import structural_similarity
from skimage.transform import resize
from skimage.util import img_as_ubyte
from skimage.io import imread, imsave
import os

def read_image(path, is_gray=False):
    """
    Reads an image from the specified path.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"No such file: '{path}'")
        
    image = imread(path, as_gray=is_gray)
    if not is_gray and len(image.shape) == 2:
        from skimage.color import gray2rgb
        image = gray2rgb(image)
    return image

def resize_image(image, target_shape):
    """
    Resizes the image to the target shape.
    """
    return resize(image, target_shape, anti_aliasing=True)

def find_difference(image1, image2):
    """
    Computes the difference between two images.
    """
    gray_image1 = rgb2gray(image1)
    gray_image2 = rgb2gray(image2)
    
    # Normalize images to range [0, 1]
    gray_image1 = (gray_image1 - gray_image1.min()) / (gray_image1.max() - gray_image1.min())
    gray_image2 = (gray_image2 - gray_image2.min()) / (gray_image2.max() - gray_image2.min())
    
    # Compute structural similarity
    score, difference_image = structural_similarity(gray_image1, gray_image2, full=True, data_range=1)
    print("Similarity of the images:", score)
    
    # Convert difference_image to 8-bit format
    difference_image = img_as_ubyte(difference_image)
    
    return difference_image

def transfer_histogram(image1, image2):
    """
    Transfers the histogram from image1 to image2.
    """
    # Ensure both images are in 8-bit format
    image1 = img_as_ubyte(image1)
    image2 = img_as_ubyte(image2)
    return match_histograms(image2, image1, channel_axis=-1)

def save_image(image, path):
    """
    Saves the image to the specified path.
    """
    # Convert the image to 8-bit unsigned integer format
    image = img_as_ubyte(image)
    imsave(path, image)

def main():
    img_folder = 'image_processing/imgs'

    image1_path = os.path.join(img_folder, 'imagem1.jpg')
    image2_path = os.path.join(img_folder, 'imagem2.jpg')

    print(f"Lendo imagem 1 de: {image1_path}")
    print(f"Lendo imagem 2 de: {image2_path}")

    try:
        image1 = read_image(image1_path)
        image2 = read_image(image2_path)
    except FileNotFoundError as e:
        print(e)
        return

    print("Shape of image1:", image1.shape)
    print("Shape of image2:", image2.shape)

    height, width = image1.shape[:2]
    image2_resized = resize_image(image2, (height, width, image2.shape[2]))
    print("Resized shape of image2:", image2_resized.shape)

    difference_image = find_difference(image1, image2_resized)
    save_image(difference_image, os.path.join(img_folder, 'difference_image.jpg'))

    histogram_matched_image = transfer_histogram(image1, image2_resized)
    save_image(histogram_matched_image, os.path.join(img_folder, 'histogram_matched_image.jpg'))

if __name__ == "__main__":
    main()
