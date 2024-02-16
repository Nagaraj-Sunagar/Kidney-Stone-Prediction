import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle


app = Flask(__name__, template_folder='templets')
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')



@app.route('/', methods=['post'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    print(int_features)
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0])

    if (output == 1):
        predictions = "You have Kideny Stones!!🥺"
    else:
        predictions = "Don't Worry you don't have stones😊"

    return render_template('index.html', prediction_text=predictions)


if __name__ == "__main__":
    app.run(debug=True)
