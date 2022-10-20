import streamlit 

streamlit.title('My Moms New Healthy Breakfast')

streamlit.header('Breakfast Menu')
streamlit.text('Vada Sambar')
streamlit.text('idli Sambar')
streamlit.text('Dosa')

import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.dataframe(my_fruit_list)
