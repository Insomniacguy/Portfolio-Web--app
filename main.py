import streamlit as st
import pandas

df = pandas.read_csv('data.csv', sep=';')
st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image('Images/me with glasses.png')

with col2:
    st.title("Rahul Chandan")
    content = """I'm Rahul, a freelance Python developer. I completed my Bachelors of Science in Information 
    Technology from Mumbai University in 2017. Over the years, I've gained experience in diverse fields such as 
    online marketing, cybersecurity, and healthcare. My broad understanding of different business areas allows me to 
    grasp your unique requirements effectively. I specialize in crafting tailored software solutions that prioritize 
    security, scalability, and relevance to your business needs."""
    # st.write(content)
    st.info(content)

content2 = """
Below, you can find some of the apps that I have built. Feel free to contact me
"""
st.info(content2)

st.write(df)

col3, col4 = st.columns(2)

# slicing used for diving the content in 2 columns
with col3:
    # for title in df["title"]:
    #     st.header(title)
    for index, row in df[:10].iterrows():  # slicing from 0 till 10. first 10 items
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():  #starting from index 10. So last 10 items
        st.header(row["title"])
