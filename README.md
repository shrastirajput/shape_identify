#Random Shape Generator
This script generates a new image with randomly drawn shapes based on the provided parameters. The shapes can be points, lines, or polygons, and they are drawn on a blank canvas.

#Requirements
Python 3.x
OpenCV (cv2)
Shapely (shapely)
#Installation
Install the required dependencies by running the following command:
$pip install opencv-python shapely

#Usage
Provide an input image file (image_path) where the script will load the image as a background canvas.
Specify the output image file (output_path) where the resulting image with the drawn shapes will be saved.
Run the script and follow the instructions:
$python gen_images.py
Enter the number of shapes to be drawn (num_shapes).
Enter the size of the new image (image_size).
Wait for the script to generate the new image. The progress will be displayed in the console.
Once the image generation is complete, the resulting image will be saved at the specified output path.
#Example
Here's an example usage of the script:
python gen_images.py
Enter the number of shapes to be drawn: 4
Enter the size of the new image: 1024
This will generate an image with 4 randomly drawn shapes on a canvas with a size of 1024x1024 pixels.

#Notes
The script ensures that the randomly generated shapes do not overlap with each other. If overlap occurs, new positions or vertices are generated until non-overlapping shapes are obtained.
The script supports three types of shapes: points, lines, and polygons. The number of vertices for polygons is randomly determined between 3 and 6.
The maximum size of the shapes is determined based on the width and height of the input image. The generated shapes are scaled accordingly.
