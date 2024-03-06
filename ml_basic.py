import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


np.random.seed(42)
X=2*np.random.rand(100,1)
y=4+3*X +np.random.randn(100,1)

X_train,X_test,y_train, y_test=train_test_split(X,y,test_size=0.2,random_state=42)

model=LinearRegression()
model.fit(X_train,y_train)

y_pred=model.predict(X_test)


plt.scatter(X_test, y_test, color='black', label='Actual Data')
plt.plot(X_test, y_pred, color='blue', linewidth=3, label='Linear Regression Model')
plt.xlabel('X-axis')
plt.ylabel('y-axis')
plt.title('Simple Linear Regression Example')
plt.legend()
plt.show()