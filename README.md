# Auto Image Rotator

## Overview
This app uses the OpenCV and Dlib computer vision libraries to auto rotate images based on detected human faces.

*This is useful for auto rotating images in bulk that do not contain EXIF orientation meta data (e.g., scanned photos).*

Currently, this is only effective for images that contain one or more face. In the future, [advanced CNN techniques](https://d4nst.github.io/2017/01/12/image-orientation/) may be used to auto correct the rotation for other subjects.

## Setup

#### Images
First, add images you want auto rotated to the `images` directory.

#### Docker
Next, install [Docker](https://www.docker.com/get-started) which is how the app will be run.


## Usage
After installing Docker and adding your image files, rotating your images is as simple as running this command:

```
docker-compose run image-rotator
```

> NOTE: The **first** run will take a few minutes to complete while it installs Dlib's native C extension Python package.

#### Parameters

By default, rotated images are saved as new files with the `*-rotated` filename pattern. If you're comfortable overwriting your original files with rotated versions you may prefix the command with the `OVERWRITE_FILES` param like so:

```
OVERWRITE_FILES=1 docker-compose run image-rotator
```
