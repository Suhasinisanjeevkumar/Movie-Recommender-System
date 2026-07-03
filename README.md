# Project: Movie Recommender System Using Machine Learning!

<img src="demo/6.jpeg" alt="workflow" width="70%">

# 🎬 Movie Recommender System Using Machine Learning

A content-based movie recommendation system built using Python and Machine Learning techniques. This project suggests movies similar to the one selected by the user based on features like genres, cast, crew, and overview.

---

## 🚀 Project Overview

This system uses Natural Language Processing (NLP) and similarity scoring to recommend movies. It analyzes movie metadata and computes similarity between movies to suggest the most relevant ones.

---

## 🧠 How It Works

1. Dataset containing movie details is preprocessed.
2. Important features like **genres, keywords, cast, crew, and overview** are combined.
3. Text data is converted into vectors using **CountVectorizer / TF-IDF**.
4. Similarity is calculated using **cosine similarity**.
5. Based on user input, top similar movies are recommended.

---

## 🛠️ Tech Stack

- Python 
- Pandas
- NumPy
- Scikit-learn
- Natural Language Processing (NLP)
- Flask / Streamlit
- VS code

---

## 📂 Project Structure
         

# About this project:

This is a streamlit web application that can recommend various kinds of similar movies based on an user interest.
here is a demo,



# Demo:

<img src="demo/1.png" alt="workflow" width="70%">

<img src="demo/2.png" alt="workflow" width="70%">

<img src="demo/3.png" alt="workflow" width="70%">


# Dataset has been used:

* [Dataset link](https://www.kaggle.com/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv)

# Concept used to build the model.pkl file : cosine_similarity

1 . Cosine Similarity is a metric that allows you to measure the similarity of the documents.

2 . In order to demonstrate cosine similarity function we need vectors. Here vectors are numpy array.

3 . Finally, Once we have vectors, We can call cosine_similarity() by passing both vectors. It will calculate the cosine similarity between these two.

4 . It will be a value between [0,1]. If it is 0 then both vectors are complete different. But in the place of that if it is 1, It will be completely similar.

5 . For more details , check URL : https://www.learndatasci.com/glossary/cosine-similarity/

# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/entbappy/Movie-Recommender-System-Using-Machine-Learning.git
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n movie python=3.7.10 -y
```

```bash
conda activate movie
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
#run this file to generate the models

Movie Recommender System Data Analysis.ipynb
```

Now run,
```bash
streamlit run app.py
```


```bash
Author: Suhasini


```
