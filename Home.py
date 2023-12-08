import streamlit as st
import streamlit.components.v1 as components
from utils import embed_small_video

st.set_page_config(
    page_title='page1',
    page_icon='📋',
    layout='wide',
    initial_sidebar_state='expanded',
)

st.title('Choro Library')
st.subheader('What you can do')
play, loop, choose = st.tabs(['Play', 'Loop', 'Choose Instrument'])

with play:
    embed_small_video('./assets/gifs/play.webm')


with loop:
    components.iframe('./assets/gifs/play.webm')

with choose:
    components.iframe('./assets/gifs/play.webm')
