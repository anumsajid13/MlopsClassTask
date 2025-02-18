from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Deploying Lab Task at Vercel- 21i-1145"

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))  # Use Vercel's PORT environment variable
    app.run(host="0.0.0.0", port=port)
