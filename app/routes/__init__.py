from flask import request, jsonify
from app import app
from app.services.chatbot_services import *

# @app.route("/similiar", methods=['POST'])
# def similiar():
#     data = request.json
#     query = data.get('query', '')
#     print(f"Query received: {query}")
#     prompts = handle_similar_queries(query)
#     return jsonify({'response': prompts})

# @app.route('/')
# def index():
#     return send_from_directory(app.static_folder, 'index.html')

# @app.route('/<path:path>')
# def serve_static(path):
#     return send_from_directory(app.static_folder, path)

@app.route("/response", methods=['POST'])
def response():
    data = request.json
    question = data.get('query', '')
    print(f"Question received: {question}\n")
    ans = handle_question(question)
    print(ans)
    return jsonify({'response': ans})


from flask import request, jsonify
from app import app
from werkzeug.utils import secure_filename
import os
from app.services.loader import extract_text_from_pdf
from app.services.chatbot_services import handle_question

UPLOAD_FOLDER = 'data'
ALLOWED_EXTENSIONS = {'pdf'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        text = extract_text_from_pdf(filename)
        return jsonify({'text': text}), 200
    #     file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    #     file.save(file_path)
        
        # Extract text using the function from document_services
    # text = extract_text_from_pdf(file_path)
        
    # return jsonify({'text': text}), 200


