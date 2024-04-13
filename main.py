import streamlit as st

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

