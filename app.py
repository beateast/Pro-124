from flask import flask, jsonify, request
app = Flask(__name__)

contact = [
    {
        'id': tasks[-1]['id']+1,
        'Name': request.json['name'],
        'Contact': request.json.get['contct'],
        'done': False
    }
]
@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error"
        }
        