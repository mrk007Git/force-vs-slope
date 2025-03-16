import numpy as np
import matplotlib.pyplot as plt

# Define slope angles (in degrees)
angles = np.linspace(0, 90, 19)  # From 0 to 90 degrees

# Define weight values in kg
weights = {
    "200kg (2 people)": 200,
    "280kg (3 people)": 280,
    "360kg (4 people)": 360,
    "440kg (5 people)": 440,
    "520kg (6 people)": 520
}

# Gravitational acceleration
g = 9.81  # m/s²

# Compute force values using F = mg sin(θ), converted to kN
forces_on_rope = {
    label: (mass * g * np.sin(np.radians(angles))) / 1000 for label, mass in weights.items()
}

# Function to plot the background gradient
def plot_background():
    y = np.linspace(0, 6, 100)
    X, Y = np.meshgrid(angles, y)
    Z = Y
    plt.contourf(X, Y, Z, levels=[0, 2, 4, 6], colors=['green', 'yellow', 'orange', 'red'], alpha=0.3)

# Create the plot
plt.figure(figsize=(10, 6))
plot_background()

# Plot each dataset based on the formula
for label, force_values in forces_on_rope.items():
    plt.plot(angles, force_values, marker='o', linestyle='-', label=label)

# Labels and title
plt.xlabel("Slope Angle (degrees)")
plt.ylabel("Force (kN)")
plt.title("Force (kN) on the Rope vs. Slope Angle Based on Gravity Formula")
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
