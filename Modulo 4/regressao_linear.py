import numpy as np

x = np.array([[160],[165],[171],[174],[179],[181],[185],[188],[191],[200]])

y = np.array([[64],[67],[70],[80],[77],[81],[87],[94],[101],[112]])

import matplotlib.pyplot as plt

plt.scatter(x,y)


from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x,y)

regressor.intercept_
regressor.coef_

previsao = regressor.intercept_ + regressor.coef_ * 190
print(previsao)
previsao1 = regressor.predict(np.array([[190]]).reshape(1,1))

previsao2 = regressor.predict(x)
resultado = abs(y - previsao2).mean()
print(resultado)

from sklearn.metrics import mean_absolute_error, mean_squared_error

mae = mean_absolute_error(y, previsao2)
print(mae)

mse = mean_squared_error(y, previsao2)
print(mse)

plt.plot(x, y, 'o')
plt.plot(x, previsao2, color = 'red')
plt.title('Regressão Linear Simples')
plt.xlabel('Altura')
plt.ylabel('Peso')
plt.show()