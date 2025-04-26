import streamlit as st
import pandas as pd
import numpy as np

## title of the application
st.title("Hello Streamlit")

## Display simple text
st.write("This is a simple text")

## Create simple dataFrame
df = pd.DataFrame({
    "first column": [1,2,3,4],
    "second column": [10,20,30,40]
})

## Display dataFrame
st.write("Here is DataFrame")
st.write(df)

## Create simple line chart
chart_data=pd.DataFrame(
    np.random.randn(20,3), columns=['a','b','c']
)
st.line_chart(chart_data)