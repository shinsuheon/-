import streamlit as st
import random

st.title("나의 첫번째 앱")
st.text('\n\n\n\n\n\n')
st.write('ㅎㅇㅎㅇㅎㅇ')
st.write('제 이메일 주소는 안알려줄거야')

st.button("처음으로 되돌리다", type="primary")
if st.button("뽑다 무작위 숫자를"):
    st.write("random.random()")
else:
    st.write("좋은안녕")

if st.button("알로하", type="tertiary"):
    st.write("챠오")
