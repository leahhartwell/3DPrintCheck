from sklearn.metrics import confusion_matrix
from tensorflow.keras.models import load_model
import tensorflow as tf

#CPU Only
#os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
#GPU
physical_devices = tf.config.list_physical_devices("GPU")
tf.config.experimental.set_memory_growth(physical_devices[0], True)

#dataset images and labels
X = []
y = []

#dataset file path
SCRIPT_DIR = os.path.abspath('')
DATA_DIR = SCRIPT_DIR + '\\dataset\\' 
print(DATA_DIR)

#number of files in dataset
length = len(os.listdir(DATA_DIR))
print(length)

#converting file names to labels and images to np arrays
for fname in os.listdir(DATA_DIR):
    #print(fname)
    FILE_DIR = DATA_DIR + fname
    fname_arr = fname.split('_')
    label = fname_arr[1]
    spec_img = Image.open(FILE_DIR)
    spec_arr = np.asarray(img)
    
    X.append(arr)
    y.append(label)
    
X = np.array(X)
y = to_categorical(np.array(y))

#splitting dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

y_pred = []
y_true = []

#labels
labels = ['ok', 'fail']

#load model
model = load_model('full_saved_model_V3.h5')

#prediction using model
predict = model.predict([X_test])

for i in range(len(X_test)):
    pred_label = labels[np.argmax(predict[i])]
    y_pred.append(pred_label)
for i in range(len(X_test)):
    true_label = labels[np.argmax(y_test[i])]
    y_true.append(true_label)

#outputs confusing matrix
confusion_matrix(y_true, y_pred, labels=labels)

#outputs specific images that where predicted incorrectly
count = 0
for i in range(len(X_test)):
    if y_pred[i] == y_true[i]:
        continue
    else:
        count = count + 1
        print("Wrong Prediction Number: " + str(count))
        print("Image Number: " + str(i))
        print("True Label: " + str(y_true[i]))
        print("Predict Label: " + str(y_pred[i]))
        plt.imshow(X_test[i])
        plt.show()