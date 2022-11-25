from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def home():
    return render_template('index.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/pythonPortfolio.html')
def python():
    return render_template('pythonPortfolio.html')

@app.route('/webPortfolio.html')
def web():
    return render_template('webPortfolio.html')

if __name__ == "__main__":
    app.run(debug=True)
