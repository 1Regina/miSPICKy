from flask import Flask, render_template, url_for, request
from predictor_api import make_prediction

# Deep Learning Package
# from keras.models import load_model
# import pickle
# import cv2

app = Flask(__name__)
# Bootstrap(app)


@app.route('/')  # methods=['GET', 'POST']) should methods be 2.
def render_static():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    result = make_prediction()
    return {
        "api_stuff": "values",
        "result": result
    }


if __name__ == '__main__':
    app.run()
