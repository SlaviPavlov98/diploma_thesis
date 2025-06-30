# Triangle Calculator

A Python script for calculating the perimeter and area of a triangle. The script uses the user's input for the side lengths of the triangle and applies Heron's formula for area calculation. The script can also determine the validity of a triangle based on the given side lengths.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Key Functions](#key-functions)
  - [get_perimeter(a, b, c)](#get_perimetera-b-c)
  - [get_area(a, b, c)](#get_areaa-b-c)
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

- **Description**: Checks if the provided side lengths are able to form a valid triangle.
- **Parameters**: `a`, `b`, `c` (floats or integers): Side lengths of the triangle.
- **Returns**: `True` if the given side lengths can form a valid triangle. `False` otherwise.

## Usage Example

If you want to use the script for calculations on a triangle with side lengths `a`, `b`, and `c`, channel changes to:

```python
a, b, c = 3, 4, 5

print(f'Is valid triangle: {is_valid_triangle(a, b, c)}')
print(f"Perimeter: {get_perimeter(a, b, c)}")
print(f"Area: {get_area(a, b, c)}")
```

## Output

The output given for a triangle with side lengths `a = 3`, `b = 4`, and `c = 5`:

```
Is a valid triangle: True
Perimeter: 12
Area: 6.0
```

## Contributions

Contributions are encouraged and welcomed! If you wish to develop or improve the script, you can fork this repository and open a pull request. Simply follow the steps below to get started:

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/InterestingFeature`)
3. Commit your Changes (`git commit -m 'Add some InterestingFeature'`)
4. Push to the Branch (`git push origin feature/InterestingFeature`)
5. Open a Pull Request