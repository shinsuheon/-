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

# 제목 설정
st.title("대한민국 년도별 자살율 바 차트")

# 임의의 년도별 자살율 데이터 생성 (단위: 자살자 수(100,000명당))
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
suicide_rates = [31.3, 32.2, 33.3, 29.9, 28.2, 27.1, 26.6, 24.2, 23.3, 22.8, 20.3]  # 예시 자살율 데이터

# 데이터 프레임 생성
data = pd.DataFrame({
    "년도": years,
    "자살율": suicide_rates
})

# 바 차트 출력
st.write("대한민국의 년도별 자살율")
st.bar_chart(data.set_index("년도")["자살율"])

# 데이터 출력
st.write("자살율 데이터:")
st.dataframe(data)

st.image("https://www.google.com/url?sa=i&url=https%3A%2F%2Fm.blog.naver.com%2F131oto%2F222742272800&psig=AOvVaw07RKqnFMNiQHua6ZU34Oeh&ust=1736390375014000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCLCv9KaM5YoDFQAAAAAdAAAAABAn")
