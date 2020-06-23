from flask import abort, Flask, jsonify, request

from flair.models import TextClassifier
from flair.data import Sentence
classifier = TextClassifier.load('en-sentiment')

app = Flask(__name__)
@app.route('/api/v1', methods=['POST'])

def response():
    if not request.json or not 'message' in request.json:
        abort(400)
    message = request.json['message']
    
    sentence = Sentence(message)
    classifier.predict(sentence)
    response = {'sentiment': sentence.labels[0].value, 'polarity':sentence.labels[0].score}
    
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)
