# Speech-Controlled WebBrowser

#### Abstract
This project uses Google SpeechRecognition API to recognize what you said, and controlling webiste(only for listening youtube music curently) according to that.


#### Install
```
# pip install SpeechRecognition
# pip install pyaudio
# pip install selenium
# pip install bs4
# pip install BeautifulSoup
```

#### Install ChromeDriver
This project use [chromedriver](http://chromedriver.chromium.org/) in selenium, before running this project, you have to add the downloaded executable file to PATH enviroment variable.

#### Setting
Before running this project, you have to modify the following variable
```
driver = webdriver.Chrome('THE_ABSOLUTE_PATH_OF_CHROMEDRIVER_THAT_YOU_JUST_INSTALLED')
```

#### Trouble Shooting
1. UnicodeWaring: if you encouter this problem, probably you are using python2 instead of python3, because the string generates by ```recognizer.recognize_google(audio)``` is a unicode string instead of bytes string, and the default string format in python2 is bytes string, in the other hand, the default string format in python3 is unicode string. You can convert string to bytes string if you are using python2, or simply use python3 

2. ExecptionHandling: when I use Visual Studio to develope this project, I continiously having trouble while the code should handle the exception, after I use cmd in win10, not having this problem anymore. 

3.  Recognize: if the recognizer continously tring to recognize audio even when you are not speaking, which means that ```recognizer.energy_threshold``` is too low, try to increase that. Otherwise, if the recognizer did not try to recognize what you have said all the time, which means that ```recognizer.energy_threshold``` is too high, so the recognizer considered your voice as ambient noise 


#### Reference
1. [Official SpeechRecognition Github](https://github.com/Uberi/speech_recognition)
