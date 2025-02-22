from flask import Blueprint, render_template, request, redirect, url_for
from models.quiz_model import db, Quiz, UserResponse

quiz_bp = Blueprint('quiz', __name__)

# Fetch quiz questions from DB
@quiz_bp.route('/')
def quiz():
    quizzes = Quiz.query.all()
    return render_template('quiz.html', quizzes=quizzes)

# Submit quiz and evaluate score
@quiz_bp.route('/submit', methods=['POST'])
def submit_quiz():
    score = 0
    total_questions = Quiz.query.count()

    for quiz in Quiz.query.all():
        user_answer = request.form.get(f"q{quiz.id}")
        if user_answer == quiz.answer:
            score += 1

    recommendation = recommend_content(score, total_questions)
    return render_template('result.html', score=score, total_questions=total_questions, recommendation=recommendation)

# Recommendation logic based on performance
def recommend_content(score, total_questions):
    if score == total_questions:
        return "Great job! Here are some advanced topics: [Advanced Topic 1, Advanced Topic 2]"
    elif score >= total_questions / 2:
        return "Good effort! Try these intermediate topics: [Intermediate Topic 1, Intermediate Topic 2]"
    else:
        return "Start with these basics: [Beginner Topic 1, Beginner Topic 2]"
