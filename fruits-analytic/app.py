# core 0 = vermelho
# core 1 = amarelo
# core 2 = laranja

# textura => 0 = lisa | 1 - Áspera

import pandas as pd
import streamlit as st
from sklearn import tree

df = pd.read_csv("fruits.csv")
model = tree.DecisionTreeClassifier()

x_treino = df.iloc[:, :-1]
y_treino = df.iloc[:, -1]

model.fit(x_treino, y_treino)

st.title("Classificar fruta:")

textures = ["Áspera", "lisa"]
colors = ["amarelo", "vermelho", "laranja"]

fruitWeigth = st.number_input("Digite o peso da fruta")

fruitTexture = st.selectbox("Textura da fruta", textures)
fruitColor = st.selectbox("Selecione a cor da fruta", colors)

if (fruitColor and fruitTexture and fruitWeigth):
    pred = {
        "cor":[colors.index(fruitColor)],
        "peso": (fruitWeigth),
        "textura": [textures.index(fruitTexture)]
    }

    df_pred = pd.DataFrame(pred)
    fruit = model.predict(df_pred)[0]

    st.subheader(f"Possivelmente, a fruta classificada é: {fruit}")
