
from flask import Flask
import random

print(__name__)
app = Flask(__name__)

@app.route('/')
def index():
    lastname = "Newman"
    firstname = "Mark"
    return f'''
        <h1>My name is {firstname} {lastname}!</h1>
        Go to: <a href='/about'>about</a> <a href='/lucky'>lucky</a>
    '''

@app.route('/about')
def about():
    course = 'SI 507'
    semester = 'Winter 2020'
    html = f'''
        <h1>
            This app was created in {semester} for {course}.
        </h1>
        <p>
            Return <a href='/'>home</a>.
        </p>
    '''
    return html

@app.route('/lucky')
def lucky():
    lucky_num = random.randint(0, 100)
    html = f'''
        <h1>
            Your lucky number is {lucky_num}
        </h1>
        <img src="https://media.giphy.com/media/yaYV8i5n1OjZe/giphy.gif"/>
        <p>
            Return <a href='/'>home</a>.
        </p>
    '''
    return html

if __name__ == '__main__':  
    print('starting Flask app', app.name)  
    app.run(debug=True)