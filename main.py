from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Home</h1>"

@app.route("/get-game/<game_id>")
def get_game(game_id):
    game_data = {
        "game_id": game_id,
        "title": "Balatro",
        "developer": "LocalThunk"
    }

    extra = request.args.get("extra")
    if extra:
        game_data["extra"] = extra

    return jsonify(game_data), 200

if __name__ == "__main__":
    app.run(debug=True)
