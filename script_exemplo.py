from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from recaptcha_solver import RecaptchaSolver  # Supondo que o arquivo seja nomeado como recaptcha_solver.py

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--start-maximized")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get('https://app.hugme.com.br')  # Substitua pela URL real onde deseja resolver o reCAPTCHA

solver = RecaptchaSolver(driver)
solver.solve_recaptcha(
    captcha_iframe_xpath='/html/body/div[1]/div/div[1]/section/form/div[3]/div/div/iframe',
    captcha_button_xpath='/html/body/div[2]/div[3]/div[1]/div/div/span/div[1]',
    audio_challenge_iframe_xpath='/html/body/div[3]/div[4]/iframe',
    audio_button_id='recaptcha-audio-button',
    audio_source_xpath='/html/body/div/div/div[7]/a',
    audio_response_id='audio-response',
    verify_button_id='recaptcha-verify-button'
)

driver.quit()
