import argparse
import cv2
import dlib
import numpy as np
import os

from pathlib import Path
from PIL import Image, ImageFile


class Rotator:
    IMAGES_DIRECTORY = "images"

    def __init__(self, overwrite_files: bool=False):
        self.detector = dlib.get_frontal_face_detector()
        self.overwrite_files =overwrite_files

    def analyze_images(self):
        for filename in os.listdir(self.IMAGES_DIRECTORY):
            if not filename.endswith(".jpeg"):
                continue

            image = self.open_image(filename)

            self.analyze_image(image, filename)

    def analyze_image(self, image: ImageFile, filename: str) -> bool:
        """Cycles through 4 image rotations of 90 degrees.
           Saves the image at the current rotation if faces are detected.
        """

        print(f"ANALYZING IMAGE: {filename}")

        for cycle in range(0, 4):
            if cycle > 0:
                # Rotate the image an additional 90 degrees for each non-zero cycle.
                image = image.rotate(90, expand=True)

            image_copy = np.asarray(image)
            image_gray = cv2.cvtColor(image_copy, cv2.COLOR_BGR2GRAY)

            faces = self.detector(image_gray, 0)
            if len(faces) == 0:
                continue

            if cycle > 0:
                print(f"ROTATING IMAGE: {filename}, {cycle * 90} Degrees\n")
                return self.save_image(image, filename)
            else:
                return False

        return False

    def open_image(self, filename: str) -> ImageFile:
        """Intentionally opens an image file using Pillow.
           If opened with OpenCV, the saved image is a much larger file size than the original
           (regardless of whether saved via OpenCV or Pillow).
        """

        return Image.open(Path(self.IMAGES_DIRECTORY + "/" + filename))

    def save_image(self, image: ImageFile, filename: str) -> bool:
        """Saves the rotated image using Pillow."""

        if not self.overwrite_files:
            filename = filename.replace(".", "-rotated.", 1)

        return image.save(Path(self.IMAGES_DIRECTORY + "/" + filename))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Attempts to auto rotate images to their proper orientation.")
    parser.add_argument("overwrite_files", nargs="?", type=int, default=0, help="Whether to use the same filename when saving rotated images.")
    args = parser.parse_args()

    rotator = Rotator(bool(args.overwrite_files))
    rotator.analyze_images()
