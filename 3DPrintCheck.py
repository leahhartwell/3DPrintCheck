# 1) Create Google Vision API service account with .json key
# 2) Create environment variable called GOOGLE_APPLICATION_CREDENTIALS with path 
# to service account .json key
# 3) Install and open Google Cloud SDK
# 4) Type: gcloud auth activate-service-account [SERVICE ACCOUNT EMAIL] --key-file=[PATH OF .JSON KEY]

import io # input/output library
from cv2 import cv2 # OpenCV library
# google cloud client libraries
from google.cloud import automl
from google.cloud.automl import types

project_id = "lofty-door-270403"
model_id = "ICN2041463239291699200"
prediction_client = automl.PredictionServiceClient() # client image function to return detected properies
model_full_id = prediction_client.model_path(
    project_id, "us-central1", model_id
)

def detect_printFailure(path): # text detection function definition with "path" argument
    """Detects print failure in the file."""
    with io.open(path, 'rb') as image_file: # open and read image_file in binary
        content = image_file.read() # read and stores image_file content in content var

    image = types.Image(image_bytes=content) # image to be processed request
    payload = types.ExamplePayload(image=image)
    params = {"score_threshold": "0.8"}
    response = prediction_client.predict(model_full_id, payload, params) # if image is present, function returns detections

    print("Prediction results:")
    for result in response.payload:
        print("Predicted class name: {}".format(result.display_name))
        print("Predicted class score: {}".format(result.classification.score))

cap = cv2.VideoCapture(0) # stores captured webcam video, frame-by-frame

while(True):
    # for each captured frame
    ret, frame = cap.read() # ret = returns true if frame is availible, frame = image array vector
    file = 'live.png' # initialzes file to store a .png image 
    cv2.imwrite( file,frame) # read captured frame stored in file variable

    detect_printFailure(file) # calls detect print failure file defined above with new file path and prints labels

    cv2.imshow('3D Print Check',frame) # names dispay frame and displays image array vector for cap
    if cv2.waitKey(1) & 0xFF == ord('q'): # frame waits 1 ms for keyboard even to equal keystroke q
        break # if q is pressed, breaks form loop

cap.release() # releases captured video
cv2.destroyAllWindows() # destory display