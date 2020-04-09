from flask import Flask, render_template

app = Flask(__name__)

@app.route('/about')
def about():
    fname = "Mark"
    lname = "Newman"

    return render_template('about.html', 
        first_name=fname, 
        last_name=lname)

if __name__ == '__main__':  
    app.run(debug=True)