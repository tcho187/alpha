import pickle
from flask import Flask, jsonify,request

app = Flask(__name__) #instantiate Flask app
model = pickle.load(open("model.pkl", "rb")) #load saved model


@app.route('/predict', methods=['POST'])
def predict():
	data = request.get_json(force=False) #expects json
	prediction = ''.join(map(str,model.predict(data))) #prediction
	prediction_readable = 'Not Fraud' if prediction == 0 else 'Fraud' #readable prediction
	return jsonify({'prediction': prediction_readable}) #returns json

@app.route('/', methods=['GET'])
def index():
	return 'Machine Learning Inference'


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=5000)

