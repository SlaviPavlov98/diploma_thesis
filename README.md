# Triangle Calculator

This Python script calculates the perimeter, area, and angles of a triangle using the lengths of its three sides. It employs Heron's formula to compute the area and the Law of Cosines to calculate the angles. It also verifies the triangle validity based on the specified sides.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Functions](#functions)
  - [get_perimeter(a, b, c)](#get_perimetera-b-c)
  - [get_area(a, b, c)](#get_areaa-b-c)
  - [get_angles(a, b, c)](#get_anglesa-b-c)
- [Example](#example)
- [Output](#output)
- [Contributing](#contributing)

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    ```

2. Navigate to the project directory:
    ```bash
    cd your-repo-name
    ```

3. Ensure you have Python installed. This script uses Python 3.x.

## Usage

To use this script, run it with Python after modifying the side lengths `a`, `b`, and `c` for your triangle in the code:

```bash
python triangle.py
```

## Functions

### `get_perimeter(a, b, c)`

- **Description**: Calculates the perimeter of a triangle.
- **Parameters**:
  - `a` (float or int): Length of the first side.
  - `b` (float or int): Length of the second side.
  - `c` (float or int): Length of the third side.
- **Returns**: The perimeter of the triangle.

### `get_area(a, b, c)`

- **Description**: Calculates the area of a triangle using Heron's formula.
- **Parameters**:
  - `a` (float or int): Length of the first side.
  - `b` (float or int): Length of the second side.
  - `c` (float or int): Length of the third side.
- **Returns**:
  - The area of the triangle if the sides form a valid triangle.
  - A message `"These sides do not form a valid triangle"` if the provided sides do not meet the triangle inequality conditions.

### `get_angles(a, b, c)`

- **Description**: Calculates the angles of the triangle using the Law of Cosines.
- **Parameters**:
  - `a` (float or int): Length of the first side.
  - `b` (float or int): Length of the second side.
  - `c` (float or int): Length of the third side.
- **Returns**: The angles of the triangle (in degrees).

## Example

Modify the following example in the script to calculate the perimeter, area, and angles for a triangle using the sides `a`, `b`, and `c`:

```python
a, b, c = 3, 4, 5  # Modify these values for your triangle

print(f"Perimeter: {get_perimeter(a, b, c)}")
print(f"Area: {get_area(a, b, c)}")
print(f"Angles: {get_angles(a, b, c)}")
```

## Output

For a triangle with sides `a = 3`, `b = 4`, `c = 5`:

```
Perimeter: 12
Area: 6.0
Angles: (36.86989764584402, 53.13010235415599, 90.0)
```

## Contributing

Contributions are welcome! If you'd like to improve this script, please fork the repository and submit a pull request.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/NewFeature`)
3. Commit your Changes (`git commit -m 'Add some feature'`)
4. Push to the Branch (`git push origin feature/NewFeature`)
5. Open a Pull Request