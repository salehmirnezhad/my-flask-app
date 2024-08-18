import os
import json
from flask import Flask, jsonify

echo "saleh mirnezhad"
app = Flask(__name__)

def get_directory_info(path):
    total_files = 0
    total_size = 0

    for dirpath, dirnames, filenames in os.walk(path):
        total_files += len(filenames)
        total_size += sum(os.path.getsize(os.path.join(dirpath, f)) for f in filenames)

    return {
        "path": path,
        "file_count": total_files,
        "total_size": total_size
    }

@app.route('/directory_info', methods=['GET'])
def directory_info():
    root_path = '/tmp'  # می‌توانید این را به هر دایرکتوری که می‌خواهید تغییر دهید
    info = get_directory_info(root_path)
    return jsonify(info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
