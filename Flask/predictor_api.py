# make prediction

# import the necessary packages
from keras.models import load_model
# import argparse
import pickle
import cv2
import numpy

from keras import backend as K

# # load the model and label binarizer
# model = load_model('vgg_CNN_adam_early128_model.h5')
# lb = pickle.loads(open("label_bin_adam__early128.env", "rb").read())

def make_prediction(photoFile):
    K.clear_session()
    # load the input image and resize it to the target spatial dimensions
    width = 64
    height = 64
    # image = cv2.imread(photoFile) #photoFile
    
    filestr = photoFile.read()
    npimg = numpy.fromstring(filestr, numpy.uint8) #convert string data to numpy array
    image = cv2.imdecode(npimg, cv2.IMREAD_UNCHANGED) # convert numpy array to image

    # output = image.copy()
    image = cv2.resize(image, (width, height))

    # scale the pixel values to [0, 1]
    image = image.astype("float") / 255.0

    # when working with a CNN: don't flatten the image, simply add the batch dimension
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))

    # load the model and label binarizer
    model = load_model('vgg_CNN_adam_early128_model.h5')
    lb = pickle.loads(open("label_bin_adam__early128.env", "rb").read())

    # make a prediction on the image
    preds = model.predict(image)

    # find the class label index with the largest corresponding probability
    i = preds.argmax(axis=1)[0]
    label = lb.classes_[i]

    # draw the class label + probability on the output image
    text = "{}: {:.2f}%".format(label, preds[0][i] * 100)

    return label, float(preds[0][i] * 100)
    # return "Hello", 90.0

# This section checks that the prediction code runs properly
# To run, type "python predictor_api.py" in the terminal.
#
# The if __name__='__main__' section ensures this code only runs
# when running this file; it doesn't run when importing



