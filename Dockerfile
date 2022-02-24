FROM python:3.8

# Update package lists and install CMake (for compiling Dlib).
RUN apt-get -y update && apt-get -y install build-essential cmake python3-opencv

# Set the container's working directory.
WORKDIR /app

# Copy Python dependencies list and install.
# Note: this is done prior to copying all project files to maximize cache hits.
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy the current directory contents into the container's working directory.
COPY . /app
