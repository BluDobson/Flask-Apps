from flask import Flask, url_for, redirect

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return 'This is the home page'

@app.route('/about')
def about():
    return 'This is the about page'

@app.route('/square')
def square_home():
    return 'Enter a number above 1 at the end of the url'

@app.route('/square/<int:number>')
def square(number):
    if number >= 1:
        ans = number*number
        return str(ans)
    else:
        return redirect(url_for('square_home'))

if __name__ == "__main__":
    app.run(debug=True, host = '0.0.0.0')