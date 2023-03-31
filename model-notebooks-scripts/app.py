
from flask import Flask, request, jsonify
from prediction import smartcities
import base64

app = Flask(__name__)


@app.route('/', methods = ['POST'])
def parse_request():
    request_data = request.get_json()
    video_64 = request_data['video']
    sc = smartcities()
    response_64 = sc.predict(video_64)
    return jsonify(output=response_64)

# Entry point
if __name__ == "__main__":
    app.run(debug = True, host = '0.0.0.0', port = 8000)
