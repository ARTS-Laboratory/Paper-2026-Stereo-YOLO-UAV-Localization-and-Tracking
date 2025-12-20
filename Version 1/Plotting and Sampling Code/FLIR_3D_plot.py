import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Function to apply rotation and translation
def transform_coordinates(x, y, z, rotation_deg, translation):
    # Convert Euler angles (degrees) to radians
    rx, ry, rz = np.radians(rotation_deg)

    # Rotation matrices
    Rx = np.array([[1, 0, 0],
                   [0, np.cos(rx), -np.sin(rx)],
                   [0, np.sin(rx), np.cos(rx)]])
    
    Ry = np.array([[np.cos(ry), 0, np.sin(ry)],
                   [0, 1, 0],
                   [-np.sin(ry), 0, np.cos(ry)]])
    
    Rz = np.array([[np.cos(rz), -np.sin(rz), 0],
                   [np.sin(rz), np.cos(rz), 0],
                   [0, 0, 1]])

    # Combined rotation matrix
    R = Rz @ Ry @ Rx  # Note: ZYX order of rotations

    # Stack coordinates and apply transformation
    coords = np.vstack((x, y, z))
    transformed_coords = R @ coords + np.array(translation).reshape(3, 1)

    return transformed_coords[0], transformed_coords[1], transformed_coords[2]

# Load your Excel file
df = pd.read_excel('Hand_marked_coordinate_non_normalized.xlsx')

# Extract coordinates
x = df['3D_X'].to_numpy()
y = df['3D_Y'].to_numpy()
z = df['3D_Z'].to_numpy()

# Define rotation in degrees (rx, ry, rz) and translation (tx, ty, tz)
rotation_deg = [0, 0, 0]       # Example: 30° rotation around X-axis
translation = [0, 0, 0]      # Example: translate by (100, 0, 50)

# Apply transformation
x_t, y_t, z_t = transform_coordinates(x, y, z, rotation_deg, translation)

# Plotting
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Scatter plot
ax.scatter(x_t, y_t, z_t, c='blue', s=50)
# Line plot
ax.plot(x_t, y_t, z_t, color='blue', linewidth=2)

# Annotate each point with its serial number (row index + 1)
for i in range(len(df)):
    ax.text(x_t[i], y_t[i], z_t[i], str(i+1), color='red', fontsize=20)

# Labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Transformed 3D Plot of Hand-drawn FLIR Images')

plt.tight_layout()
plt.show()
