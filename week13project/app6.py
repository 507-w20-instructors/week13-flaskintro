from flask import Flask, render_template
import random
import requests

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

@app.route('/beatles')
def beatles():
    names = ['John', 'Paul', 'George', 'Ringo']
    return render_template('beatles.html', 
        beatles=names)


@app.route('/rhyme/<word>')
def find_rhymes(word):
    base_url = 'https://api.datamuse.com/words'
    params = { 'rel_rhy': word }
    results = requests.get(base_url, params).json()
    rhy_words = []
    for r in results:
        rhy_word = r['word']
        rhy_words.append(rhy_word)
    return render_template('rhymes.html', 
        word=word, word_list=rhy_words) 


@app.route('/hello/<nm>')
def hello_name(nm):
    return render_template('hello.html', name=nm)       
        
if __name__ == '__main__':  
    app.run(debug=True)