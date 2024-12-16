# Importing necessary libraries
from Body.speak import Speak
from Body.listen import MicExecution
import os
from dotenv import load_dotenv
from cachetools import TTLCache
import openai

# File paths
chat_log_file = "C:\\Users\\KIIT\\Desktop\\adi\\project_training\\Database\\chat_log.txt"
api_file = "C:\\Users\\KIIT\\Desktop\\adi\\project_training\\Data\\Api.txt"

# Read API key from file
with open(api_file, "r") as f:
    api_key = f.read().strip()

# Set up OpenAI API
openai.api_key = api_key

# Load environment variables
load_dotenv()

# Create cache for API responses
cache = TTLCache(maxsize=1000, ttl=600)

# OpenAI model engine
model_engine = "text-davinci-002"

# Create OpenAI completion instance
completion = openai.Completion()


def ReplyBrain(question, chat_log=None):
    # Read the chat log from the file
    with open(chat_log_file, "r") as f:
        chat_log_template = f.read()

    if chat_log is None:
        chat_log = chat_log_template

    # Construct prompt
    prompt = f'{chat_log}You: {question}\nMoni: '

    if prompt in cache:
        answer = cache[prompt]
    else:
        # Make an API call to OpenAI for response
        response = completion.create(
            engine=model_engine,
            prompt=prompt,
            temperature=0,
            max_tokens=500,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0)

        answer = response.choices[0].text.strip()

        # Add response to cache
        cache[prompt] = answer

    # Write the updated chat log to the file
    chat_log_template_update = chat_log_template + f"\nYou : {question} \nMoni : {answer}"
    with open(chat_log_file, "w") as f:
        f.write(chat_log_template_update)

    return answer


def open_whatsapp():
    # Open WhatsApp application
    os.startfile(
        "C:\\Users\\KIIT\\AppData\\Local\\Packages\\5319275A.WhatsAppDesktop_cv1g1gvanyjgm\\WhatsApp\\WhatsApp.exe")


while True:
    # Get user input using microphone
    user_input = MicExecution()
    user_input = str(user_input)

    # Perform actions based on user input
    if "Open Camera" in user_input:
        response = "Ok sir.. Camera is opened"
        Speak(response)

    elif "Open WhatsApp" in user_input:
        response = "Opening WhatsApp"
        Speak(response)
        open_whatsapp()

    else:
        # Get response from the chatbot and speak the answer
        reply = ReplyBrain(user_input)
        Speak(reply)
        print(reply)
