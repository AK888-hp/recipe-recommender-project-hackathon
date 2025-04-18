#### Recipe Recommendation System
An AI-powered recipe predictor that recommends Indian dishes based on ingredients and recipe attributes. Built using Flask, KNN, and a custom Indian food dataset.

### Features
Predicts recipes based on input ingredients

Uses K-Nearest Neighbors classifier

Combines region, state, diet, course, and flavor_profile into a single recipe category

Simple web interface using Flask


### Tech Stack
Backend: Flask

ML Model: Scikit-learn (KNN)

Language: Python

Dataset: Custom Indian food dataset (CSV)


###  Setup Instructions
## Clone the repo

git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name

## Create a virtual environment

python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate

## Install dependencies

pip install -r requirements.txt

## Run the app

flask run

### Project Structure
├── app.py
├── model/
│   └── knn_model.pkl
├── templates/
│   └── index.html
├── static/
│   └── styles.css
├── data/
│   └── indian_food.csv
├── requirements.txt
├── .env.example
└── README.md

### Dataset Info
The dataset includes:

Ingredients (list of ingredients)

Prep Time / Cook Time

Diet, Region, State, Course, Flavor Profile

Target: Recipe Name (converted to categorical for classification)
