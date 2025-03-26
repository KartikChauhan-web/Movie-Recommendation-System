import pandas as pd
import streamlit as st
import pickle

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    movies_list = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies=[]
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

movie_dict=pickle.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movie_dict)
similarity=pickle.load(open('similarity.pkl','rb'))
st.title('Movie Recommender System')
selected_movie=st.selectbox('Select a movie:',(movies['title'].values))
if st.button('Recommend'):
    recommendations=recommend(selected_movie)
    for i in recommendations:
        st.write(i)
