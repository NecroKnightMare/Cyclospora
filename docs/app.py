from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    # Run the game script and capture the output
    result = subprocess.run(['python', 'game.py'], capture_output=True, text=True)
    game_output = result.stdout  # Capture the game output

    # Render the HTML template and pass the game output to it
    return render_template('index.html', game_output=game_output)

if __name__ == '__main__':
    app.run(debug=True)
