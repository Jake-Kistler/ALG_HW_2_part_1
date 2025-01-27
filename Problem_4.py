import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

# Define the two functions
T1 = lambda n: 0.5 * n**2
T2 = lambda n: 6 * n * np.log2(n) + 6 * n

# Define the function for their difference
difference = lambda n: T1(n) - T2(n)

# Find the intersection point
intersection_point = fsolve(difference, x0=50)[0]  # Initial guess is n=50

# Print the intersection point
print(f"The intersection point is approximately at n = {intersection_point:.5f}")

# Define the range of n values to plot and check
n_values = np.linspace(1, 200, 500)  # Plot for n from 1 to 200
T1_values = T1(n_values)
T2_values = T2(n_values)

# Plot the functions and their intersection point
plt.figure(figsize=(10, 6))
plt.plot(n_values, T1_values, label="T1(n) = 0.5n^2", color="blue")
plt.plot(n_values, T2_values, label="T2(n) = 6nlogn + 6n", color="green")
plt.scatter(intersection_point, T1(intersection_point), color="red", label=f"Intersection at n ≈ {intersection_point:.2f}")
plt.axvline(intersection_point, color="red", linestyle="--", label=f"n = {intersection_point:.2f}")

# Add labels and legend
plt.title("Comparison of T1(n) and T2(n)")
plt.xlabel("n")
plt.ylabel("Steps")
plt.legend()
plt.grid()
plt.show()

# Determine the interval where T2(n) < T1(n)
if intersection_point > 0:
    print(f"Algorithm-2 performs better than Algorithm-1 for n > {intersection_point:.2f}.")
else:
    print("Algorithm-2 does not perform better than Algorithm-1 in the tested range.")
