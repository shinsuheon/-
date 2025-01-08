import streamlit as st
import pandas as pd
import numpy as np

# 제목 설정
st.title("국가별 출산율 바 차트")

# 출산율 데이터를 만들기 위해 임의의 국가와 출산율 값을 생성
countries = ["한국", "미국", "일본", "프랑스", "독일", "영국", "캐나다", "호주", "브라질", "인도"]
birth_rates = [0.84, 1.78, 1.34, 1.88, 1.53, 1.65, 1.47, 1.70, 2.14, 2.21]  # 예시 출산율 데이터

# 출산율 데이터를 DataFrame으로 변환
data = pd.DataFrame({
    "국가": countries,
    "출산율": birth_rates
})

# 바 차트 출력
st.write("각 국가의 출산율")
st.bar_chart(data.set_index("국가")["출산율"])

# 데이터 출력
st.write("출산율 데이터:")
st.dataframe(data)

st.image('funny.pns')
