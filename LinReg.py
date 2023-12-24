import numpy as np
import matplotlib as plt
from lab_utils_uni import plt_intuition, plt_stationary, plt_update_onclick, soup_bowl

x_train = np.array([1.0,2.0])
y_train = np.array([300.0, 500.0])

# Numpy arrays have a .shape parameter. x_train.shape returns a python tuple with an entry for each dimension
# m = x_train.shape[0]
m = len(x_train)
print(f"Number of training examples is: {m}")

# Training example x_i, y_i
i = 0
x_i = x_train[i]
y_i = y_train[i]
print(f"(x^({i}), y^({i})) = ({x_i}, {y_i})")

# Plot the data points
plt.scatter(x_train, y_train, marker='x', c='r')
# Set the title
plt.title("Housing Prices")
# Set the y-axis label
plt.ylabel('Price (in 1000s of dollars)')
# Set the x-axis label
plt.xlabel('Size (1000 sqft)')
plt.show()
