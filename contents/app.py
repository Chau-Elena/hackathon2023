from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from roboflow import Roboflow
from trash_objects import objects_list
import config
import gptcontents as gpt
import os

# APP_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# TEMPLATE_PATH = os.path.join(APP_PATH, 'templates/')

my_list = objects_list()

def page_not_found(e):
  return render_template('404.html'), 404


app = Flask(__name__)
app.config.from_object(config.config['development'])
app.register_error_handler(404, page_not_found)
rf = Roboflow(api_key="QgwRoa71JYqIgWfVPa8k")
project = rf.workspace().project("trashdetection1141")
model = project.version(1).model



@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', **locals())

# app route

#change
@app.route('/text-prompt', methods=["GET", "POST"])
def textPrompt():

    if request.method == 'POST':
        query = request.form['textPrompt']
        openAIAnswer = gpt.diy_generation(query)
        prompt = 'AI Suggestions for {} are:'.format(query)
        

    return render_template('text-prompt.html', **locals())


@app.route('/ai-prompt', methods=["GET", "POST"])
def aiPrompt():

    if request.method == 'POST':
        query = request.form['aiPrompt']
        openAIAnswer = gpt.diy_generation(query)
        prompt = 'AI Suggestions for {} are:'.format(query)

    return render_template('ai-prompt.html', **locals())

# def upload_image():
#     # Check if a file was uploaded
#     if request.method == 'POST' and 'file' in request.files:
#         # Get the uploaded file
#         file = request.files['file']
        
#         # Save the file to disk
#         filename = secure_filename(file.filename)
#         file.save(filename)
        
#         # Call the model to get the predicted classes
#         result = model.predict(filename, confidence=30, overlap=30)
#         data = result.json()
#         #imageclass = []
#         for prediction in data['predictions']:
#             class_name = prediction['class']
#             my_list.append(class_name)
#             print(class_name)
        
#         # Remove the saved file
#         os.remove(filename)
        
#         # Return the predicted classes as a response
#         return '\n'.join(str(item) for item in my_list)
    
#     # If no file was uploaded, render the predict page
#     return render_template('404.html')

# app route

@app.route('/upload', methods=['GET', 'POST'])
def upload_image():
    # Check if a file was uploaded
    if request.method == 'POST' and 'file' in request.files:
        # Get the uploaded file
        file = request.files['file']
        
        # Save the file to disk
        filename = secure_filename(file.filename)
        file.save(filename)
        
        # Call the model to get the predicted classes
        result = model.predict(filename, confidence=30, overlap=30)
        data = result.json()
        #imageclass = []
        for prediction in data['predictions']:
            class_name = prediction['class']
            my_list.append(class_name)
            print(class_name)
        
        # Remove the saved file
        os.remove(filename)
        
        # Return the predicted classes as a response
        return '\n'.join(str(item) for item in my_list)
    
    # If no file was uploaded, render the predict page
    return render_template('404.html')

# app route




if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True)
