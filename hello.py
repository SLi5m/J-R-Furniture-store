from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/showroom/')
def showroom():
    return render_template('showroom.html')

@app.route('/contact/')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug = True)