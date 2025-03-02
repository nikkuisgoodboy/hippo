import os
import logging
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, session
from death_predictor import generate_death_prediction
import json

# Configure logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "default_secret_key")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict_death', methods=['POST'])
def predict_death():
    try:
        name = request.form.get('name')
        birth_date = request.form.get('birthDate')
        description = request.form.get('description')

        if not all([name, birth_date, description]):
            return render_template('index.html', error='All fields are required')

        # Convert birth_date to year
        birth_year = datetime.strptime(birth_date, '%Y-%m-%d').year

        # Generate prediction
        prediction = generate_death_prediction(name, birth_year, description)

        # Store prediction in session for the result page
        session['prediction'] = prediction

        # Redirect to the result page
        return redirect(url_for('show_prediction'))

    except Exception as e:
        logging.error(f"Error generating prediction: {str(e)}")
        return render_template('index.html', error='Failed to generate prediction')

@app.route('/prediction')
def show_prediction():
    prediction = session.get('prediction')
    if not prediction:
        return redirect(url_for('index'))
    
    # Parse the JSON string into a Python dictionary
    prediction_data = json.loads(prediction)
    
    return render_template('prediction.html', prediction=prediction_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)