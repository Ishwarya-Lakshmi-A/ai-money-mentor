function analyze() {
    let income = document.getElementById("income").value;

    let expenses = {
        food: parseInt(document.getElementById("food").value) || 0,
        travel: parseInt(document.getElementById("travel").value) || 0
    };

    fetch('/analyze', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ income: income, expenses: expenses })
    })
    .then(res => res.json())
    .then(data => {
        let output = `
        Total Expense: ₹${data.total_expense} <br>
        Balance: ₹${data.balance} <br>
        Suggestions: <br> ${data.suggestions.join("<br>")}
        `;
        document.getElementById("result").innerHTML = output;
    });
}
