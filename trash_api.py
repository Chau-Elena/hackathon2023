from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
from roboflow import Roboflow
import os

app = Flask(__name__, template_folder='/templates')
rf = Roboflow(api_key="QgwRoa71JYqIgWfVPa8k")
project = rf.workspace().project("trashdetection1141")
model = project.version(1).model

@app.route('/predict', methods=['GET', 'POST'])
def predict_image():
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
        imageclass = []
        for prediction in data['predictions']:
            class_name = prediction['class']
            imageclass.append(class_name)
        
        # Remove the saved file
        os.remove(filename)
        
        # Return the predicted classes as a response
        return '\n'.join(imageclass)
    
    # If no file was uploaded, render the predict page
    return render_template('predict.html')



if __name__ == '__main__':
    app.run()