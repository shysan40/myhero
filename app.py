from flask import Flask, Response, render_template

app = Flask(__name__)

@app.route('/')
def greet():
    return "Welcome ..."

@app.route('/health')
def health():
    return "Doing good!"

@app.errorhandler(404)
def my404handler(error):
    return render_template('error.html', errorCode="404", message=error.description), 404

if __name__=="__main__":
    app.run(host='0.0.0.0', port=26026)
