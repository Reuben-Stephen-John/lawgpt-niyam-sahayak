from flask import Flask, request, jsonify
from flask_cors import CORS
from model import generate_response

app = Flask(__name__)
CORS(app)  # Enable CORS for your entire Flask app

@app.route('/prompt', methods=['POST'])
def process():
    # Get the input data from the POST request
    data = request.json  # Assumes JSON data is sent in the request

    # Check if 'prompt' is in the JSON data
    if 'prompt' in data:
        prompt = data['prompt']
        response = generate_response(prompt)  # Call the generate_response function
        return jsonify({'response': response})
    else:
        return jsonify({'error': 'Missing prompt parameter'}), 400

if __name__ == '__main__':
    app.run(debug=True)

