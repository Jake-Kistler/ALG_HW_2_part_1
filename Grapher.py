import math
import matplotlib.pyplot as plt

# 1. Define the range for n (integer values 2 through 20)
n_values = range(2, 21)

# 2. Define each T(n)
T1 = [15 * (n**2)           for n in n_values]    # 15n^2
T2 = [8 * (n**3)            for n in n_values]    # 8n^3
T3 = [2 * n                 for n in n_values]    # 2n
T4 = [3 * n                 for n in n_values]    # 3n
T5 = [math.factorial(n)     for n in n_values]    # n!
T6 = [n * math.log(n, 2)    for n in n_values]    # n log2(n)

# 3. Create the plot
plt.figure(figsize=(8, 6))

# Plot each sequence with a unique marker/line style
plt.plot(n_values, T1, marker='o', label='15n^2')
plt.plot(n_values, T2, marker='s', label='8n^3')
plt.plot(n_values, T3, marker='^', label='2n')
plt.plot(n_values, T4, marker='d', label='3n')
plt.plot(n_values, T5, marker='v', label='n!')
plt.plot(n_values, T6, marker='>', label='n log₂(n)')

# 4. Because n! grows very fast, a log scale on the y-axis can help visualize
plt.yscale('log')  # comment out if you prefer a regular scale

# 5. Label the axes and add a legend
plt.xlabel('n')
plt.ylabel('T(n)')
plt.title('Growth of Various Functions T(n) for n from 2 to 20')
plt.legend()

# 6. Show the plot
plt.tight_layout()
plt.show()
