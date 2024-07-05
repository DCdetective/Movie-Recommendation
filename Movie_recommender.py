import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster (movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=c2853631f3d726c9e142db5824ea1e9f')
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list =sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommend_movies = []
    recommended_poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommend_movies.append(movies.iloc[i[0]].title)
        recommended_poster.append(fetch_poster((movie_id)))
    return recommend_movies,recommended_poster
similarity = pickle.load(open('similarity.pkl','rb'))

movies_list = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_list)
st.title('Movie Recommender System')

option = st.selectbox('How would u like to connect?',movies['title'].values)
if st.button('Recommend'):
    names,poster = recommend(option)

    col1, col2 , col3 ,col4 , col5 = st.columns(5)
    with col1:
        st.header(names[0])
        st.image(poster[0])
    with col2:
        st.header(names[1])
        st.image(poster[1])
    with col3:
        st.header(names[2])
        st.image(poster[2])
    with col4:
        st.header(names[3])
        st.image(poster[3])
    with col5:
        st.header(names[4])
        st.image(poster[4])