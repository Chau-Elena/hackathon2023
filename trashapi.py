from roboflow import Roboflow
rf = Roboflow(api_key="QgwRoa71JYqIgWfVPa8k")
project = rf.workspace().project("trashdetection1141")
model = project.version(1).model

# infer on a local image
#print(model.predict("WIN_20230415_18_26_04_Pro.jpg", confidence=30, overlap=30).json())
# interpret the results
# Call the predict function and get the result object


result = model.predict("twogirlsonecup.png", confidence=30, overlap=30)

# Parse the JSON data into a Python dictionary or list
data = result.json()
#print (len(data['predictions']))

imageclass = []

for prediction in data['predictions']:
    class_name = prediction['class']
    imageclass.append(class_name)
    #print(class_name)

for imageclass in imageclass:
    print(imageclass)


# predictions = data['predictions']

# print(data)

# class_name = data['predictions'][0]['class']
# print(class_name)

# for prediction in predictions:
#     class_name = predictions['class']
#     print(class_name)



# print(data["predictions"])

# if len(data) == 0:
#     print("Error: No objects detected in image.")
# else:
#     # Extract the value of the 'class' key from the first dictionary in the list
#     if 'class' not in data[0]:
#         print("Error: 'class' key not found in dictionary.")
#     else:
#         class_name = data[0]['class']
#         # Use the class name as needed, for example:
#         print(class_name)
# visualize your prediction
# model.predict("your_image.jpg", confidence=40, overlap=30).save("prediction.jpg")

# infer on an image hosted elsewhere
# print(model.predict("img.com", hosted=True, confidence=40, overlap=30).json())