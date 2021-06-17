from flask import Flask, render_template, request

import pickle

from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('bodyfat1.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
   
  
    Age=int(request.form['Age'])
    Weight=float(request.form['Weight'])
    Height=float(request.form['Height'])
    Chest=float(request.form['Chest'])
    Abdomen=float(request.form['Abdomen'])
    Knee=float(request.form['Knee'])
    Wrist=float(request.form['Wrist'])
    Density=float(request.form['Density'])
     
       
    prediction=model.predict([[Age,Weight,Height,Chest,Abdomen,Knee,Wrist,Density]])
    output=round(prediction[0],2)
    return render_template('index.html',prediction_text="Body Fat Percentage is{}".format(output))
 

if __name__=="__main__":
    app.run(debug=True)

