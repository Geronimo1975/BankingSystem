import re

def validate_username(username):

    # Exemple valid username: 'user123', 'user_name', 'user-name'
    return bool(re.match(r'^[A-Za-z0-9]{3,}$', username))

def validate_password(password):

    #Example valid password: 'Password123!', 'Password123', 'password1234567890'
    return bool(re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$', password))

def validate_phone_number(phone):

    # Exemple to validate phone numbers: '+1234567890', '+1234567890123', '+123456789012345'
    return bool(re.match(r'^\+\d{10,15}$', phone))
