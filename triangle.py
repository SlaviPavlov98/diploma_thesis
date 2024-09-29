import math


def get_perimeter(a, b, c):
    P = a + b + c
    return P


def get_area(a, b, c):
    s = (a + b + c) / 2

    if a < s and b < s and c < s:
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area
    else:
        return "These sides do not form a valid triangle"


def get_angles(a, b, c):
    A = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
    B = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
    C = 180 - A - B
    return A, B, C


def is_valid_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a


# Example usage
a, b, c = 3, 4, 5

print(f'Is valid triangle: {is_valid_triangle(a, b, c)}')
print(f"Perimeter: {get_perimeter(a, b, c)}")
print(f"Area: {get_area(a, b, c)}")
print(f"Angles: {get_angles(a, b, c)}")
