import secrets
from tinydb import TinyDB, Query

db = TinyDB('users.json')

def generate_api_key():
    # Generate a random API key using the secrets module
    api_key = secrets.token_hex(16)  # Adjust the length as needed
    
    return api_key

def save_api_key(user_id, api_key):
    # Update the user's record with the generated API key
    User = Query()
    db.update({'api_key': api_key}, User.id == user_id)
