from flask import Flask, render_template, request, jsonify
import random
import os

app = Flask(__name__)

# Emoji mapping for emotions
emoji_map = {
    "laughing child.webp": "😂",
    "sad face.jpeg": "😢",
    "angry person.jpeg": "😡",
    "surprised person.jpeg": "😲"
}

@app.route('/')
def index():
    images = list(emoji_map.keys())
    selected_image = random.choice(images)
    correct_emoji = emoji_map[selected_image]

    return render_template("index.html", captcha={"image": selected_image, "correct_emoji": correct_emoji})

@app.route('/validate', methods=['POST'])
def validate():
    data = request.get_json()
    user_emoji = data.get("emoji")
    correct_emoji = data.get("correct_emoji")

    if user_emoji == correct_emoji:
        return jsonify({"success": True, "message": "✅ Correct! Good job!"})
    else:
        return jsonify({"success": False, "message": "❌ Wrong! Try again."})

if __name__ == '__main__':
    app.run(debug=True)
