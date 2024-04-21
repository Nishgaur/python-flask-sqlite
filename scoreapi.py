from flask import Flask, jsonify

app = Flask(__name__)

student_scores = [
    {"Student_name": "Margaret Atwood", "Sub_name": "Computer", "Marks": 20},
    {"Student_name": "Delia Owens", "Sub_name": "Computer", "Marks": 23},
    {"Student_name": "Alex Michaelides", "Sub_name": "Computer", "Marks": 22},
    {"Student_name": "Stephen King", "Sub_name": "Computer", "Marks": 21},
    {"Student_name": "Ann Patchett", "Sub_name": "Computer", "Marks": 43},
    {"Student_name": "Ruskin Bond", "Sub_name": "Computers", "Marks": 32},
    {"Student_name": "Arthur Conan Doyle", "Sub_name": "Computer", "Marks": 49},
    {"Student_name": "Agatha Cristie", "Sub_name": "Computer", "Marks": 18},
    {"Student_name": "Sudha Murty", "Sub_name": "Computer", "Marks": 50},
    {"Student_name": "Margaret Atwood", "Sub_name": "Science", "Marks": 24},
    {"Student_name": "Delia Owens", "Sub_name": "Science", "Marks": 26},
    {"Student_name": "Alex Michaelides", "Sub_name": "Science", "Marks": 28},
    {"Student_name": "Stephen King", "Sub_name": "Science", "Marks": 29},
    {"Student_name": "Ann Patchett", "Sub_name": "Science", "Marks": 47},
    {"Student_name": "Ruskin Bond", "Sub_name": "Science", "Marks": 31},
    {"Student_name": "Arthur Conan Doyle", "Sub_name": "Science", "Marks": 42},
    {"Student_name": "Agatha Cristie", "Sub_name": "Science", "Marks": 19},
    {"Student_name": "Sudha Murty", "Sub_name": "Computer", "Marks": 12}
]

@app.route('/student_scores', methods=['GET'])
def get_student_scores():
    return jsonify(student_scores)

if __name__ == '__main__':
    app.run(debug=True)
