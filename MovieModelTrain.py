import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load movie data
movies = pd.read_csv("data/ml-32m/movies.csv")

# Use TF-IDF to process genres
tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(movies["genres"].fillna(""))

# Compute similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Save the model
with open("movie_recommendation_model.pkl", "wb") as file:
    pickle.dump(cosine_sim, file)

print("Model trained and saved successfully!")
    