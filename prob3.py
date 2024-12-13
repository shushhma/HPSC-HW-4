import numpy as np
import matplotlib.pyplot as plt
import time

max_iterations = 1000
grid_size = 1000
xlim = [-0.748766713922161, -0.748766707771757]
ylim = [0.123640844894862, 0.123640851045266]

start_time = time.time()
x = np.linspace(xlim[0], xlim[1], grid_size)
y = np.linspace(ylim[0], ylim[1], grid_size)
x_grid, y_grid = np.meshgrid(x, y)
z0 = x_grid + 1j * y_grid
count = np.zeros_like(z0, dtype=float)

z = z0
for n in range(max_iterations):
    mask = np.abs(z) <= 2  # Create a mask for points that are still in the iteration
    count += mask  # Update count only for points that are still valid
    z[mask] = z[mask] * z[mask] + z0[mask]  # Update only valid points

count = np.log(count + 1)  # Avoid log(0)

cpu_time = time.time() - start_time
plt.figure(figsize=(6, 6))
plt.imshow(count, extent=(xlim[0], xlim[1], ylim[0], ylim[1]), cmap='jet')
plt.axis('equal')
plt.axis('off')
plt.colorbar()
plt.title(f'{cpu_time:.2f} secs (serial)')
plt.show()


