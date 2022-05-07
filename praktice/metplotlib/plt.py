import numpy as np
import matplotlib.pyplot as plt

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
x = np.linspace(0, 5, 20)
y = np.linspace(0, 10, 20)
plt.plot(x, y, 'purple')  # line
plt.plot(x, y, 'o')      # dots
plt.show()
