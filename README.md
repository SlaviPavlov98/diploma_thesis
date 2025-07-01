# Triangle Calculator

A Python script for calculating the perimeter, area, and angles of a triangle. This script accepts the inputs for the side lengths of the triangle and applies mathematical formulas to calculate the related properties. It also checks the validity of a triangle based on the given side lengths. It now includes a function to calculate the inner angles of the triangle as well.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Key Functions](#key-functions)
    - [get_perimeter(a, b, c)](#get_perimetera-b-c)
    - [get_area(a, b, c)](#get_areaa-b-c)
    - [is_valid_triangle(a, b, c)](#is_valid_trianglea-b-c)
    - [get_angles(a, b, c)](#get_anglesa-b-c)
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
3. Ensure you have Python installed. This script is designed for Python 3.x.

## Usage

To run this script, execute it with Python after specifying the `a`, `b`, and `c` side lengths for your triangle in the code:

```bash
python triangle.py
```

## Key Functions

### `get_perimeter(a, b, c)`

- **Description**: Calculates the perimeter of a triangle.
- **Parameters**: `a`, `b`, `c` (floats or integers): Side lengths of the triangle.
- **Returns**: The perimeter of the triangle.

### `get_area(a, b, c)`

- **Description**: Calculates the area of a triangle using Heron's formula.
- **Parameters**: `a`, `b`, `c` (floats or integers): Side lengths of the triangle.
- **Returns**: 
  - The area of the triangle if the provided sides form a valid triangle.
  - `"These sides do not form a valid triangle"` if the sides do not meet the conditions defined by the Triangle Inequality Theorem.

### `is_valid_triangle(a, b, c)`

- **Description**: Checks whether three given lengths can form a valid triangle.
- **Parameters**: `a`, `b`, `c` (floats or integers): Side lengths to form a triangle.
- **Returns**: 
  - True if the sides form a valid triangle.
  - False if the sides do not form a valid triangle.

### `get_angles(a, b, c)`

- **Description**: Calculates the angles of a triangle in degrees.
- **Parameters**: `a`, `b`, `c` (floats or integers): Side lengths of the triangle.
- **Returns**: The angles of the triangle defined by side lengths a, b, and c.

## Usage Example

If you want to run the calculations on a triangle with side lengths `a=3`, `b=4`, and `c=5`, you can input them into the Python console as shown below:

```python
a, b, c = 3, 4, 5

print(f'Is valid triangle: {is_valid_triangle(a, b, c)}')
print(f"Perimeter: {get_perimeter(a, b, c)}")
print(f"Area: {get_area(a, b, c)}")
print(f"Angles: {get_angles(a, b, c)}")
```

## Output

The output given for a triangle with side lengths `a = 3`, `b = 4`, and `c = 5`:

```
Is valid triangle: True
Perimeter: 12
Area: 6.0
Angles: (36.86989764584402, 53.13010235415599, 90.0)
```

## Contributions

Contributions are encouraged and welcomed! If you wish to develop or improve the script, you can fork this repository and open a pull request. Simply follow the steps below to get started:

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/InterestingFeature`)
3. Commit your Changes (`git commit -m 'Add some InterestingFeature'`)
4. Push to the Branch (`git push origin feature/InterestingFeature`)
5. Open a Pull Request