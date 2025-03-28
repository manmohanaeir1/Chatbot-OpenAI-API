import google.generativeai as genai
import os
from dotenv import load_dotenv
import re
from datetime import datetime, timedelta

# Load API Key from .env file (Recommended for security)
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
# Set up Gemini API
genai.configure(api_key=GEMINI_API_KEY)

def get_answer(user_prompt):
    """
    Generates a response from Google's Gemini AI model.
    
    Args:
        user_prompt (str): The user's question or input.

    Returns:
        str: The AI-generated response.
    """
    try:
        model = genai.GenerativeModel("gemini-1.5-pro")   
        response = model.generate_content(user_prompt)
        return response.text.strip() if response.text else "Sorry, I couldn't generate a response."
    
    except Exception as e:
        return f"Error: {str(e)}"


# Function to parse a date input and convert it into a valid date format (YYYY-MM-DD)

def parse_date(date_input):
    """
    Function to parse user input for dates (e.g., 'Next Monday', '2025-03-29', 'Next Friday').
    Returns the date in YYYY-MM-DD format.
    """

    try:
        parsed_date = datetime.strptime(date_input, "%Y-%m-%d").date()
        return parsed_date
    except ValueError:
        pass   

    days_of_week = {
        "monday": 0,
        "tuesday": 1,
        "wednesday": 2,
        "thursday": 3,
        "friday": 4,
        "saturday": 5,
        "sunday": 6,
    }

    date_input = date_input.strip().lower()
    if "next" in date_input:
        for day, day_num in days_of_week.items():
            if day in date_input:
                today = datetime.today()
                days_until_target = (day_num - today.weekday()) % 7
                target_date = today + timedelta(days=days_until_target)
                return target_date.date()

    return None   

def validate_email(email):
    """
    Function to validate email format using regex.
    """
    email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    if re.match(email_regex, email):
        return True
    return False

def validate_phone(phone):
    """
    Function to validate phone number format.
    Example: Validates that phone is 10 digits long.
    """
    phone_regex = r"^\d{10}$"   
    if re.match(phone_regex, phone):
        return True
    return False

