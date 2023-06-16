import streamlit as st
from widget.player_list import get_player_list
from widget.player_detail import get_player_detail

st.title("농구")

p = st.selectbox("**POSITION**", ["GUARD", "FORWARD", "CENTER"])

def choice_player(name, img, dunk, link):
    return dict(name=name, img=img, dunk=dunk, link=link)

player1 = choice_player(
    "빈스 카터", "img/vince.jpg", "img/vince-carter.jpg",
    "https://www.youtube.com/watch?v=LrIfS5_TyQQ",
)

player2 = choice_player(
    "르브론 제임스", "img/lebron.jpeg", "img/lebron-james.png",
    "https://www.youtube.com/watch?v=xKdMUAr6_vQ",
)

player3 = choice_player(
    "샤킬 오닐", "img/shaq.jpg", "img/shaquille-o'neal.png",
    "https://www.youtube.com/watch?v=8-trVjrz-N8",
)

if 'detail' not in st.session_state:
    st.session_state['detail'] = ""
    st.session_state['dunk'] = ""
    st.session_state['link'] = ""

if p == "GUARD" :
    get_player_list(player1)
elif p == "FORWARD" :
    get_player_list(player2)
elif p == "CENTER" :
    get_player_list(player3)


# 맛집 상세보기
if st.session_state['detail']:
    get_player_detail()