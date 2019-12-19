from flask import Flask, jsonify, abort, make_response, request
import unicode

app = Flask(__name__)

dictionary = [
    {
        'id': 1,
        'word': u'table',
        'translation': u'стіл',
        'done': False
    },
    {
        'id': 2,
        'word': u'chair',
        'translation': u'крісло',
        'done': False
    }
]


@app.route('/')
def hello_world():
    return 'Dictionary'


@app.route('/words', methods=['GET'])
def get_words():
    return jsonify({'words': dictionary})


@app.route('/word/<int:word_id>', methods=['GET'])
def get_word(word_id):
    word = list(filter(lambda t: t['id'] == word_id, dictionary))
    if len(word) == 0:
        abort(404)
    return jsonify({'task': word[0]})


@app.route('words', methods=['POST'])
def create_word():
    if not request.json or not 'word' in request.json:
        abort(400)
    word = {
        'id': 4,
        'word': request.json['word'],
        'translation': request.json.get('translation', ""),
        'done': False
    }
    dictionary.append(word)
    return jsonify({'words': dictionary}), 201


@app.route('/words/<int:word_id>', methods=['PUT'])
def update_task(word_id):
    word = list(filter(lambda t: t['id'] == word_id, dictionary))
    if len(word) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'word' in request.json and type(request.json['word']) != unicode:
        abort(400)
    if 'translation' in request.json and type(request.json['translation']) is not unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    word[0]['word'] = request.json.get('word', word[0]['word'])
    word[0]['translation'] = request.json.get('translation', word[0]['translation'])
    word[0]['done'] = request.json.get('done', word[0]['done'])
    return jsonify({'task': word[0]})


@app.route('/words/<int:word_id>', methods=['DELETE'])
def delete_word(word_id):
    word = filter(lambda t: t['id'] == word_id, dictionary)
    if len(word) == 0:
        abort(404)
    dictionary.remove(word[0])
    return jsonify({'result': True})


if __name__ == '__main__':
    app.run()
