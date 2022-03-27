from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return'<h1>Hello DevOps Classroom</h1>'

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/user/<name>')
def user(name):
    return f'<h1>Welcome, {name}!</h1>'