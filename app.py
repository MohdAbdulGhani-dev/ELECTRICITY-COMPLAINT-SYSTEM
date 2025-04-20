from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', user_name="Guest")

if __name__ == '__main__':
    app.run(debug=True)