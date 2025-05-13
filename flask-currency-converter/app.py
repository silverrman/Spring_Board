from flask import Flask, render_template, request, flash, redirect, url_for
from currency_utils import convert_currency, is_valid_currency, is_valid_amount

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Handle the home page form for currency conversion.
    GET: Display the form
    POST: Process form submission and perform conversion
    """
    if request.method == 'POST':
        from_currency = request.form.get('from_currency', '').upper()
        to_currency = request.form.get('to_currency', '').upper()
        amount_str = request.form.get('amount', '')
        
        # Validate inputs
        errors = False
        
        if not is_valid_currency(from_currency):
            flash(f"Invalid currency code: {from_currency}")
            errors = True
            
        if not is_valid_currency(to_currency):
            flash(f"Invalid currency code: {to_currency}")
            errors = True
            
        if not is_valid_amount(amount_str):
            flash("Not a valid amount")
            errors = True
            
        if errors:
            return render_template('index.html')
        
        # Perform conversion
        amount = float(amount_str)
        converted_amount, symbol = convert_currency(from_currency, to_currency, amount)
        
        return render_template(
            'index.html', 
            result=True,
            from_currency=from_currency,
            to_currency=to_currency,
            amount=amount,
            converted_amount=converted_amount,
            symbol=symbol
        )
        
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5050)
