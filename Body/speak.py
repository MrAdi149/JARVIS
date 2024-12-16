# Importing necessary modules from Selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

# Chrome options setup
chrome_options = Options()
chrome_options.add_argument('--log-level=3')  # Setting log level to suppress unnecessary warnings
chrome_options.headless = True  # Running Chrome in headless mode

# Path to ChromeDriver executable
chrome_driver_path = r"C:\Users\KIIT\Desktop\adi\project_training\Database\chromedriver.exe"
# Creating a Service object
chrome_service = webdriver.chrome.service.Service(chrome_driver_path)

# Initializing Chrome driver with the Service object
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
driver.maximize_window()  # Maximizing the Chrome window


# Opening the website for text-to-speech conversion
website = "https://ttsmp3.com/text-to-speech/British%20English/"
driver.get(website)

# Selecting the voice option (US English / Kimberly) from the dropdown
ButtonSelection = Select(driver.find_element(by=By.XPATH, value='//form/select'))
ButtonSelection.select_by_visible_text('US English / Kimberly')


# Function to convert text to speech
def Speak(Text):
    length_of_text = len(str(Text))

    if length_of_text == 0:
        pass
    else:
        # Printing the text to be spoken
        print(f"\nMoni: {Text}\n")

        # Entering the text into the website's textarea and triggering the conversion
        Data = str(Text)
        textarea_xpath = '//form/textarea'
        driver.find_element(By.XPATH, value=textarea_xpath).send_keys(Data)
        driver.find_element(By.CSS_SELECTOR, value='#vorlesenbutton').click()
        driver.find_element(By.XPATH, value=textarea_xpath).clear()

        # Adding sleep delays based on the length of the text to ensure proper processing
        if length_of_text >= 30:
            sleep(4)
        elif length_of_text >= 40:
            sleep(6)
        elif length_of_text >= 55:
            sleep(8)
        elif length_of_text >= 70:
            sleep(10)
        elif length_of_text >= 100:
            sleep(13)
        elif length_of_text >= 120:
            sleep(14)
        else:
            sleep(2)


# Calling the Speak function with an empty string
Speak("")
