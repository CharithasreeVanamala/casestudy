from flask import Flask, render_template, request

app = Flask(__name__)

# Predefined student list
students = ["Alice", "Bob", "Charlie", "David", "Emma"]

@app.route('/')
def home():
    return render_template('index.html', students=students)

@app.route('/attendance', methods=['POST'])
def attendance():
    present_students = request.form.getlist('present')
    total = len(students)
    present_count = len(present_students)
    absent_count = total - present_count

    return render_template('result.html',
                           students=students,
                           present_students=present_students,
                           total=total,
                           present=present_count,
                           absent=absent_count)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

