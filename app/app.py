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
        answer = True
        if random.random() > 0.5:
            answer = False
        return Response(response=json.dumps({'result': str(answer)}), status=200, headers=get_header(request),
                        mimetype='application/json')
    else:
        return Response(response=json.dumps({'result': "action: " + str(action) + " is not supported!"}), status=422,
                        headers=get_header(request), mimetype='application/json')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
