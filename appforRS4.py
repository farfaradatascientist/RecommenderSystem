import streamlit as st
import pickle
import pandas as pd



def recommend(book):
    index = books[books['Name'] == book].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_book_names = []
    recommended_book_posters = []
    for i in distances[1:10]:
        recommended_book_names.append(books.iloc[i[0]].Name)
        recommended_book_posters.append(books.iloc[i[0]].Images)

    return recommended_book_names,recommended_book_posters




books_dict = pickle.load(open("Books_dict.pkl","rb"))
books = pd.DataFrame(books_dict)
similarity = pickle.load(open("similarity.pkl","rb"))
book_list = books['Name'].values

st.title("Book Recommender System")
Selected_Book = st.selectbox(
"Select Your Favorite Book: ",
book_list
)


if st.button("Recommend"):
    names,posters = recommend(Selected_Book)
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs(["1","2","3","4","5","6","7","8","9"])
    with tab1:
        st.text(names[0])
        st.image(posters[0],width = 200)
    with tab2:
        st.text(names[1])
        st.image(posters[1],width = 200)
    with tab3:
        st.text(names[2])
        st.image(posters[2],width = 200)
    with tab4:
        st.text(names[3])
        st.image(posters[3],width = 200)
    with tab5:
        st.text(names[4])
        st.image(posters[4],width = 200)
    with tab6:
        st.text(names[5])
        st.image(posters[5],width = 200)
    with tab7:
        st.text(names[6])
        st.image(posters[6],width = 200)
    with tab8:
        st.text(names[7])
        st.image(posters[7],width = 200)
    with tab9:
        st.text(names[8])
        st.image(posters[8],width = 200)
