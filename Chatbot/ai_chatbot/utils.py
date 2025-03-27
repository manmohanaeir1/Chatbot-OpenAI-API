import openai
from datetime import datetime, timedelta
import re

import os
openai.api_key ='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'  # Ensure you set this environment variable

def get_answer(message: str) -> str:
    try:
        # Send request to OpenAI's updated Completion API
        response = openai.Completion.create(
            model="gpt-3.5-turbo",   
            prompt=message,
            max_tokens=100,   
            temperature=0.7   
        )

        # Extract the response content
        answer = response['choices'][0]['text'].strip()
        return answer
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
