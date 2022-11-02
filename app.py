from boggle import Boggle
from flask import Flask, session, request, render_template, jsonify
from flask_debugtoolbar import DebugToolbarExtension
import json

boggle_game = Boggle()

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
debug = DebugToolbarExtension(app)
tried = set()
score = 0
timesPlayed = 0

@app.route('/')
def home():
    """Generate board and display"""
    board = boggle_game.make_board()
    session['board'] = board
    global score
    score = 0
    return render_template('home.html', board = board)

@app.route("/guess", methods = ["POST"])
def guessCheck():
    """Check if guess is correct, or used"""
    word = json.loads(request.data)['guess']
    if word in tried:
       res = 'already used' 
    else:
        tried.add(word)
        res = boggle_game.check_valid_word(session['board'], word)
        if res == 'ok':
            global score
            score = score + len(word)
    reply = {'result': res, 'score': score}
    return jsonify(reply)

@app.route("/done", methods = ["POST"])
def done():
    """Game Over"""
    global timesPlayed
    timesPlayed = timesPlayed + 1
    return jsonify({'result':'ok'})
