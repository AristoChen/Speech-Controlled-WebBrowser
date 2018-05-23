import speech_recognition as sr
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
import json

driver = webdriver.Chrome('C:\Users\jj251\Desktop\chromedriver\chromedriver.exe')
driver.get('https://www.youtube.com')

recognized_result = ""

def speech_to_text(recognizer, audio):
    #r = sr.Recognizer()
    #with microphone as source:
    print("Recognizing...")
        #audio = recognizer.listen(source)
    
    #result = recognizer.recognize_google(audio, language="zh_TW")
    global recognized_result
    
    try:
        recognized_result = recognizer.recognize_google(audio)
        #print type(recognizer.recognize_google(audio))
        print("Google thinks you said : ") + recognized_result
    except sr.UnknownValueError:
        print("Google could not understand audio")
    except sr.RequestError as e:
        print("Google error; {0}".format(e))

    #return recognized_result

def search_youtube_song(recognized_result):
    input = driver.find_element_by_id('search')
    input.send_keys(recognized_result)

    driver.find_element_by_id('search-icon-legacy').click()

    delay = 5 # seconds
    try:
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'result-count')))
        print("Page is ready!")
    except TimeoutException:
        print("Loading took too much time!")
    time.sleep(5)
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    song_list = soup.find_all('a', id='video-title')
    for song in song_list:
        #print song.text.lower().find(recognized_result)
        if song.text.lower().find(recognized_result) != -1:
            driver.get('https://youtube.com' + song['href'])
            print('Enjoy the music called: ' + song.text)
            break

def microphone_calibration(recognizer, microphone):
    with microphone as source:
        print("Please wait. Calibrating microphone...") 
        recognizer.adjust_for_ambient_noise(source, duration=5) 
        print("Microphone is now calibrated")

if __name__ == '__main__':
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    microphone_calibration(recognizer, microphone)
    background_listening = recognizer.listen_in_background(microphone, speech_to_text)
    
    trigger = 0

    while True:
        #recognized_result = speech_to_text(recognizer, microphone)
        #print trigger
        if recognized_result != "":
            print(recognized_result)
        if recognized_result.lower().find("ok google") != -1:
            print("What can I do for you? ")
            trigger = 1
        
        elif recognized_result.lower() == "break" and trigger == 1:
            print("See you next time!")
            driver.quit()
            
        elif recognized_result and trigger == 1:
            search_youtube_song(recognized_result)
            trigger = 0
        time.sleep(0.5)
    

    
