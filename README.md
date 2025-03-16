# Force vs Slope Angle

This project visualizes the force exerted on a rope when a stretcher and carry party are pulled up a slope at varying angles. It calculates the force using basic physics principles and plots the results using Python and Matplotlib.

## Sample Output
![Figure_1](https://github.com/user-attachments/assets/b1186ca1-f60a-4f2d-88e6-fda0f8387816)

## Overview
The force exerted on the rope is computed using the formula:

\[ F = W \times \sin(\theta) \]

Where:
- \( F \) is the force on the rope (in kN),
- \( W \) is the weight (mass \( \times \) gravity, in Newtons),
- \( \theta \) is the slope angle in degrees.

## Features
- Calculates force for multiple weight categories (200kg to 520kg).
- Visualizes force vs. slope angle on a graph.
- Background gradient shows safe and dangerous force zones (green to red).

## Requirements
- Python 3.x
- numpy
- matplotlib

Install dependencies:
```bash
pip install numpy matplotlib
```

## How to Run
1. Clone this repository:
```bash
git clone https://github.com/mrk007Git/force-vs-slope.git
cd force-vs-slope
```

2. Run the Python script:
```bash
python main.py

```

## Acknowledgements
Inspired by Nicholas Le Maitre and his work on rope forces in rescue scenarios.
Learn more: [Steep Slope Stretcher Work](https://sites.google.com/site/mcsasearchandrescue/rescue-skills/technical/2---intermediate/steep-slope-stretcher-work)


## License
This project is licensed under the MIT License.

## Author
Michael Klopper - Inspired by real-world rope force scenarios in rescue operations.
