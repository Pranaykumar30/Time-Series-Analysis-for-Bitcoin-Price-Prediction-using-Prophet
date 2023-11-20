import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle

# Flask app
app = Flask(__name__)

# Loading the saved model
m = pickle.load(open('prophetbitcoin.pkl', 'rb'))

# Make forecast and prediction
future = m.make_future_dataframe(periods=365)
forecast = m.predict(future)
print(forecast)

@app.route('/', methods=["GET"])
def index():
    # Main page
    return render_template('index.html')  # Rendering html page

@app.route('/Bitcoin', methods=['GET'])
def prediction_page():
    # Route to the prediction page
    return render_template('predict.html')

@app.route('/predict', methods=['GET', 'POST'])
def y_predict():
    if request.method == "POST":
        ds = request.form["Date"]
        ds = str(ds)
        next_day = ds
        prediction = forecast[forecast['ds'] == next_day]['yhat'].item()
        prediction = round(prediction, 2)
        return render_template('predict.html', prediction_text="Bitcoin Price on the selected date is $ {} Cents".format(prediction))
    else:
        # For GET requests, render the prediction form
        return render_template('predict.html')

if __name__ == "__main__":
    app.run(debug=False)
