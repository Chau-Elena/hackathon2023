from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['image']
    file.save(file.filename)
    return 'Image saved!'

if __name__ == '__main__':
    app.run(port=5000)
