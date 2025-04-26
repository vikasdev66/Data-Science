import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

@st.cache_data
def load_data():
    iris= load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    return df, iris.target_names

df,target_name=load_data()

model=RandomForestClassifier()
model.fit(df.iloc[:,:-1], df['species'])

st.sidebar.title("Input Features")
st.slider('sepal length', float(df['sepal length (cm)'].min()), float(df['sepal length (cm)'].max()))