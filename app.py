from flask import Flask, render_template, request

app = Flask(__name__, template_folder= 'template')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    if not request.form.get('name') or request.form.get("sport") not in ['Football', 'Swimming', 'Baseball']:
        return render_template('failure.html')

    return render_template('Success.html')
    if __name__ == "__main__":
        app.run()