import streamlit 

import pandas
import matplotlib.pyplot as plt

dataframe=pandas.read_csv("test.csv")

streamlit.title("Reading CSV")

streamlit.write(dataframe)

streamlit.write(dataframe["score"].mean())

fig, ax = plt.subplots(figsize=(7,4))
ax.bar(dataframe["name"], dataframe["score"])
ax.set_xlabel("Student")
ax.set_ylabel("Score")
ax.set_title("Scores of Students")

streamlit.pyplot(fig)


        
