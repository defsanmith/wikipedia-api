from flask import Flask, request, jsonify
from summarize.summarize import summarize

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return "Welcome!"


@app.route('/summarize', methods=['GET'])
def getSummary():
    title = request.args.get('title')

    try:
        summary = summarize(title)
        return jsonify({'status': True, 'summary': summary})
    except Exception as e:
        print(e)
        return jsonify({'status': False, 'summary': None})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)
