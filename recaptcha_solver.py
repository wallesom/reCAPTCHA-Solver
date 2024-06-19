import os
import urllib.request
import ssl
import time
import speech_recognition as sr
from pydub import AudioSegment

class RecaptchaSolver:
    def __init__(self, driver):
        self.driver = driver

    def download_audio(self, src, dest):
        try:
            _create_unverified_https_context = ssl._create_unverified_context
        except AttributeError:
            pass
        else:
            ssl._create_default_https_context = _create_unverified_https_context

        urllib.request.urlretrieve(src, dest)

    def convert_audio(self, mp3_path, wav_path):
        sound = AudioSegment.from_mp3(mp3_path)
        sound.export(wav_path, format="wav")

    def recognize_audio(self, wav_path):
        recognizer = sr.Recognizer()
        with sr.AudioFile(wav_path) as source:
            audio = recognizer.record(source)
        return recognizer.recognize_google(audio)

    def solve_recaptcha(self, captcha_iframe_xpath, captcha_button_xpath, audio_challenge_iframe_xpath, audio_button_id, audio_source_xpath, audio_response_id, verify_button_id):
        # Access captcha iframe
        self.driver.switch_to.frame(self.driver.find_element('xpath', captcha_iframe_xpath))
        self.driver.find_element('xpath', captcha_button_xpath).click()
        self.driver.switch_to.parent_frame()
        time.sleep(2)

        self.driver.switch_to.frame(self.driver.find_element('xpath', audio_challenge_iframe_xpath))
        self.driver.find_element('id', audio_button_id).click()
        time.sleep(2)

        src = self.driver.find_element('xpath', audio_source_xpath).get_attribute("href")
        print(f"[INFO] Audio source URL: {src}")

        audio_dir = os.path.join(os.getcwd(), 'audio')
        os.makedirs(audio_dir, exist_ok=True)
        mp3_path = os.path.join(audio_dir, "sample.mp3")
        wav_path = os.path.join(audio_dir, "sample.wav")

        self.download_audio(src, mp3_path)
        self.convert_audio(mp3_path, wav_path)
        key = self.recognize_audio(wav_path)
        print(f"[INFO] Audio transcription: {key}")

        self.driver.find_element('id', audio_response_id).send_keys(key)
        self.driver.find_element('id', verify_button_id).click()
        self.driver.switch_to.parent_frame()
        time.sleep(2)

        os.remove(mp3_path)
        os.remove(wav_path)
