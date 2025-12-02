class BinaryRepresentation:
    def __init__(self, number: float):
        if not isinstance(number, float):
            raise TypeError("Input must be a float.")
        self.number = number

    def integer2binary(self) -> str:
        integer_part = int(self.number)
        return bin(integer_part)[2:]

    def decimal2binary(self) -> str:
        decimal_part = self.number - int(self.number)
        result = []
        for _ in range(10):
            decimal_part *= 2
            bit = int(decimal_part)
            result.append(str(bit))
            decimal_part -= bit
        return ''.join(result)

    def __str__(self) -> str:
        return f"{self.integer2binary()}.{self.decimal2binary()}"



from flask import Flask, request, jsonify
from binary_representation import BinaryRepresentation

app = Flask(__name__)

@app.route('/binary', methods=['GET'])
def binary():
    number_str = request.args.get('number')
    if number_str is None:
        return jsonify({"error": "Missing 'number' query parameter"}), 400

    try:
        number = float(number_str)
    except ValueError:
        return jsonify({"error": "Invalid float value"}), 400

    try:
        binary = str(BinaryRepresentation(number))
        return jsonify({"binary": binary})
    except TypeError as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
