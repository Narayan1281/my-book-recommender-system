from flask import Flask, render_template, request
import pandas as pd
import numpy as np

# Loading the pre-processed csv files
popular_df = pd.read_csv('popular_books.csv')
pt = pd.read_csv('dump_pivot_table.csv',index_col='Book-Title')
similarity_score = pd.read_csv('dump_similarity_scores.csv')
books = pd.read_csv('dump_books.csv')

title = pt.index
title = list(title)

app = Flask(__name__)

# ------------------------------- Home Page of Book-Recommender system ---------------------

@app.route('/')
def index():
    return render_template('index.html',
                            book_name = list(popular_df['Book-Title'].values),
                            author = list(popular_df['Book-Author'].values),
                            image = list(popular_df['Image-URL-M'].values),
                            votes = list(popular_df['count_of_ratings'].values),
                            rating = list(popular_df['avg_ratings'].values),
                            )

# ----------------------------- Taking User Input ---------------------

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html',
                            book_title=title,
                            argument = 0,
                            data = 0
                            )


# ---------------------------------- Recommmendation Generation ------------------

@app.route('/recommend_books', methods=['post'])
def recommend_books():
    book_name = request.form.get('user_input')
    # fetch index
    index1 = np.where(pt.index==book_name)[0]
    if(len(index1)==0):
        return render_template('recommend.html',
                            book_title=title,
                            argument = 0,
                            data = 0,
                            book_name = book_name,
                            not_found = 1
                            )
    index = index1[0]
    similar_items = sorted(list(enumerate(list(similarity_score.iloc[index]))), key=lambda x:x[1], reverse=True)[1:8]
    # we shall show 7 recommendation based on the given book_name
    data = []
    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title']==pt.index[i[0]]].drop_duplicates('Book-Title')
        item.append(temp_df['Book-Title'].values[0])
        item.append(temp_df['Book-Author'].values[0])
        item.append(temp_df['Image-URL-M'].values[0])
        
        data.append(item)
    return render_template('recommend.html',
                            book_title=title,
                            argument = 1,
                            data = data
                            )

# ------------------------------ About Page ------------------------
@app.route('/about')
def about():
    return render_template('recommend.html',
                            about = 1
                            )


if __name__ == "__main__":
    app.run(debug=True)