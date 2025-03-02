import os
import logging
import json
import random
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.DEBUG)

def generate_death_prediction(name, birth_year, description):
    # Load pre-generated responses from JSON file
    with open('responses.json', 'r') as file:
        responses = json.load(file)
    
    # Randomly select a response
    response = random.choice(responses)
    
    # Customize the response with the user's details
    response['name'] = name
    response['birth_year'] = birth_year
    response['description'] = description
    
    return json.dumps(response)

if __name__ == "__main__":
    try:
        prediction = generate_death_prediction("John Doe", 1990, "Loves adventure and technology")
        print(prediction)
    except Exception as e:
        print(f"Error: {e}")