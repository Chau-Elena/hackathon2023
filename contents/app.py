from flask import Flask, render_template, request
import config
import gptcontents as gpt
# import os

# APP_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# TEMPLATE_PATH = os.path.join(APP_PATH, 'templates/')

def page_not_found(e):
  return render_template('404.html'), 404


app = Flask(__name__)
app.config.from_object(config.config['development'])
app.register_error_handler(404, page_not_found)


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', **locals())

# app route


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True)
