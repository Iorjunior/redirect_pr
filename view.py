from flask import Flask, redirect
import os

app = Flask(__name__)


@app.route('/')
def home():
    return redirect("https://promaxima.com.br/", code=302)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8000))
    app.run(debug=True, host='0.0.0.0', port=port)