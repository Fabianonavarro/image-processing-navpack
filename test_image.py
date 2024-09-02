from image_processing.utils.io import read_image, save_image
from image_processing.processing.transformation import resize_image, find_difference
from image_processing.processing.combination import transfer_histogram
import os

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
