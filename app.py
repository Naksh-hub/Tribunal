from flask import Flask, render_template, request
import os
import random

app = Flask(__name__)

# HOME ROUTE
@app.route('/')
def home():
    return render_template('index.html')


# ANALYZE ROUTE
@app.route('/analyze', methods=['POST'])
def analyze():
    # GET DATA FROM FORM
    topic = request.form.get('topic', '')
    teamA = request.form.get('teamA', 'Team A')
    teamB = request.form.get('teamB', 'Team B')
    arg1 = request.form.get('argument1', '')
    arg2 = request.form.get('argument2', '')

    # BASIC SCORING (word count)
    scoreA = len(arg1.split())
    scoreB = len(arg2.split())

    # DECIDE WINNER
    if scoreA > scoreB:
        winner = teamA + " (FOR)"
    elif scoreB > scoreA:
        winner = teamB + " (AGAINST)"
    else:
        winner = "It's a Tie"

    # AI-STYLE EXPLANATION (SIMULATED)
    explanations = [
        f"{teamA} demonstrated stronger logical structure and clearer argument development.",
        f"{teamB} presented more persuasive reasoning and handled rebuttals effectively.",
        "Both teams performed competitively, but one side lacked depth in critical analysis.",
        f"{teamA} maintained clarity and consistency, giving them a slight advantage.",
        f"{teamB} showed better engagement with opposing arguments and stronger rebuttal."
    ]

    explanation = random.choice(explanations)

    # RETURN RESULT
    return render_template(
        'index.html',
        result=winner,
        topic=topic,
        explanation=explanation,
        teamA=teamA,
        teamB=teamB,
        scoreA=scoreA,
        scoreB=scoreB
    )


# RUN APP (IMPORTANT FOR RAILWAY)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)