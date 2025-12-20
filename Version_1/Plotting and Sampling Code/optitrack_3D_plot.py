import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load your Excel file
df = pd.read_excel('Sampled_OPT_data.xlsx')  # Replace with your filename

# Extract coordinates
x = df['X']
y = df['Y']
z = df['Z']

# Plotting
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Scatter plot
ax.scatter(x, y, z, c='blue', s=50)
# Line plot
ax.plot(x, y, z, color='blue', linewidth=2)

# Annotate each point with its serial number (row index + 1)
for i in range(len(df)):
    ax.text(x[i], y[i], z[i], str(i+1), color='red', fontsize=20)

# Labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Plot of Sampled optitrack points')

plt.tight_layout()
plt.show()
