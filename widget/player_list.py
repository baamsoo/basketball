import streamlit as st

def set_detail(name):
    st.session_state['detail'] = name

def get_player_list(players):
    player = st.expander(players["name"])
    img = player.image(players["img"], use_column_width=True)
    if st.button("자세히보기", key=f"button", use_container_width=True):
        st.session_state['detail'] = players["name"]
        st.session_state['dunk'] = players["dunk"]
        st.session_state['link'] = players["link"]