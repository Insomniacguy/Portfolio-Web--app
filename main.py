import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image('Images/me with glasses.png')

with col2:
    st.title("Rahul Chandan")
    content = """I'm Rahul, a freelance Python developer. My background spans online marketing, cybersecurity, 
    and healthcare. With expertise across various business domains, I excel in understanding your specific use cases."""
    # st.write(content)
    st.info(content)