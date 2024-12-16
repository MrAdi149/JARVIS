# file path to the chat log file
chat_log_file = "C:\\Users\\KIIT\\Desktop\\adi\\mini_project\\Database\\chat_log.txt"

from transformers import pipeline, set_seed, AutoConfig

from Body.speak import Speak
from Body.listen import MicExecution

import os

set_seed(42)  # for reproducibility

config_path = "C:\\Users\\KIIT\\Desktop\\adi\\mini_project\\Brain\\file.json"
config = AutoConfig.from_pretrained(config_path, cache_dir=None)
generator = pipeline(
    "text-generation",
    model=config_path,
    config=config,
    tokenizer="GPT2LMHeadModel",
)


def ReplyBrain(question, chat_log=None):
    # read the chat log from the file
    with open(chat_log_file, "r") as f:
        chat_log_template = f.read()

    if chat_log is None:
        chat_log = chat_log_template

    prompt = f"{chat_log}You: {question}\nMoni: "
    prompt = prompt[:2000]  # truncate the prompt to a maximum length of 2000
    response = generator(
        prompt,
        max_length=1024,  # set max length to a fixed value
        temperature=0.5,
        do_sample=True,
    )[0]["generated_text"]
    answer = response.strip()

    # write the updated chat log to the file
    chat_log_template_update = f"{chat_log_template}\nYou : {question} \nMoni : {answer}"
    with open(chat_log_file, "w") as f:
        f.write(chat_log_template_update)

    return answer


def open_whatsapp():
    os.startfile(
        "C:\\Users\\KIIT\\AppData\\Local\\Packages\\5319275A.WhatsAppDesktop_cv1g1gvanyjgm\\WhatsApp\\WhatsApp.exe")


while True:
    kk = MicExecution()
    kk = str(kk)

    if "Open Camera" in kk:
        pp = "Ok sir.. Camera is opened"
        Speak(pp)

    elif "Open WhatsApp" in kk:
        qq = "Opening WhatsApp"
        Speak(qq)
        open_whatsapp()

    else:
        reply = ReplyBrain(kk)
        Speak(reply)
        print(reply)
