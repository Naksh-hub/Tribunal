from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    topic = request.form.get('topic', '')
    teamA = request.form.get('teamA', 'Team A')
    teamB = request.form.get('teamB', 'Team B')
    arg1 = request.form.get('argument1', '')
    arg2 = request.form.get('argument2', '')

    # Simple scoring logic (we upgrade later)
    scoreA = len(arg1.split())
    scoreB = len(arg2.split())

    if scoreA > scoreB:
        winner = teamA + " (FOR)"
    elif scoreB > scoreA:
        winner = teamB + " (AGAINST)"
    else:
        winner = "It's a Tie"

    return render_template(
        'index.html',
        result=winner,
        topic=topic,
        teamA=teamA,
        teamB=teamB,
        scoreA=scoreA,
        scoreB=scoreB
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)