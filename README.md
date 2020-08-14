# Auto Image Rotator

## Overview
This app uses the OpenCV and Dlib computer vision libraries to auto rotate images based on detected human faces.

*This is useful for auto rotating images in bulk that do not contain EXIF orientation meta data (e.g., scanned photos).*

Currently, this is only effective for images that contain one or more face. In the future, [advanced CNN techniques](https://d4nst.github.io/2017/01/12/image-orientation/) could be implemented to auto correct the rotation for other subjects.

## Setup

#### Docker
1. Install [Docker](https://www.docker.com/get-started) so we can build and run the app.

2. Build the app's Docker image (this take a few minutes to complete while it builds Dlib's native C extension for Python):
```
docker-compose build app
```

## Usage
After the one-time setup, rotating a directory of images is as simple as running this command:

```
IMAGES_PATH=/path/to/your/images/folder docker-compose run app
```

By default, rotated images are saved as new files with a `*-rotated` filename pattern in your `IMAGES_PATH` directory. If you're comfortable overwriting your original files with rotated versions you may prefix the command with the `OVERWRITE_FILES` param like so:

```
IMAGES_PATH=/path/to/your/images/folder OVERWRITE_FILES=1 docker-compose run app
```
