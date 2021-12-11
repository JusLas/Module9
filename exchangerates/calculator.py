from flask import Flask, render_template, request
from data import get_rates


app = Flask(__name__)

@app.route("/calculator/", methods=["GET", "POST"])
def calculate():

    rates = get_rates()

    data = {
        "current_amount": 0,
        "current_currency": "",
        "rates": rates,
        "final_price": None
    }

    if request.method == "POST":
        form_data = request.form
        amount = float(form_data.get("amount", 0))
        currency = form_data.get("currency", None)

        if currency is not None:
            data["current_amount"] = amount
            data["current_currency"] = currency
            data["final_price"] = amount * get_ask_for_currency(
                rates, currency)

    return render_template("calculator.html", data=data)


def get_ask_for_currency(rates, code):
    if rates:
        rate = next((r for r in rates if r["code"] == code), None)
        if rate:
            return rate["ask"]

    return 0


if __name__ == "__main__":
    app.run(debug=True)
