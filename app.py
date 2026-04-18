from flask import Flask , render_template, request
import os
import numpy as np 
import pandas as pd 
from mlopsProject.pipeline.prediction import predictionpipeline

app = Flask(__name__)

@app.route('/',methods = ['GET']) #homepage
def homepage():
    return render_template("index.html")

@app.route('/train', methods = ['GET']) #training
def train():
    os.system("python main.py")

    return "Training sucessful"

@app.route('/predict',methods = ['POST','GET'])
def predict():
    if request.method == 'POST':
        try:
            # Extract data from the form
            fixed_acidity = float(request.form['fixed_acidity'])
            volatile_acidity = float(request.form['volatile_acidity'])
            citric_acid = float(request.form['citric_acid'])
            residual_sugar = float(request.form['residual_sugar'])
            chlorides = float(request.form['chlorides'])
            free_sulfur_dioxide = float(request.form['free_sulfur_dioxide'])
            total_sulfur_dioxide = float(request.form['total_sulfur_dioxide'])
            density = float(request.form['density'])
            pH = float(request.form['pH'])
            sulphates = float(request.form['sulphates'])
            alcohol = float(request.form['alcohol'])
            
            # Prepare data for prediction
            data = [fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol]
            data = np.array(data).reshape(1, 11)
            
            prediction_pipeline = predictionpipeline()
            pred = prediction_pipeline.predict(data)
            
            # Format and pass results to results.html
            results = str(round(pred[0], 2))
            
            return render_template("results.html", results=results)
        except Exception as e:
            print("The Exception message is: ", e)
            return "Something went wrong while predicting " + str(e)
    else:
        return render_template("index.html")

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=8080)