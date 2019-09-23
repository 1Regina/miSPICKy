from flask import Flask, render_template, url_for, request
from flask_bootstrap import Bootstrap

# Deep Learning Package
from keras.models import load_model
import pickle
import cv2

app = Flask(__name__)
Bootstrap(app)


@app.route('/')  # methods=['GET', 'POST']) should methods be 2.
def render_static():
    return flask.render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict(image):
    # load the input image and resize it to the target spatial dimensions
    width = 64
    height = 64
    image = cv2.imread() # Shd i remove this image? "static\SGLr.jpg"
    output = image.copy()
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
    cv2.putText(output, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    # show the output image
    cv2.imshow("Image", output)
    cv2.waitKey(0)   # Delay in milliseconds. 0 is the special value that means “forever”, until you close the image window

# # Receives the input query from form
#if request.method == 'POST':
# 	namequery = request.form['namequery']
# 	data = [namequery]
# 	vect = cv.transform(data).toarray()
# 	my_prediction = clf.predict(vect)
# return render_template('results.html',prediction = my_prediction,name = namequery.upper())


if __name__ == '__main__':
    app.run()

