from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'rishabh-secret'

@app.route('/')
def index():
    return render_template('index.html',
                           score1=session.get('score1', 0),
                           score2=session.get('score2', 0),
                           rolls_p1=session.get('rolls_p1', []),
                           rolls_p2=session.get('rolls_p2', []),
                           turn=session.get('turn', 'player1'),
                           result=session.get('result', None)
                          )

@app.route('/roll/<player>')
def roll(player):
    if 'score1' not in session:
        session['score1'] = 0
        session['score2'] = 0
        session['rolls_p1'] = []
        session['rolls_p2'] = []
        session['turn'] = 'player1'
        session['result'] = None

    roll = random.randint(1, 6)

    if player == 'player1' and session['turn'] == 'player1':
        session['score1'] += roll
        session['rolls_p1'].append(roll)
        if roll == 1:
            session['turn'] = 'player2'
    elif player == 'player2' and session['turn'] == 'player2':
        session['score2'] += roll
        session['rolls_p2'].append(roll)
        if roll == 1:
            # Game ends here
            if session['score1'] > session['score2']:
                session['result'] = 'Player 1 Wins! 🏆'
            elif session['score2'] > session['score1']:
                session['result'] = 'Player 2 Wins! 🏆'
            else:
                session['result'] = 'Game Draw 🤝'

    return redirect(url_for('index'))

@app.route('/reset')
def reset():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
