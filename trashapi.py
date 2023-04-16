from roboflow import Roboflow
rf = Roboflow(api_key="QgwRoa71JYqIgWfVPa8k")
project = rf.workspace().project("trashdetection1141")
model = project.version(1).model

# infer on a local image
print(model.predict("WIN_20230415_18_26_04_Pro.jpg", confidence=30, overlap=30).json())

# visualize your prediction
# model.predict("your_image.jpg", confidence=40, overlap=30).save("prediction.jpg")

# infer on an image hosted elsewhere
# print(model.predict("img.com", hosted=True, confidence=40, overlap=30).json())