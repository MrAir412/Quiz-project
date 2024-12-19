from flask import Flask, request, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL config

# Connection to database
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='testing123'
app.config['MYSQL_DB']='quiz_db'
mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        score = 0
        user_answers = request.form
        print("User's answers:", user_answers)

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT id, answer FROM quiz")
        correct_answers = cursor.fetchall()
        cursor.close()

        for question_id, correct_answer in correct_answers:
            question_id_str = str(question_id)
            if question_id_str in user_answers and user_answers[question_id_str] == correct_answer:
                score += 1

        print(f"User's score: {score}")
        return render_template('result.html', score=score, total=len(correct_answers))

    else:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT id, question, option_a, option_b, option_c, option_d FROM quiz")
        quiz_data = cursor.fetchall()
        cursor.close()

        return render_template('quiz.html', quiz=quiz_data)

if __name__ == '__main__':
    print("Starting Quiz Application...")
    app.run(debug=True)
