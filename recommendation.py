import pandas as pd
import pickle

# Load dataset
MOVIES_CSV_PATH = r"E:\Aiml_Miniproject\data\Movies_reco_data.csv"
MODEL_PATH = r"E:\Aiml_Miniproject\models\movie_recommendation_model.pkl"

try:
    movies_df = pd.read_csv(MOVIES_CSV_PATH)
    print("✅ Movie dataset loaded successfully.")
except FileNotFoundError:
    print("❌ Error: Movies_reco_data.csv file not found.")
    movies_df = None

# Load trained recommendation model
try:
    with open(MODEL_PATH, "rb") as file:
        cosine_sim = pickle.load(file)
    print("✅ Model loaded successfully.")
except FileNotFoundError:
    print("❌ Error: movie_recommendation_model.pkl file not found.")
    cosine_sim = None

# Recommendation function based on Genre and Ratings
def recommend_movies(genre):
    if movies_df is None:
        return ["❌ Error: Movie dataset not loaded."]
    
    # Check if required columns exist
    required_columns = {"Genre", "Rating", "Title"}
    if not required_columns.issubset(movies_df.columns):
        return ["❌ Error: Required columns ('Genre', 'Rating', 'Title') not found in dataset."]
    
    # Ensure "Rating" is numeric
    movies_df["Rating"] = pd.to_numeric(movies_df["Rating"], errors="coerce")

    # Filter movies by genre (case insensitive)
    genre_filtered = movies_df[movies_df["Genre"].str.contains(genre, case=False, na=False)]

    if genre_filtered.empty:
        return ["⚠️ No movies found for this genre. Try another one!"]

    # Sort by rating (highest to lowest) and return top 5 movies
    top_movies = genre_filtered.sort_values(by="Rating", ascending=False).head(5)["Title"].tolist()
    
    return top_movies if top_movies else ["⚠️ No movies found for this genre. Try another one!"]

# Test the function
print(recommend_movies("Action"))
