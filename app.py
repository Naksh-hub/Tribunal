from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    party_a = request.form['party_a']
    party_b = request.form['party_b']

    words_a = party_a.split()
    words_b = party_b.split()
    count_a = len(words_a)
    count_b = len(words_b)

    strong_words = ["must", "definitely", "clearly", "strong", "important", "critical", "believe", "undeniable"]
    strong_a = sum(word.lower() in strong_words for word in words_a)
    strong_b = sum(word.lower() in strong_words for word in words_b)

    score_a = count_a + (2 * strong_a)
    score_b = count_b + (2 * strong_b)

    if score_a > score_b:
        winner = "Party A"
    elif score_b > score_a:
        winner = "Party B"
    else:
        winner = "It's a Tie!"

    analysis = {
        "count_a": count_a,
        "count_b": count_b,
        "strong_a": strong_a,
        "strong_b": strong_b,
        "score_a": score_a,
        "score_b": score_b
    }

    return render_template('index.html', result=winner, analysis=analysis, party_a=party_a, party_b=party_b)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
