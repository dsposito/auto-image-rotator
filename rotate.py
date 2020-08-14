import click
import cv2
import dlib
import numpy as np
import os

from pathlib import Path
from PIL import Image, ImageFile


class Rotator:
    IMAGES_DIRECTORY = "/images"

    def __init__(self, overwrite_files: bool=False):
        self.detector = dlib.get_frontal_face_detector()
        self.overwrite_files =overwrite_files

    def analyze_images(self):
        rotations = {}
        with click.progressbar(os.listdir(self.IMAGES_DIRECTORY), label="Analyzing Images...") as files:
            for filename in files:
                if not filename.endswith(".jpeg"):
                    continue

                image = self.open_image(filename)
                rotation = self.analyze_image(image, filename)

                if rotation:
                    rotations[filename] = rotation

        print(f"{len(rotations)} Images Rotated")
        for filename, rotation in rotations.items():
            print(f" - {filename} (Rotated {rotation} Degrees)")

    def analyze_image(self, image: ImageFile, filename: str) -> int:
        """Cycles through 4 image rotations of 90 degrees.
           Saves the image at the current rotation if faces are detected.
        """

        for cycle in range(0, 4):
            if cycle > 0:
                # Rotate the image an additional 90 degrees for each non-zero cycle.
                image = image.rotate(90, expand=True)

            image_copy = np.asarray(image)
            image_gray = cv2.cvtColor(image_copy, cv2.COLOR_BGR2GRAY)

            faces = self.detector(image_gray, 0)
            if len(faces) == 0:
                continue

            # Save the image only if it has been rotated.
            if cycle > 0:
                self.save_image(image, filename)
                return cycle * 90

        return 0

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

        try:
            image.save(Path(self.IMAGES_DIRECTORY + "/" + filename))
            return True
        except:
            return False


@click.command()
@click.argument("overwrite_files", type=click.BOOL, default=False)
def cli(overwrite_files: bool=False):
    rotator = Rotator(overwrite_files)
    rotator.analyze_images()


if __name__ == "__main__":
    cli()
