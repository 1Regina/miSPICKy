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
    # print(request.files)
    photoFile = request.files['file']
    # print("aa")
    # print(photoFile)
    result, result_val = make_prediction(photoFile)
    # # return render_template('index.html', result=result, result_val = result_val)
    # return {
    #     "aaa": result,
    #     "bbb": result_value 
    # }
    # print(result)
    # print(result_val)
    return {
        "result": result,
        "result_val": result_val
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
    # app.run()