import streamlit as st
import streamlit.components.v1 as components
from utils import get_choro_data, get_youtube_videos, search_bar
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    layout="wide",
    page_title="Choro Library"
)


def main():
    main_container = st.empty()

    with main_container.container():
        matches = search_bar()
        display_main_panel(matches)

    with st.sidebar:
        if st.button("Back to list"):
            reset(main_container)


def reset(main_container):
    main_container.empty()


def display_main_panel(matches):
    cols = st.columns(3)
    for index, match in enumerate(matches):
        if cols[index % 3].button(match, use_container_width=True):
            st.session_state['Song'] = match
            switch_page("Song")


if __name__ == '__main__':
    main()
