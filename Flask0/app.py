from flask import Flask, render_template, request
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
    photoFile = request.files['photo']
    result = make_prediction(photoFile)
    return {
        "api_stuff": "values",
        "result": result
    }


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5000, debug=True)
    app.run()
    # x_input, probs = make_prediction(features)
    # print(f'Input values: {x_input}')
    # print('Output probabilities')
    pprint(text) 