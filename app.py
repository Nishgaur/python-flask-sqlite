from flask import Flask, jsonify

app = Flask(__name__)

bestselling_novels = [
    {"year": 2023, "title": "The Testaments", "author": "Margaret Atwood"},
    {"year": 2023, "title": "Where the Crawdads Sing", "author": "Delia Owens"},
    {"year": 2023, "title": "The Silent Patient", "author": "Alex Michaelides"},
    {"year": 2023, "title": "The Institute", "author": "Stephen King"},
    {"year": 2023, "title": "The Dutch House", "author": "Ann Patchett"},
    {"year": 2002, "title": "A tale of two cities", "author": "Ruskin Bond"},
    {"year": 2008, "title": "Sherlock Holmes", "author": "Arthur Conan Doyle"},
    {"year": 2018, "title": "The Murder on Orient Express", "author": "Agatha Cristie"},
    {"year": 2020, "title": "The Ancient Temple", "author": "Sudha Murty"},
    
]

@app.route('/bestselling-novels', methods=['GET'])
def get_bestselling_novels():
    return jsonify(bestselling_novels)

if __name__ == '__main__':
    app.run(debug=True)
