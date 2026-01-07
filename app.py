from flask import Flask, render_template, request, jsonify
from summarizer import summarize_text

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.get_json(force=True)
    text = data.get("text", "")
    summary = summarize_text(text)
    return jsonify({"summary": summary})

if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(host="127.0.0.1", port=5000, debug=True)
