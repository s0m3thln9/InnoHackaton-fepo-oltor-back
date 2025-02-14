from flask import Flask, jsonify
from flask_cors import CORS
from api.db_utils import get_all_people

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "https://inno-hackathon-fepo-oltor-front.vercel.app"}}, supports_credentials=True)

@app.route('/api/people', methods=['GET'])
def get_people():
    try:
        people = get_all_people()
        return jsonify({'people': people})
    except Exception as e:
        return jsonify({'status': False, 'message': str(e)})

@app.route('/api/people', methods=['OPTIONS'])
def handle_options():
    response = jsonify({})
    response.headers.add('Access-Control-Allow-Origin', 'https://inno-hackathon-fepo-oltor-front.vercel.app')
    response.headers.add('Access-Control-Allow-Methods', 'POST, OPTIONS')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    return response

if __name__ == "__main__":
    app.run()