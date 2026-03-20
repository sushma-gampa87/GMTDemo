from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample tax brackets
TAX_BRACKETS = [
    {'rate': 0.1, 'min': 0, 'max': 9875},
    {'rate': 0.12, 'min': 9876, 'max': 40125},
    {'rate': 0.22, 'min': 40126, 'max': 85525},
    {'rate': 0.24, 'min': 85526, 'max': 163300},
    {'rate': 0.32, 'min': 163301, 'max': 207350},
    {'rate': 0.35, 'min': 207351, 'max': 518400},
    {'rate': 0.37, 'min': 518401, 'max': float('inf')},
]

@app.route('/calculate_tax', methods=['POST'])
def calculate_tax():
    data = request.json
    income = data.get('income', 0)
    tax = 0
    for bracket in TAX_BRACKETS:
        if income > bracket['min']:
            taxable_income = min(income, bracket['max']) - bracket['min']
            tax += taxable_income * bracket['rate']
    return jsonify({'tax': tax})

@app.route('/tax_brackets', methods=['GET'])
def get_tax_brackets():
    return jsonify(TAX_BRACKETS)

@app.route('/tax_summary', methods=['POST'])
def tax_summary():
    data = request.json
    income = data.get('income', 0)
    tax = calculate_tax(income)
    return jsonify({'income': income, 'tax': tax})

if __name__ == '__main__':
    app.run(debug=True)