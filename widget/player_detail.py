import streamlit as st

def get_player_detail():
    img = st.image(st.session_state['dunk'], width=200)
    link = st.session_state['link']
    link_html = f'<a href="{link}"><img src="{img}"></a>'
    st.markdown(link_html, unsafe_allow_html=True)

    # 실패