import numpy as np
import pickle
import math
from flask import Flask, render_template, request
from sklearn.linear_model import LinearRegression

app = Flask(__name__)
model = pickle.load(open('DataScience_Final/model(1).pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/PREDICT', methods=['GET', 'POST'])
def predict():
    if request.method == "POST":
        try:
            Month = float(request.form.get('Month'))
            hour = float(request.form.get('hour'))
            wind_deg = float(request.form.get('wind_deg'))
            Total_Power_lag1 = float(request.form.get('Total_Power_lag1'))
            Total_Power_lag2 = float(request.form.get('Total_Power_lag2'))
            Total_Power_lag3 = float(request.form.get('Total_Power_lag3'))
            Total_Power_lag4 = float(request.form.get('Total_Power_lag4'))
            Total_Power_lag5 = float(request.form.get('Total_Power_lag5'))
            Total_Power_lag6 = float(request.form.get('Total_Power_lag6'))
            Total_Power_lag7 = float(request.form.get('Total_Power_lag7'))
            Total_Power_lag8 = float(request.form.get('Total_Power_lag8'))
            Total_Power_lag9 = float(request.form.get('Total_Power_lag9'))
            Total_Power_lag10= float(request.form.get('Total_Power_lag10'))


            final_features =[[Month,hour,wind_deg,Total_Power_lag1,Total_Power_lag2,
            Total_Power_lag3,Total_Power_lag4,Total_Power_lag5,Total_Power_lag6,
            Total_Power_lag7,Total_Power_lag8,Total_Power_lag9,Total_Power_lag10]]
            prediction = model.predict(final_features)
            output = round(prediction[0],2)
            global pred 
            pred =  "Total power is " + str(output)

        except ValueError:
            return "CHEAK THE INPUTS"

   
    return render_template('index.html',prediction = pred)


@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)