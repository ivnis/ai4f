from flask import Flask, render_template, request, jsonify
import g4f

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_message = request.form.get("message")
        try:
            response = g4f.ChatCompletion.create(
                model="gemini-1.5-flash",
                messages=[{"role": "user", "content": user_message}],
            )
            return jsonify({"response": response})
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)