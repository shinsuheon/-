import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# 제목 설정
st.title("대한민국 년도별 자살율 애니메이션 차트")

# 임의의 년도별 자살율 데이터 생성 (단위: 자살자 수(100,000명당))
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
suicide_rates = [31.3, 32.2, 33.3, 29.9, 28.2, 27.1, 26.6, 24.2, 23.3, 22.8, 20.3]

# 데이터 프레임 생성
data = pd.DataFrame({
    "년도": years,
    "자살율": suicide_rates
})

# Plotly 애니메이션 차트 생성
fig = go.Figure(
    data=[go.Bar(
        x=data['년도'],
        y=data['자살율'],
        text=data['자살율'],
        textposition='auto',
        marker=dict(color='rgba(50, 171, 96, 0.6)', line=dict(color='rgba(50, 171, 96, 1.0)', width=2))
    )],
    layout=go.Layout(
        title="대한민국의 년도별 자살율",
        xaxis=dict(title='년도'),
        yaxis=dict(title='자살율 (100,000명당)'),
        updatemenus=[dict(
            type="buttons",
            showactive=False,
            buttons=[dict(label="Play", method="animate", args=[None, dict(frame=dict(duration=500, redraw=True), fromcurrent=True)])]
        )],
        sliders=[dict(
            active=0,
            currentvalue={"prefix": "년도: ", "visible": True},
            steps=[dict(label=str(year), method="animate", args=[[str(year)], dict(frame=dict(duration=500, redraw=True), mode="immediate", transition=dict(duration=300))]) for year in data['년도']]
        )]
    ),
    frames=[go.Frame(
        data=[go.Bar(
            x=data[data['년도'] <= year]['년도'],
            y=data[data['년도'] <= year]['자살율'],
            text=data[data['년도'] <= year]['자살율'],
            textposition='auto'
        )],
        name=str(year)
    ) for year in data['년도']]
)

# 애니메이션 차트 출력
st.plotly_chart(fig)
