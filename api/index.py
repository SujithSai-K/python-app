from flask import Flask, request, jsonify

app = Flask(__name__)

# Data to simulate marks
marks_list = [
    {"name": "Sp", "marks": 83}, {"name": "NlWE8LA7U", "marks": 66}, {"name": "r6i", "marks": 92},
    {"name": "iGP9B", "marks": 31}, {"name": "IpG5Sa", "marks": 7}, {"name": "fOwD4i2ykR", "marks": 75},
    {"name": "uJFvkA", "marks": 39}, {"name": "wQ", "marks": 70}, {"name": "SC", "marks": 81},
    {"name": "B", "marks": 96}
]

# Helper function to find marks by name
def find_marks(name):
    for entry in marks_list:
        if entry["name"] == name:
            return entry["marks"]
    return 0  # Default if name is not found

@app.route('/api', methods=['GET'])
def get_marks():
    # Extract 'name' parameters from query string
    names = request.args.getlist('name')

    # Find marks for each name
    marks = [find_marks(name) for name in names]

    # Enable CORS by adding the necessary headers
    response = jsonify({"marks": marks})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
