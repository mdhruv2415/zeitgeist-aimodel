from flask import Flask, jsonify, request
from main import fetchoutput
app = Flask( __name__)

@app.route('/ai-data', methods=['POST'])
def ai_data():
    request_data = request.json
    input_string = None
    if 'text' in request_data:
        input_string = request_data['text']
    elif 'message' in request_data:
        input_string = request_data['message']

    # If no suitable text found, handle accordingly
    # if input_string is None:
    #     return jsonify({'error': 'Missing text or message key in request data'})

    output = fetchoutput(input_string)
    return output

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"status": 404, "message": "Not Found"}), 404

if __name__ =='__main__':
    app.run(host='0.0.0.0', port=5000)