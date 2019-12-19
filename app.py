from flask import Flask, jsonify, abort, make_response, request

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
    return 'Dictionary v2'


@app.route('/words', methods=['GET'])
def get_words():
    return jsonify({'words': dictionary})


@app.route('/word/<int:word_id>', methods=['GET'])
def get_word(word_id):
    word = list(filter(lambda t: t['id'] == word_id, dictionary))
    if len(word) == 0:
        abort(404)
    return jsonify({'task': word[0]})


@app.route('/words', methods=['POST'])
def create_word():
    word = {
        'id': dictionary.__len__() + 1,
        'word': request.form.get('word'),
        'translation': request.form.get('translation'),
        'done': False
    }
    dictionary.append(word)
    return jsonify({'words': dictionary}), 201


@app.route('/words/<int:word_id>', methods=['PUT'])
def update_task(word_id):

    for word in dictionary:
        if word.get('id') == word_id:

            if request.form.get('word') is not None:
                word['word'] = request.form.get('word')

            if request.form.get('translation') is not None:
                word['translation'] = request.form.get('translation')

            if request.form.get('done') is not None:
                word['done'] = request.form.get('done')

            return jsonify({'result': True})

    return jsonify({'task': False})


@app.route('/words/<int:word_id>', methods=['DELETE'])
def delete_word(word_id):

    for word in dictionary:
        if word.get('id') == word_id:
            dictionary.remove(word)
            return jsonify({'result': True})

    return jsonify({'result': False})


if __name__ == '__main__':
    app.run()
