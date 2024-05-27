# Github: https://github.com/RahulTriedCoding
# Twitter: https://x.com/RahulChandanDev
# LinkedIn: https://www.linkedin.com/in/rahulwritescode
# Youtube: www.youtube.com/@Rahulwritescodeyt
# Gmail: rahulwritescode01@gmail.com

import streamlit as st
import pandas

df = pandas.read_csv('data.csv', sep=';')
st.set_page_config(layout="wide")

col1, empty_col, col2 = st.columns([1.5, 0.5, 1.5])

with col1:
    st.image('Images/me with glasses.png', width=400)

with col2:
    st.title("Rahul Chandan")
    content = """Hey there! I'm Rahul, a freelance Python developer who loves creating secure and scalable software 
    solutions. With experience in ethical hacking and online marketing I get what businesses need and 
    how to make things work smoothly. Let's build something awesome together."""
    # st.write(content)
    st.info(content)

content2 = """
Below, you can find some of the apps that I have built. Feel free to contact me
"""
st.info(content2)

# st.write(df)

col3, col4 = st.columns(2)

# slicing used for diving the content in 2 columns
with col3:
    # for title in df["title"]:
    #     st.header(title)
    for index, row in df[:10].iterrows():  # slicing from 0 till 10. first 10 items
        st.header(row["title"])
        st.write(row["description"])
        st.image("Images/" + row["image"])  # concatenatin to create a relative path
        st.write(f"[Source code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():  #starting from index 10. So last 10 items
        st.header(row["title"])
        st.write(row["description"])
        st.image("Images/" + row["image"])
        st.write(f"[Source code]({row['url']})")
