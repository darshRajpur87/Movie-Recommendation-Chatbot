from flask import Flask, request, jsonify, render_template
import pandas as pd
import os
import random  # ← import random

app = Flask(__name__)

# Ensure the templates directory exists
TEMPLATE_DIR = os.path.join(os.getcwd(), "templates")
if not os.path.exists(TEMPLATE_DIR):
    os.makedirs(TEMPLATE_DIR)

# Load the dataset safely
MOVIES_CSV_PATH = r"E:\Aiml_Miniproject\data\Movies_reco_data.csv"

try:
    movies_df = pd.read_csv(MOVIES_CSV_PATH)
    print("✅ Movie dataset loaded successfully.")
except FileNotFoundError:
    print("❌ Error: movies.csv file not found.")
    movies_df = None

# Home page route
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def recommend():
    if movies_df is None:
        return jsonify({"error": "Movie dataset not loaded."}), 500

    data = request.get_json()
    genre = data.get("genre", "").strip().lower()

    if not genre:
        return jsonify({"error": "Please provide a genre or movie name."}), 400

    if "genre" not in movies_df.columns or "title" not in movies_df.columns:
        return jsonify({"error": "Required columns not found in dataset."}), 500

    # Filter movies based on genre
    filtered_movies = movies_df[movies_df["genre"].str.contains(genre, case=False, na=False)]

    if filtered_movies.empty:
        return jsonify({"error": "No matching movies found. Try another genre or keyword."}), 404

    # Optional: sort by rating if available
    if "rating" in filtered_movies.columns:
        filtered_movies = filtered_movies.sort_values(by="rating", ascending=False)

    # Shuffle the filtered results to get a different sample each time
    shuffled_movies = filtered_movies.sample(frac=1, random_state=random.randint(1, 10000))

    # Get top 5 random recommendations
    recommendations = shuffled_movies["title"].tolist()[:5]

    return jsonify({"recommendations": recommendations})

if __name__ == "__main__":
    app.run(debug=True)
