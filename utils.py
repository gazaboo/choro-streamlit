import streamlit as st
import rapidfuzz
from rapidfuzz.fuzz import partial_ratio
import json
from youtube_search import YoutubeSearch
from st_keyup import st_keyup


@st.cache_data
def get_choro_data():
    f = open('./liste_totale_choros.json')
    return json.load(f)['data']


@st.cache_data
def get_choro_data_simple_name():
    f = get_choro_data()
    simple_names = list(map(
        lambda x: x['title'] + ' - ' + x['author'], get_choro_data()))
    return simple_names


@st.cache_data
def get_youtube_videos(title, author):
    query = ' '.join([title, author, 'choro'])
    results = YoutubeSearch(query, max_results=3).to_dict()
    base_url = 'https://www.youtube.com/embed/'
    urls = [base_url + result['id'] for result in results]
    return urls


def search_bar():
    data = get_choro_data_simple_name()
    query = st_keyup("Search here")
    if query != '':
        ranking = rapidfuzz.process.extract(
            query, data, scorer=partial_ratio, limit=None)
        ranked_names = [item[0] for item in ranking]
        return ranked_names
    return data


def embed_small_video(url):
    _, container, _ = st.columns([20, 60, 20])
    video_file = open(url, 'rb')
    video_bytes = video_file.read()
    container.video(data=video_bytes)
    # st.video(video_bytes)


def set_style():
    st.markdown("""
        <style>
               .block-container {
                    z-index:1000000;
                    padding-top: 4rem;
                }
        </style>
        """, unsafe_allow_html=True)


# def reset_state():
#     st.empty()
#     st.session_state['selected_value'] = ''


# st.button(
#     label='back',
#     on_click=reset_state
# )
