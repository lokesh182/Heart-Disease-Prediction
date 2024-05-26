from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('Heart1.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')
standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Age = int(request.form['age'])
        sex = int(request.form['sex'])
        cp = int(request.form['cp'])
        trestbps = int(request.form['tbps'])
        chol = int(request.form['chol'])
        fbs = int(request.form['fbs'])
        restecg = int(request.form['ecg'])
        thalach = int(request.form['thalach'])
        exang = int(request.form['exang'])
        old_peak= float(request.form['oldpeak'])
        slope = int(request.form['slope'])
        ca = int(request.form['ca'])
        thal = int(request.form['Thal'])
        prediction_model = model.predict([[Age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,old_peak,slope,ca,thal]])
        output = round(prediction_model[0],2)
        if output<0:
            return render_template('index.html',prediction_texts="Error")
        else:
            return render_template('index.html',prediction_text="You have an Disease Value as : -  {}".format(output))
    else:
        return render_template('index.html')
    
if __name__=="__main__":
    app.run(debug=True)
        

        
        
        
        
        
        