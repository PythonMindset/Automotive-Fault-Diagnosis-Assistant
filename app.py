from flask import Flask, render_template, request
from modals.bot import get_similar_query
from modals.main import ask_gemini_with_history

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form["query"]

        try:
            answer = ask_gemini_with_history(user_input)

        except Exception as e:
            answer = f"An error occurred: {str(e)}"

        return render_template("result.html",user_input=user_input,answer=answer)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
