
from flask import Flask

print(__name__)
app = Flask(__name__)

@app.route('/')
def index():
    lastname = "Newman"
    firstname = "Mark"
    return f'<h1>Hello {firstname} {lastname}!</h1>'

@app.route('/about')
def about():
    course = 'SI 507'
    semester = 'Winter 2020'

    html = f'''
        <p>
            This app was created in {semester} for {course}.
        </p>
        <p>
            Return <a href='/'>home</a>.
        </p>
    '''
    return html


if __name__ == '__main__':  
    print('starting Flask app', app.name)  
    app.run(debug=True)