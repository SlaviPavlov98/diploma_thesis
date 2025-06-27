# Triangle Calculator
Python script that calculates the perimeter, area, and angles of a triangle given the lengths of its three sides as input. It utilizes Heron's formula for the computation of the area and the Law of Cosines to determine the angles. The script also checks if the provided side lengths can form a valid triangle.

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

3. Ensure you have Python installed. This script is designed for Python 3.x.

## Usage

To run this script, execute it with Python after specifying the `a`, `b`, and `c` side lengths for your triangle in the code:

```bash
python triangle.py
```

## Core Functions

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

### `get_angles(a, b, c)`

- **Description**: Compute the angles of a triangle using the Law of Cosines. 
- **Parameters**: `a`, `b`, `c` (floats or integers): Side lengths of the triangle.
- **Returns**: The angles (in degrees) of the triangle.

### `is_valid_triangle(a, b, c)`

- **Description**: Checks if the given lengths can form a valid triangle.
- **Parameters**: `a`, `b`, `c` (floats or integers): Side lengths of the triangle.
- **Returns**: `True` if the given side lengths can form a valid triangle, `False` otherwise.

## Usage Example

Make modifications to the code sample below in order to perform calculations on your triangle using the provided sides `a`, `b`, and `c`:

```python
a, b, c = 3, 4, 5

print(f'Is a valid triangle: {is_valid_triangle(a, b, c)}')
print(f"Perimeter: {get_perimeter(a, b, c)}")
print(f"Area: {get_area(a, b, c)}")
print(f"Angles: {get_angles(a, b, c)}")
```

## Output

For a triangle with side lengths `a = 3`, `b = 4`, and `c = 5`, the outputs are:

```
Is a valid triangle: True
Perimeter: 12
Area: 6.0
Angles: (36.86989764584402, 53.13010235415599, 90.0)
```

## Contributions

Your contributions are most welcome! In order to contribute or improve this script, please fork this repository and create a pull request. Follow the steps below to get started:

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/InterestingFeature`)
3. Commit your Changes (`git commit -m 'Add an interesting feature'`)
4. Push to the Branch (`git push origin feature/InterestingFeature`)
5. Open a Pull Request