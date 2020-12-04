from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from PIL import Image
import os
import numpy as np
import random as rn
from tensorflow.keras.layers import Dense
from tensorflow.keras import Input
from tensorflow.keras.models import Model, load_model
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.layers import Dense, TimeDistributed, Dropout, Bidirectional, GRU, BatchNormalization, Activation, LeakyReLU, \
    LSTM, Flatten, RepeatVector, Permute, Multiply, Conv2D, MaxPooling2D
import tensorflow as tf

#CPU Only
#os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
#GPU
physical_devices = tf.config.list_physical_devices("GPU")
tf.config.experimental.set_memory_growth(physical_devices[0], True)

X = []
y = []

SCRIPT_DIR = os.path.abspath('')
DATA_DIR = SCRIPT_DIR + '\\dataset\\' 
print(DATA_DIR)

length = len(os.listdir(DATA_DIR))
print(length)

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

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

ip = Input(shape=X_train[0].shape)
m = Conv2D(32, kernel_size=(3, 3), activation='relu', padding='same')(ip)
m = Conv2D(64, kernel_size=(3, 3), activation='relu', padding='same')(m)
m = MaxPooling2D(pool_size=(2, 2))(m)
m = Dropout(0.25)(m)
m = Flatten()(m)
m = Dense(64, activation='relu')(m)
m = Dropout(0.3)(m)
op = Dense(2, activation='softmax')(m)

model = Model(ip, op)
model.summary()

opt = tf.keras.optimizers.Adam(learning_rate=0.001)
model.compile(loss='categorical_crossentropy',
              optimizer=opt,
              metrics=['accuracy'])

history = model.fit(X_train,
          y_train,
          epochs=20,
          batch_size=4,
          verbose=1,
          validation_data=(X_test, y_test))

model.save('full_saved_model_V3.h5')