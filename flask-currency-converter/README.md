# Flask Currency Converter

A simple web application that converts currency using the exchangerate.host API.

## Project Structure

```
flask-currency-converter/
├── app.py                  # Main Flask application
├── currency_utils.py       # Helper functions for currency conversion
├── conceptual.md           # Answers to conceptual questions
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
├── static/
│   └── style.css           # CSS styles for the application
├── templates/
│   ├── base.html           # Base template with common HTML structure
│   └── index.html          # Main page template with form
└── tests/
    ├── test_app.py         # Tests for Flask routes
    └── test_currency_utils.py  # Tests for utility functions
```

## Setup and Installation

1. Clone the repository (or unzip the project files)
2. Navigate to the project directory
3. Create a virtual environment:
   ```
   python3 -m venv venv
   ```
4. Activate the virtual environment:
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```
   - On Windows:
     ```
     venv\Scripts\activate
     ```
5. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

1. Ensure your virtual environment is activated
2. Start the Flask development server:
   ```
   python app.py
   ```
3. Open your web browser and navigate to `http://127.0.0.1:5000/`

## Running Tests

To run the tests, execute the following command:
```
pytest
```

Or to run tests with more verbose output:
```
pytest -v
```

## Features

- Convert between different currencies using the exchangerate.host API
- Input validation for currency codes and amount
- Display of conversion results with proper currency symbols
- Error handling for invalid inputs

## API Used

This application uses the [exchangerate.host](https://exchangerate.host) API for currency conversion.
