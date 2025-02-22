from flask import Flask, render_template, request

app = Flask(__name__)

# Mock quiz data
quizzes = [
    {"question": "What is 2 + 2?", "options": ["3", "4", "5"], "answer": "4"},
    {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin"], "answer": "Paris"},
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/quiz")  # Ensure this route is defined
def quiz():
    return render_template("quiz.html", quizzes=quizzes)

@app.route("/submit-quiz", methods=["POST"])
def submit_quiz():
    score = 0
    for i, quiz in enumerate(quizzes):
        user_answer = request.form.get(f"q{i}")
        if user_answer == quiz["answer"]:
            score += 1
    return f"Your score is {score}/{len(quizzes)}!"

if __name__ == "__main__":
    app.run(debug=True)