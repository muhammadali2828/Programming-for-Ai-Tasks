from flask import Flask, render_template, request, jsonify
from faiss_idx import get_answer

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get", methods=["POST"])
def chatbot_response():
    user_input = request.json.get("message" , "").strip()
    if not user_input:
        return jsonify({"response": "Please enter a message."})

    response = get_answer(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
