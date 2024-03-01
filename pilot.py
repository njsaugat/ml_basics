import numpy as np
import matplotlib.pyplot as plt

matrix_a=np.array([[1,2],[3,4]])
matrix_b=np.array([[1,0],[0,1]])

dot_product_result=np.dot(matrix_a,matrix_b)

print(dot_product_result)

plt.imshow(matrix_a, cmap='viridis', interpolation='nearest')
plt.title('Matrix A')
plt.show()
