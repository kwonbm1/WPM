from flask import Flask, render_template, request, jsonify
import os
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/calculate_wpm', methods=['POST'])
def calculate_wpm():
    length = request.form.get('length')
    if length:
        url = "https://random-word-api.herokuapp.com/word?number=" + length
        try:
            response = requests.get(url)
            phrase = response.json()
            wordCount = len(phrase)
            finalPhrase = " ".join(phrase).strip()
            return jsonify({'finalPhrase': finalPhrase, 'wordCount': wordCount})
        except Exception as e:
            error_message = "An error occurred: {}".format(str(e))
            return jsonify({'error': error_message}), 500
    else:
        return jsonify({'error': 'Length parameter is missing'}), 400

if __name__ == '__main__':
    app.run(debug=True)




