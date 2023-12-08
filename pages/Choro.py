import streamlit as st
import streamlit.components.v1 as components
from streamlit_searchbox import st_searchbox
from utils import get_choro_data, get_youtube_videos, search_bar

st.set_page_config(
    layout="wide",
    page_title="Choro Library"
)


def main():
    matches = search_bar()
    display_main_panel(matches)


def display_main_panel(matches):
    cols = st.columns(3)
    for index, match in enumerate(matches):
        cols[index % 3].button(match)

# def display_main_panel():
    # if st.session_state['selected_value'] != '':
    #     title, author = st.session_state['selected_value'].split(' - ')
    #     item = next(filter(lambda x: x['title'] ==
    #                        title and x['author'] == author, get_choro_data()))
    #     keys = [key for key in item['melody']
    #             if item['melody'][key] != '']
    #     tabs = st.tabs(keys + ['Youtube'])
    #     for key, tab in zip(keys, tabs[:-1]):
    #         with tab:
    #             components.iframe(item['melody'][key], height=1500)

    #     with tabs[-1]:
    #         cols = st.columns(3)
    #         for i, col in enumerate(cols):
    #             urls = get_youtube_videos(item['title'], item['author'])
    #             with col:
    #                 components.iframe(urls[i], height=300)


if __name__ == '__main__':
    main()
