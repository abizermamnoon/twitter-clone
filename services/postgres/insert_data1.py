from tqdm import tqdm
import faker
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

# Define characters for alphanumeric string generation
alphanumeric_chars = string.ascii_letters + string.digits

# Function to generate random alphanumeric strings
def generate_random_alphanumeric(length):
    return ''.join(random.choice(alphanumeric_chars) for _ in range(length))

# Function to generate random users
def generate_users(num_users):
    for i in tqdm(range(num_users), desc="Generating Users"):
        user_id = i + 1
        username = generate_random_alphanumeric(10)  # Adjust length as needed
        password = generate_random_alphanumeric(12)  # Adjust length as needed
        age = random.randint(18, 80)
        connection.execute("INSERT INTO users (username, password, age) VALUES (%s, %s, %s)", (username, password, age))
        print("user",i)

generate_users(10000000)
def generate_tweet_urls(num_tweet_urls):
    for i in range(num_tweet_urls):
        tweet_id = i
        url_id = num_tweet_urls - i
        try:
            connection.execute("INSERT INTO tweet_urls (id_tweets, id_urls) VALUES (%s, %s)", (tweet_id, url_id))
            print("tweet_url", i)
        except IntegrityError as e:
            # Handle the case where the record already exists
            print(f"Skipping duplicate tweet_url: {tweet_id}, {url_id}")

generate_tweet_urls(1100000)

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

