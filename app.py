from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
from utils import odd_even, is_perfect, digit_sum, is_prime, is_armstrong

app = Flask(__name__)
CORS(app)


@app.route("/api/classify-number", methods=["GET"])
def classify_number():
    """Classifies a number"""
    try:
        number = int(request.args.get('number'))
        abs_number = abs(number)
        url = f"http://numbersapi.com/{abs_number}/math?json"
        response = requests.get(url)
        fun_fact = ""
        if response.status_code == 200:
            fun_fact = response.json().get("text", "No fun fact found.")
        else:
            fun_fact = "This number does not have a fun fact."

        properties = []
        if is_armstrong(abs_number):
            properties.append("armstrong")
        
        properties.append(odd_even(abs_number))

        response = {
            "number": number,
            "is_prime": is_prime(abs_number),
            "is_perfect": is_perfect(abs_number),
            "properties": properties,
            "digit_sum": digit_sum(abs_number),
            "fun_fact": fun_fact
        }
        return jsonify(response), 200

    except (ValueError, TypeError):
        alphabet = request.args.get('number')
        response = {
            "number": alphabet,
            "error": True
        }
        return jsonify(response), 400


if __name__ == "__main__":
    app.run()
