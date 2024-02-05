import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pickle
import plotly.express as px

st.title("2023년 KBO 리그 중계방송 통계")

with open(file="resultA.pickle", mode="rb") as f:
    result_bc = pickle.load(f)
with open(file="resultB.pickle", mode="rb") as f:
    result_team = pickle.load(f)

team_list = ["LG", "KT", "SSG", "NC", "두산", "KIA", "롯데", "삼성", "한화", "키움"]
custom_palette = {"LG": (165, 0, 52), 'KT': (0, 0, 0), "SSG": (206, 14, 45), "NC": (49, 82, 136), "두산": (19, 19, 48),
                  "KIA": (234, 0, 41), "롯데": (4, 30, 66), "삼성": (7, 76, 161), "한화": (255, 102, 0), "키움": (87, 5, 20)}


team = st.selectbox(
    '확인하고 싶은 팀을 선택해주세요', team_list)
df = result_team[team]

fig = px.bar(df, x="경기수", text="경기수", title=f"{team}의 방송사별 중계 횟수 (총 {df['경기수'].sum()}회 중계)")
fig.update_xaxes(range=[0, 55])
fig.update_traces(textposition='outside')
fig.update_layout(yaxis={'categoryorder': 'total ascending'}, yaxis_title="방송사")
st.plotly_chart(fig, use_container_width=True)

bc_names = {"SPO": "SPOTV 및 SPOTV-2", "MS-T": "MBC Sports+", "KN-T": "KBS N Sports", "SS-T": "SBS Sports",
           "SPO-T": "SPOTV", "SPO-2T": "SPOTV-2", "S-T": "SBS(지상파)", "M-T": "MBC(지상파)", "K-2T": "KBS2(지상파)",
           "G-CMB": "CMB광주방송", "D-CMB": "CMB대전방송", "중계없음": "중계없음(OTT)", "KMS": "지상파(KBS2 + MBC + SBS)"}
bc_list = bc_names.values()
bc = st.selectbox(
    '확인하고 싶은 방송국을 선택해주세요', bc_list)
bc_names_back = {v: k for k, v in bc_names.items()}
bc_code = bc_names_back[bc]

if bc_code == "SPO":
    max_y = 100
elif bc_code in ["G-CMB", "D-CMB"]:
    max_y = 30
elif bc_code == "KMS":
    max_y = 10
elif bc_code in ["M-T", "S-T", "K-2T", "중계없음"]:
    max_y = 5
else:
    max_y = 60


sr = result_bc[bc_code]

fig = px.bar(sr, y="팀", text="팀", title=f"{bc}의 팀별 중계 횟수 (총 {int(sr.sum())}회 중계)")
fig.update_yaxes(range=[0, max_y])
fig.update_traces(textposition='outside')
fig.update_layout(xaxis_title="팀", yaxis_title="경기수")
st.plotly_chart(fig, use_container_width=True)







