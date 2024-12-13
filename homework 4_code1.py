import numpy as np
import time

def f(x, y):
    return x**2 + y**2  # Example function

def midpoint_double_integral(x_start, x_end, y_start, y_end, nx, ny):
    hx = (x_end - x_start) / nx  # Step size in x direction
    hy = (y_end - y_start) / ny  # Step size in y direction

    integral = 0
    for i in range(nx):
        for j in range(ny):
            x_mid = x_start + (i + 0.5) * hx
            y_mid = y_start + (j + 0.5) * hy
            integral += f(x_mid, y_mid)

    return integral * hx * hy

# Domain and number of points
a, b = 0, 2  
c, d = 0, 2  

nx_total = 100  
ny_total = 100  

# --- Serial Execution ---
start_time_serial = time.time()
serial_integral = midpoint_double_integral(a, b, c, d, nx_total, ny_total)
end_time_serial = time.time()
serial_time = end_time_serial - start_time_serial

print(f'Serial integral value: {serial_integral}')
print(f'Serial execution time: {serial_time} seconds')

# --- Parallel Execution ---
n_workers = 4
x_splits = np.linspace(a, b, n_workers + 1)
worker_results = []

start_time_parallel = time.time()

for i in range(n_workers):
    x_start = x_splits[i]
    x_end = x_splits[i + 1]
    subdomain_integral = midpoint_double_integral(x_start, x_end, c, d, nx_total // n_workers, ny_total)
    worker_results.append(subdomain_integral)
    print(f'Worker {i+1} integral value: {subdomain_integral}')

total_integral = sum(worker_results)
end_time_parallel = time.time()
parallel_time = end_time_parallel - start_time_parallel

print(f'Total parallel integral value: {total_integral}')
print(f'Parallel execution time: {parallel_time} seconds')

# --- Speedup and Efficiency Calculation ---
speedup = serial_time / parallel_time
efficiency = speedup / n_workers

print(f'Speedup: {speedup}')
print(f'Efficiency: {efficiency}')

# --- Consistency Check ---
if abs(serial_integral - total_integral) < 1e-6:  # Allowing a small tolerance
    print("The total integral value from serial and parallel executions match.")
else:
    print("Warning: The total integral values do not match.")