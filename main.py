import pandas as pnd
import streamlit as st
import requests
import pickle

movies = pickle.load(open('movies.pkl', 'rb'))
movies = pnd.DataFrame(movies)
sim_score = pickle.load(open('sim_score (1).pkl', 'rb'))


def recommend(movie):
    index_of_m = movies[movies['title'] == movie].index[0]
    return sorted(list(enumerate(sim_score[index_of_m])), reverse=True, key=lambda i: i[1])[1:6]


st.header("Movie Recommendation System")
movie_inp = st.selectbox(
    'Select a movie from the list below',
    movies['title'].values)



def getPos(movie):
    api_ = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=319eb1d8611d9add12276df81486e0f0'.format(movie))
    apiPost = api_.json()

    if 'success' in apiPost:
        if apiPost['success'] == False:
            return None

    return 'https://image.tmdb.org/t/p/w500/' + apiPost['poster_path']


if st.button("Recommend Movies"):
    st.write('recommended movies')
    movies_list = []
    m_posters = []
    for i in recommend(movie_inp):
        movies_list.append(movies.iloc[i[0]]['title'])
        m_posters.append(getPos(movies.iloc[i[0]]['movie_id']))
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        # if m_posters[0] is not None:
        st.image(m_posters[0])
        st.write(movies_list[0])
    with col2:
        # if m_posters[1] is not None:
        st.image(m_posters[1])
        st.write(movies_list[1])
    with col3:
        # if m_posters[2] is not None:
        st.image(m_posters[2])
        st.write(movies_list[2])
    with col4:
        # if m_posters[3] is not None:
        st.image(m_posters[3])
        st.write(movies_list[3])
    with col5:
        st.image(m_posters[4])
        st.write(movies_list[4])

if st.button("Connect with the developer"):
    st.write("Roshan Kumar ","https://www.linkedin.com/in/roshan-kumar-b8b6b91a1/")
