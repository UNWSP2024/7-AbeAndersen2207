#UNWSP Programming PythonCos2005DEsp25
#Week#7_Program#4 Coordinates
#03/7/2025
#Abraham. N. Andersen

#Write a distance function that will take two 3-dimensional coordinates (as input) and will return
#(as output) the distance between those points in space.  The 3-dimensional coordinates must be
#stored as tuples. Now write a mainline that has the user enter the two tuples.  The mainline calls
#the distance function and stores the distance in a variable.  The mainline then displays the distance.
#Also include exception handling to deal with faulty input.
#The distance between two points (x1,y1,z1) and (x2, y2, z2) is given by:
#sqrt ((x2-x1)^2 + (y2 - y1)^2 + (z1 - z2)^2

import math


def calculate_distance(point1, point2):
    """Calculates the distance between two 3D points.

    Args:
        point1: A tuple representing the first point (x1, y1, z1).
        point2: A tuple representing the second point (x2, y2, z2).

    Returns:
        The distance between the two points, rounded to 4 decimal places.
        Returns None if input is invalid.
    """
    try:
        if not (isinstance(point1, tuple) and isinstance(point2, tuple) and
                len(point1) == 3 and len(point2) == 3 and
                all(isinstance(coord, (int, float)) for coord in point1) and
                all(isinstance(coord, (int, float)) for coord in point2)):
            return None  # Invalid input

        x1, y1, z1 = point1
        x2, y2, z2 = point2

        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
        return round(distance, 4)

    except TypeError:
        return None  # In case there are non-numbers in the tuples.
    except Exception as e:  # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")
        return None


# Mainline
while True:
    try:
        point1_str = input("Enter the first 3D point (x, y, z), separated by commas: ")
        point1_coords = tuple(map(float, point1_str.split(',')))

        point2_str = input("Enter the second 3D point (x, y, z), separated by commas: ")
        point2_coords = tuple(map(float, point2_str.split(',')))

        distance = calculate_distance(point1_coords, point2_coords)

        if distance is not None:
            print(f"The distance between the two points is: {distance}")
            break  # Exit the loop if successful.
        else:
            print("Invalid input. Please enter valid 3D coordinates.")

    except ValueError:
        print("Invalid input format. Please enter numbers separated by commas.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")