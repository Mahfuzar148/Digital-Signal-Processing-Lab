 ##Filter realization using 6-point averaging, 6-point differencing equations.


import numpy as np
import matplotlib.pyplot as plt

# Example input signal
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# 6-point averaging filter
def six_point_average(x):
    y = np.zeros_like(x, dtype=float)
    for i in range(5, len(x)):
        y[i] = np.mean(x[i-5:i+1])
    return y

# 6-point differencing filter
def six_point_difference(x):
    y = np.zeros_like(x, dtype=float)
    for i in range(6, len(x)):
        y[i] = x[i] - x[i-6]
    return y

# Apply filters
avg_output = six_point_average(x)
diff_output = six_point_difference(x)

# Plotting
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(x, label='Original Signal')
plt.plot(avg_output, label='6-Point Averaging Filter', linestyle='--')
plt.title("6-Point Averaging Filter")
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(x, label='Original Signal')
plt.plot(diff_output, label='6-Point Differencing Filter', linestyle='--')
plt.title("6-Point Differencing Filter")
plt.legend()
plt.tight_layout()
plt.show()

