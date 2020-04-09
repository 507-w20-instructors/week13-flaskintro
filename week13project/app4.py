from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    m = "April"
    d = 9
    return render_template('index2.html', 
        month=m, day=d)

@app.route('/about')
def about():
    fname = "Mark"
    lname = "Newman"

    return render_template('about.html', 
        first_name=fname, 
        last_name=lname)

@app.route('/flip')
def flip():
    result = random.random() > 0.5
    return render_template('flip.html', 
        flip=result)
        
if __name__ == '__main__':  
    app.run(debug=True)