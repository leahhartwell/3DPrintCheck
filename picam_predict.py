from cv2 import cv2 # OpenCV library
from PIL import Image
from tensorflow.keras.models import load_model
#from picamera.array import PiRGBArray
#from picamera import PiCamera

cap = cv2.VideoCapture(0)
labels = ['OK', 'failed']
model = load_model('model_1a_orig.h5')

def predict(img_path):
    img = Image.open(img_path)
    img = np.array(img)
    img = np.expand_dims(img, axis=0)
    predict = model.predict(img)
    print(predict[0])
    print(labels[np.argmax(predict[0])])
    
    
while True: 
    ret, frame = cap.read()
    img_file = os.path.abspath('') + 'live.jpg'
    cv2.imwrite(img_file, frame)
    predict(img_file)
    cv2.imshow('3D Print Check', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): # frame waits 1 ms for keyboard even to equal keystroke q
        break # if q is pressed, breaks form loop

cap.release() # releases captured video
cv2.destroyAllWindows() # destory display