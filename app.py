from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/comparisons")
def comparisons():
    return render_template("comparisons.html")

@app.route('/max-temp')
def maxTemp():
    return render_template('max-temp.html')

@app.route('/humidity')
def humidity():
    return render_template('humidity.html')

@app.route('/cloudiness')
def cloudiness():
    return render_template('cloudiness.html')

if __name__ == "__main__":
    app.run(debug=True)
