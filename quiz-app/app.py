from flask import Flask, render_template, request, redirect, url_for
from firebase_setup import store_result
from quiz_data import quiz_questions

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        score = 0
        total = len(quiz_questions)
        answers = request.form.to_dict()
        
        for q_id, q_data in quiz_questions.items():
            if answers.get(q_id) == q_data['correct']:
                score += 1
        
        store_result("Ghamzaki", score, total)
        return redirect(url_for('result', score=score, total=total))

    return render_template('quiz.html', questions=quiz_questions)

@app.route('/result')
def result():
    score = request.args.get('score')
    total = request.args.get('total')
    return render_template('result.html', score=score, total=total)

if __name__ == '__main__':
    app.run(debug=True)
