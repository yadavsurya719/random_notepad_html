from flask import Flask, render_template, request, send_file
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/clear_text', methods=['POST'])
def clear_text():
    return ''

@app.route('/download_text', methods=['POST'])
def download_text():
    content = request.form.get('content')
    file_data = BytesIO(content.encode())
    return send_file(file_data, download_name='notepad_content.txt', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
