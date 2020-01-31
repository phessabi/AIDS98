from flask import Flask, request, Response, make_response, json
from flask_restful import Resource, Api
import random


app = Flask(__name__)
api = Api(app)


def get_header(req):
    return {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET,POST',
        'Access-Control-Allow-Headers': 'Content-Type'
    }


@app.route("/<string:action>", methods=["POST"])
def handle(action):
    if action == 'detect':
        sentence = request.form['content']
        words = sentence.split()
        spam_words = set()
        for word in random.choices(words, k=3):
            spam_words.add(word)
        spam_words_str = ''
        for word in spam_words:
            spam_words_str += word + ' - '
        spam_words_str = spam_words_str[:-3]
        answer = True
        if random.random() > 0.5:
            answer = False
        if answer:
            return Response(response=json.dumps({'result': str(answer),
                                                 'reasons': spam_words_str,
                                                 })
                            , status=200, headers=get_header(request),
                            mimetype='application/json')
        else:
            return Response(response=json.dumps({'result': str(answer),
                                                 'reasons': ''})
                            , status=200, headers=get_header(request),
                            mimetype='application/json')
    else:
        return Response(response=json.dumps({'result': "action: " + str(action) + " is not supported!"}), status=422,
                        headers=get_header(request), mimetype='application/json')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
