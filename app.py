
# Import Required Libraries

from flask import Flask,render_template,request
import pickle
import numpy as np

# We need to initialise the Flask object to run the flask app 
# By assigning parameters as static folder name,templates folder name

app = Flask(__name__,template_folder='templates',static_folder='static')

# We need to load the pickled model file so as to use it for the prediction

model=pickle.load(open('model.pkl','rb+'))

# For the root '/' we need to define a function in which we are rendering the template of index.html as default
# This rendering template is done if it get's any GET Request

@app.route('/',methods=['POST','GET'])
def main():
  if request.method=='GET':
    return render_template('index.html')

# For the root '/predict' we need to define a function named predict
# This function will take values from the ajax request and performs the prediction
# By getting response from flask to ajax it will display the response to the result field
# This whole above process occurs when request method is POST
# This rendering template is index.html if it get's any GET Request

@app.route('/predict',methods=['POST','GET'])
def predict():
  if request.method=='GET':
    return render_template('index.html')
  if request.method=='POST':
    # Converting all the form values to float and making them append in a list(features)
    features=np.array([float(x) for x in request.form.values()])
    # Printing the features for debug purpose
    print(features)
    # Predicting the label for the features collected
    labels=model.predict_proba([features])
    # Printing the labels array for debug purpose
    print(labels)
    # Storing the result from the labels array
    species=labels[0]

    if species[0] > 0.5:
      return 'Probability of forest fire not occur {}, Forest is safe now!!..'.format(round(species[0],4))
    else:
      return 'Probability of forest fire not occur {}, Forest is risk now!!..'.format(round(species[0],4))
    
# It is the starting point of code
if __name__=='__main__':
  # We need to run the app to run the server
  app.run(host='0.0.0.0',port=8080,debug=False)