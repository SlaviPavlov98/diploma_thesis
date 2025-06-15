# Triangle Calculator
Updated Python script that calculates the perimeter, area, and angles of a triangle given the lengths of its three sides as input. Utilizes Heron's formula to compute the area and the Law of Cosines to determine the angles. The script also validates the triangle based on side lengths.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Core Functions](#core-functions)
  - [get_perimeter(a, b, c)](#get_perimetera-b-c)
  - [get_area(a, b, c)](#get_areaa-b-c)
  - [get_angles(a, b, c)](#get_anglesa-b-c)
  - [is_valid_triangle(a, b, c)](#is_valid_trianglea-b-c)
- [Usage Example](#usage-example)
- [Output](#output)
- [Contributions](#contributions)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    ```

2. Navigate to the project directory:
    ```bash
    cd your-repo-name
    ```

3. Ensure you have Python installed. This script uses Python 3.x.

## Usage

To deploy this script, run it with Python after editing the `a`, `b`, and `c` side lengths for your triangle in the code:

```bash
python triangle.py
```

## Core Functions

### `get_perimeter(a, b, c)`

- **Description**: Get the perimeter of a triangle.
- **Parameters**: `a`, `b`, `c` (floats or integers): Lengths of the triangle sides.
- **Returns**: The calculated perimeter of the triangle.

### `get_area(a, b, c)`

- **Description**: Calculate the area of a triangle using Heron's formula.
- **Parameters**: `a`, `b`, `c` (floats or integers): Lengths of the triangle sides.
- **Returns**: 
  - The calculated area of the triangle if the sides form a valid triangle.
  - A message `"These sides do not form a valid triangle"` if sides don't meet triangle inequality theorem conditions.

### `get_angles(a, b, c)`

- **Description**: Calculate the angles of a triangle using the Law of Cosines. 
- **Parameters**: `a`, `b`, `c` (floats or integers): Lengths of the triangle sides.
- **Returns**: The calculated angles (in degrees) of the triangle.

### `is_valid_triangle(a, b, c)`

- **Description**: Determines if given side lengths can form a valid triangle.
- **Parameters**: `a`, `b`, `c` (floats or integers): Lengths of the triangle sides.
- **Returns**: True if the sides can form a valid triangle, else False.

## Usage Example

Modify the code sample below to execute the calculations on the triangle with given sides `a`, `b`, and `c`:

```python
a, b, c = 3, 4, 5 # Change these values to test with your own values

print(f'Is a valid triangle: {is_valid_triangle(a, b, c)}')
print(f"Perimeter: {get_perimeter(a, b, c)}")
print(f"Area: {get_area(a, b, c)}")
print(f"Angles: {get_angles(a, b, c)}")
```

## Output

The result outputs for a triangle with `a = 3`, `b = 4`, `c = 5`:

```
Is a valid triangle: True
Perimeter: 12
Area: 6.0
Angles: (36.86989764584402, 53.13010235415599, 90.0)
```

## Contributions

Your contributions are always welcome! If you want to collaborate or improve this script, please fork this repository and create a pull request. Here are steps to get you started:

1. Fork the Project
2. Create your Feature Branch as (`git checkout -b feature/InterestingFeature`)
3. Commit your Changes (`git commit -m 'Add an interesting feature'`)
4. Push to the Branch (`git push origin feature/InterestingFeature`)
5. Open a Pull Request