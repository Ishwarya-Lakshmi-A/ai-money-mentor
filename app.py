from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    income = int(data['income'])
    expenses = data['expenses']

    total_expense = sum(expenses.values())
    balance = income - total_expense

    suggestions = []

    if expenses.get('food', 0) > 0.4 * income:
        suggestions.append("High spending on food. Try reducing it.")

    if balance < 0:
        suggestions.append("You are overspending!")

    if balance > 0:
        suggestions.append(f"Try saving ₹{int(balance * 0.3)} per month.")

    return jsonify({
        "total_expense": total_expense,
        "balance": balance,
        "suggestions": suggestions
    })

if __name__ == '__main__':
    app.run(debug=True)
