from flask import Flask, request, jsonify, render_template
import requests
import context 

app = Flask(__name__)

API_KEY = "68c85b3d590a26a86f95673690aae8f9b6a30613dcf133ba170e84652353acee"
TOGETHER_URL = "https://api.together.xyz/v1/completions"

context_data = context.context_data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.json['message']

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = (
        "You are an admission assistant chatbot for Superior University. "
        "Use the following university admission data to answer the user's question clearly and concisely. Answers should be very short.\n\n"
        f"ADMISSION DATA:\n{context_data}\n\n"
        f"User: {user_input}\nAssistant:"
    )

    payload = {
        "model": "meta-llama/Llama-3-8b-chat-hf",
        "prompt": prompt,
        "max_tokens": 300,
        "temperature": 0.7,
        "top_p": 0.9,
        "stop": ["User:", "Assistant:"]
    }

    try:
        response = requests.post(TOGETHER_URL, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        reply = data["choices"][0]["text"].strip()
        return jsonify({"response": reply})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"response": "Sorry, I couldn't connect to the AI server."})

if __name__ == '__main__':
    app.run(debug=True)
