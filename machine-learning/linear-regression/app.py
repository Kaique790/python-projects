import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

df.plot(kind="scatter", x="peso kg", y="altura cm")
plt.show()

model = LinearRegression()
x = df[["altura cm"]]
y = df[["peso kg"]]

model.fit(x, y)
altura = float(input("Digite uma altura em cm (ex: 160): "))
pred = model.predict([[altura]])[0][0]

print(f"O peso é próximo de {pred:.2f}kg")
