from flask import Flask, request, Response, make_response, json, render_template
from flask_restful import Resource, Api
from Detector import Detector


app = Flask(__name__)
api = Api(app)
detector = Detector()


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
        print('received content:', sentence)
        outputs = detector.detect(sentence)
        answer = outputs['answer']
        spam_words_str = outputs['spam_words']
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


@app.route("/")
@app.route("/<string:page>")
def pages(page=None):
    if page == 'homepage':
        return render_template("homepage.html", title='Homepage')
    else:
        return render_template("error.html", title='404')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
