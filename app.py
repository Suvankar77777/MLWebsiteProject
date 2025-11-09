from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

def generate_recommendations(df):
    # Example placeholder — replace this with your logic from the notebook
    # For demo: show top 5 hobbies by frequency
    hobby_cols = [col for col in df.columns if "Hobby" in col]
    hobbies = pd.concat([df[col] for col in hobby_cols], axis=0)
    top_hobbies = hobbies.value_counts().head(5).to_dict()
    return top_hobbies

@app.route("/", methods=["GET", "POST"])
def index():
    recommendations = None
    if request.method == "POST":
        file = request.files["file"]
        if file:
            df = pd.read_csv(file)
            recommendations = generate_recommendations(df)
    return render_template("index.html", recommendations=recommendations)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
