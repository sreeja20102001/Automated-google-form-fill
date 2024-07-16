Documentation: Automating Google Form Submission with Selenium

Objective: To automate the process of filling out and submitting a Google form using the Selenium library in Python.

Tools and Libraries
  •	Python
  • Selenium
  •	Google Chrome
  •	ChromeDriver
Steps
  1.	Setup ChromeDriver Path:
  •	Downloaded the appropriate version of ChromeDriver.
  •	Extracted the downloaded file.
  •	Noted the path to chromedriver.exe.
  2.	Installed Selenium and imported the required libraries:
  3.	Define Form Data: Create a dictionary containing the data to be filled in the form:
      input_data = {
          'Full_Name': 'Sreeja Bhattacharya',
          'Contact_Number': '90623XXXX',
          'Email_Id': 'sreejasrp22@gmail.com',
          'Full_Address': '63 Thakurdas Babu Lane',
          'Pin Code': '712201',
          'Date_of_Birth': '20-10-2001',
          'Gender': 'Female',
          'Code': 'GNFPYC'
      }


4.	Initialized WebDriver:
  •	Specified the path to ChromeDriver.
  •	Initialized the Chrome WebDriver.

    driver_path = r'C:\Users\Sreej\Downloads\chromedriver-win64\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=driver_path)
6.	Open the Google Form:
  •	Provided the URL of the Google form.
  •	Used the WebDriver to open the form:

  form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSdUCd3UWQ3VOgeg0ZzNeT-xzNawU8AJ7Xidml-w1vhfBcvBWQ/viewform'
  driver.get(form_url)
  time.sleep(3)  # Wait for the page to load
6.	Located and Filled Form Fields:
  •	Used XPaths to locate form fields.
  •	Filled each form field with corresponding data:
  
  name_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
  name_field.send_keys(input_data['Full_Name'])
  Repeated for other fields:
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
    
Submited the Form:
    •	Located the submit button using its XPath.
    •	Clicked the submit button:
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit_button.click()
7.	Closed the WebDriver:
    •	Ensured the WebDriver closes properly:
        driver.quit()

