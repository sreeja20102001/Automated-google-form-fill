from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# URL of the Google form
form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSdUCd3UWQ3VOgeg0ZzNeT-xzNawU8AJ7Xidml-w1vhfBcvBWQ/viewform'

# Data to be filled in the form
input_data = {
    'Full_Name': 'Sreeja Bhattacharya',
    'Contact_Number': '9062375295',
    'Email_Id': 'sreejasrp22@gmail.com',
    'Full_Address': '63 Thakurdas Babu Lane',
    'Pin Code': '712201',
    'Date_of_Birth': '20-10-2001',
    'Gender': 'Female',
    'Code': 'GNFPYC'
}

# Path to the WebDriver (e.g., ChromeDriver)
driver_path = r'C:\Users\Sreej\Downloads\chromedriver-win64\chromedriver.exe'


# Initialize the WebDriver
driver = webdriver.Chrome(executable_path=driver_path)

try:
    driver.get(form_url)
    time.sleep(3)  # Wait for the page to load

    # Filling in the form fields using the obtained XPaths
    name_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    name_field.send_keys(input_data['Full_Name'])

    contact_number_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    contact_number_field.send_keys(input_data['Contact_Number'])

    email_id_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    email_id_field.send_keys(input_data['Email_Id'])

    full_address_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea')
    full_address_field.send_keys(input_data['Full_Address'])

    pincode_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
    pincode_field.send_keys(input_data['Pin Code'])

    date_of_birth_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')
    date_of_birth_field.send_keys(input_data['Date_of_Birth'])

    gender_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input')
    gender_field.send_keys(input_data['Gender'])

    code_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input')
    code_field.send_keys(input_data['Code'])

    # Submit the form
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit_button.click()

    time.sleep(4)  # Waiting for the form to be submitted
finally:
    # Close the WebDriver
    driver.quit()
