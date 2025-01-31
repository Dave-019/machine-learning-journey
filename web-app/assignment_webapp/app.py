from flask import Flask, request, jsonify, render_template
#
import pickle
import numpy as np

app = Flask(__name__)

# Load the model
model = pickle.load('model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the data from the POST request
    data = request.form.to_dict()
    
    # Convert data to numpy array
    input_data = np.array(list(datACa.values())).reshape(1, -1)
    
    # Make prediction
    prediction = model.predict(input_data)
    
    # Return the prediction as a response
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)