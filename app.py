from flask import Flask, render_template, request
import pickle
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

app = Flask(__name__)

# Load saved model and data
knn = pickle.load(open('model/knn_model.pkl', 'rb'))
vectorizer = pickle.load(open('model/tfidf_vectorizer.pkl', 'rb'))
df = pd.read_csv('model/final_indian_food.csv')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ingredients = request.form['ingredients']

        # Vectorize input
        sample_vector = vectorizer.transform([ingredients])

        print(f"Number of features in the vectorizer: {len(vectorizer.get_feature_names_out())}")
        print("User input ingredients:", ingredients)
        print("Length of vectorized input:", vectorizer.transform([ingredients]).shape)


        # Predict category
        predicted_category = knn.predict(sample_vector)[0]

        # # Filter dataframe
        filtered_df = df[df['recipe_category'] == predicted_category]
        filtered_vectors = vectorizer.transform(filtered_df['ingredients'])

        # # Cosine similarity
        cos_sim = cosine_similarity(sample_vector, filtered_vectors)
        top_indices = np.argsort(cos_sim[0])[::-1][:5]
        top_recipes_df = filtered_df.iloc[top_indices][['name', 'prep_time', 'cook_time', 'diet', 'ingredients', 'flavor_profile', 'course', 'state']]
        top_recipes = top_recipes_df.to_dict(orient='records')
        return render_template('results.html', recipes=top_recipes, category=predicted_category)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
