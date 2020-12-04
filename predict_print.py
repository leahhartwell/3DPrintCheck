import matplotlib.pyplot as plt
from PIL import Image

#labels
labels = ['ok', 'fail']
#load model
model = load_model('full_saved_model_V3.h5')

#code to process new images
spec_img = Image.open(r'C:\Users\hartw\GitHub\3DPrintCheck\dataset\0_ok_1214.png')
spec_arr = np.asarray(spec_img)
#print(type(spec_arr))
#print(spec_arr.shape)
spec_arr = np.expand_dims(spec_arr, axis=0)
#print(type(spec_arr))
#print(spec_arr.shape)

#prediction using model
predict = model.predict(spec_arr)

print(predict[0])
print(labels[np.argmax(predict[0])])

# implementing openCV integration for live predictions