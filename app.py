from flask import Flask, render_template
import subprocess
import os
from cyclospora import start_game  # Import the modified game logic

app = Flask(__name__)

@app.route('/')
def home():
    # Start the game and get the current state
    game_state = start_game()  # This will run the game and return its state
    return render_template('index.html', score=game_state['score'], health=game_state['health'], status=game_state['status'])

if __name__ == '__main__':
    app.run(debug=True)
