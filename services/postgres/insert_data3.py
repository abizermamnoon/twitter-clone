import random
import string
from sqlalchemy.exc import IntegrityError
import string
from sqlalchemy import create_engine

# Database connection URI
db_uri = "postgresql://postgres:pass@localhost:9373"

# Create the database engine
engine = create_engine(db_uri, connect_args={'application_name': 'insert_data.py'})

# Establish a connection
connection = engine.connect()

# Function to read words from dictionary file
def read_dictionary_file(file_path):
    with open(file_path, 'r') as file:
        words = file.read().splitlines()
    return words

# Function to generate a random message
def generate_random_message(words):
    # Select up to 4 random words from the dictionary
    selected_words = random.sample(words, min(4, len(words)))
    message = ' '.join(selected_words)
    return message

# Path to the dictionary file
dictionary_file_path = "dictionary.txt"

# Read words from the dictionary file
dictionary_words = read_dictionary_file(dictionary_file_path)

# Number of messages to generate
num_messages = 1000000
message_list = []
# Generate and insert the random messages
for i in range(num_messages):
    sender_id = i + 1  # Assuming sender IDs range from 1 to num_messages
    if i < 1000:
        message = generate_random_message(dictionary_words)
        message_list.append(message)
    else:
        message = random.choice(message_list)
    print('message:', i)
    connection.execute("INSERT INTO messages (sender_id, message) VALUES (%s, %s)", (sender_id, message))

# Close the connection
connection.close()
