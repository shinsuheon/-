import streamlit as st

st.title("나의 첫번째 앱")
st.text('\n\n\n\n\n\n')
st.write('ㅎㅇㅎㅇㅎㅇ')
st.write('제 이메일 주소는 안알려줄거야')

st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")

if st.button("Aloha", type="tertiary"):
    st.write("Ciao")
