import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import streamlit.components.v1 as components
from utils import get_youtube_videos, get_choro_data


def main():
    display_main_panel()


def display_main_panel():
    if st.session_state['Song'] != '':
        title, author = st.session_state['Song'].split(' - ')
        item = next(filter(lambda x: x['title'] ==
                           title and x['author'] == author, get_choro_data()))
        keys = [key for key in item['melody']
                if item['melody'][key] != '']
        tabs = st.tabs(keys + ['Youtube'])
        for key, tab in zip(keys, tabs[:-1]):
            with tab:
                components.iframe(item['melody'][key], height=1500)

        with tabs[-1]:
            cols = st.columns(3)
            for i, col in enumerate(cols):
                urls = get_youtube_videos(item['title'], item['author'])
                with col:
                    components.iframe(urls[i], height=300)


if __name__ == '__main__':
    main()
