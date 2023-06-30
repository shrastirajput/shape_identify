import cv2
import numpy as np
import random
from shapely.geometry import Polygon, Point, LineString

def check_overlap(shape1, shape2):
    # Create Shapely objects for the two shapes
    shapely_shape1 = create_shapely_object(shape1)
    shapely_shape2 = create_shapely_object(shape2)

    # Check if the shapes intersect
    return shapely_shape1.intersects(shapely_shape2)

def create_shapely_object(shape):
    if shape['type'] == 'point':
        return Point(shape['x'], shape['y'])
    elif shape['type'] == 'line':
        return LineString([(shape['x1'], shape['y1']), (shape['x2'], shape['y2'])])
    elif shape['type'] == 'polygon':
        return Polygon([(point['x'], point['y']) for point in shape['points']])
    else:
        raise ValueError(f"Invalid shape type: {shape['type']}")

def draw_shapes(image_path, output_path, num_shapes, image_size):
    # Read the image
    image = cv2.imread(image_path)

    # Check if the image is successfully loaded
    if image is None:
        print(f"Error: Failed to load the image at '{image_path}'")
        return

    # Get the image dimensions
    height, width, _ = image.shape

    # Calculate the maximum size for the shapes
    max_shape_size = min(width, height) // 2

    # Calculate the size of the new image
    new_image_size = (image_size, image_size)
    canvas = np.ones((new_image_size[0], new_image_size[1], 3), dtype=np.uint8) * 255

    # Generate random positions for the shapes
    positions = []
    for _ in range(num_shapes):
        x = random.randint(0, new_image_size[1] - 1)
        y = random.randint(0, new_image_size[0] - 1)
        positions.append((x, y))

    # Draw the shapes on the new image
    for position in positions:
        # Generate a random rotation angle between 0 and 90 degrees
        angle = random.randint(0, 90)

        # Generate a random shape size between 0.75 and 1 times the maximum size
        size = random.uniform(0.75, 1) * max_shape_size

        # Choose a random shape type to draw
        shape_type = random.choice(['point', 'line', 'polygon'])

        if shape_type == 'point':
            # Generate a random point
            point = {'type': 'point', 'x': position[0], 'y': position[1]}

            # Check overlap with existing shapes
            while any(check_overlap(point, existing_shape) for existing_shape in positions):
                x = random.randint(0, new_image_size[1] - 1)
                y = random.randint(0, new_image_size[0] - 1)
                point = {'type': 'point', 'x': x, 'y': y}

            # Draw the point on the canvas
            cv2.circle(canvas, (point['x'], point['y']), 1, (0, 0, 255), -1)

        elif shape_type == 'line':
            # Generate random endpoints for the line
            x1 = position[0]
            y1 = position[1]
            x2 = random.randint(0, new_image_size[1] - 1)
            y2 = random.randint(0, new_image_size[0] - 1)
            line = {'type': 'line', 'x1': x1, 'y1': y1, 'x2': x2, 'y2': y2}

            # Check overlap with existing shapes
            while any(check_overlap(line, existing_shape) for existing_shape in positions):
                x2 = random.randint(0, new_image_size[1] - 1)
                y2 = random.randint(0, new_image_size[0] - 1)
                line = {'type': 'line', 'x1': x1, 'y1': y1, 'x2': x2, 'y2': y2}

            # Draw the line on the canvas
            cv2.line(canvas, (line['x1'], line['y1']), (line['x2'], line['y2']), (0, 255, 0), 1)

        elif shape_type == 'polygon':
            # Generate random vertices for the polygon
            num_vertices = random.randint(3, 6)
            points = []
            for _ in range(num_vertices):
                x = random.randint(0, new_image_size[1] - 1)
                y = random.randint(0, new_image_size[0] - 1)
                points.append({'x': x, 'y': y})
            polygon = {'type': 'polygon', 'points': points}

            # Check overlap with existing shapes
            while any(check_overlap(polygon, existing_shape) for existing_shape in positions):
                points = []
                for _ in range(num_vertices):
                    x = random.randint(0, new_image_size[1] - 1)
                    y = random.randint(0, new_image_size[0] - 1)
                    points.append({'x': x, 'y': y})
                polygon = {'type': 'polygon', 'points': points}

            # Draw the polygon on the canvas
            vertices = np.array([(point['x'], point['y']) for point in polygon['points']], dtype=np.int32)
            cv2.polylines(canvas, [vertices], True, (255, 0, 0), 1)

        positions.append(create_shapely_object({'type': shape_type, 'points': points}))

    # Save the new image with the drawn shapes
    cv2.imwrite(output_path, canvas)

# Example usage
image_path = 'C:\\Users\\TEI-1114\\Desktop\\shape.png'
output_path = 'C:\\Users\\TEI-1114\\Desktop\\image_try.png'
num_shapes = int(input("Enter the number of shapes to be drawn: "))
image_size = int(input("Enter the size of the new image: "))
draw_shapes(image_path, output_path, num_shapes, image_size)
