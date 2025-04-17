from flask import Flask, request, Response
import json

app = Flask(__name__)

@app.route('/')
def home():
    return 'Witaj w moim API!'

@app.route('/mojastrona')
def mojastrona():
    return 'To jest moja strona!'

@app.route('/hello')
def hello():
    name = request.args.get('name', 'World')
    return f'Hello {name}!'

@app.route('/api/v1.0/predict')
def predict():
    try:
        num1 = float(request.args.get('num1', 0))
        num2 = float(request.args.get('num2', 0))
    except ValueError:
        return Response(json.dumps({"error": "Invalid input"}), status=400, mimetype='application/json')

    suma = num1 + num2
    prediction = 1 if suma > 5.8 else 0

    response_dict = {
        "prediction": prediction,
        "features": {
            "num1": num1,
            "num2": num2
        }
    }

    response_json = json.dumps(response_dict, separators=(',', ': '))
    return Response(response_json, mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True) 
