from flask import Flask, jsonify, request

app = Flask(__name__)

DATA = [
    {"id":1,"campus":"MMC","lat":25.76,"lon":-80.36},
    {"id":2,"campus":"BBC","lat":25.90,"lon":-80.13},
    {"id":3,"campus":"DC","lat":38.89,"lon":-77.01}
]

next_id = 4

@app.route("/")
def index():
    return """
    <h1>FIU Campuses API</h1>"
    <p> Try these endpoints:</p>
    <ul>
        <li><a href="/api/hello">/api/hello</a></li>
        <li><a href="/api/data">/api/data</a></li>
    </ul>
    """

@app.route("/api/hello")
def hello():
    return jsonify({"Welcome": "This app provides sample campus data for CIS 3590."})

@app.route("/api/data", methods=["GET", "POST"])
def data():
    global next_id
    if request.method == "GET":
        return jsonify(DATA)
    if request.method == "POST":
        new_item = request.get_json()
        if not new_item:
            return jsonify({"error": "Invalid JSON"}), 400
        new_item["id"] = next_id
        next_id += 1
        DATA.append(new_item)
        return jsonify({"status": "created", "data": new_item}), 201

if __name__ == "__main__":
    app.run(debug=True)

