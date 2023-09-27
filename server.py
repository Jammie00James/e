from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options

app = Flask(__name__)

# Initialize the scheduler
scheduler = BackgroundScheduler()

# Define a route that triggers your Selenium script
@app.route('/run_selenium')
def run_selenium():
    # Your Selenium script goes here
    # You can call the script or function that performs the web automatio
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)
    
    # Replace 'path/to/chromedriver.exe' with the actual path to your WebDriver
    
    # Open a web page
    driver.get('https://waeup.uniben.edu/@@login')  # Replace with the URL of the webpage you want to open
    
    # Locate the username and password fields and the login button and interact with them
    username_field = driver.find_element(By.ID,'login')  # Replace 'username' with the actual name of the username input field
    password_field = driver.find_element(By.ID,'password')  # Replace 'password' with the actual name of the password input field
    login_button = driver.find_element(By.NAME,'SUBMIT')  # Replace 'login' with the actual name of the login button
    
    # Enter your credentials
    username_field.send_keys('B1139345')
    password_field.send_keys('537268')
    
    # Submit the form (assuming it's a standard login form)s
    login_button.click()
    
    # Wait for a few seconds (you may need to adjust the sleep duration)
    time.sleep(2)
    driver.get('https://waeup.uniben.edu/students/B1139345/accommodation/add')
    
    code = driver.find_element(By.NAME,'ac_series')
    code2 = driver.find_element(By.NAME,'ac_number')
    con = driver.find_element(By.NAME,'SUBMIT')
    
    
    code.send_keys('0')
    code2.send_keys('1931225407')
    
    con.click()
    
    # Close the browser
    driver.quit()

    return "Selenium script executed successfully"

if __name__ == '__main__':
    # Start the scheduler to run the script every hour
    scheduler.add_job(func=run_selenium, trigger="interval", hours=1)
    scheduler.start()

    # Run the Flask app
    app.run(host='0.0.0.0', port=5000)
