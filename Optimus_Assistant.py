from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui
from PyQt5.uic import loadUiType
from threading import Thread
import speech_recognition as sr
import os
import pyttsx3
import webbrowser
import pywhatkit
import datetime
import wikipedia
import pyjokes
import requests
import cv2
from OPTIMUS_UI import Ui_Optimus
import sys
import random
import datetime
import psutil
import pyautogui
import pywikihow
from twilio.rest import Client
import subprocess


class Main(QMainWindow):
    def __init__(self):
        print("Initializing Main...")
        super(Main, self).__init__()

        try:
            self.ui = Ui_Optimus()
            self.ui.setupUi(self)
            self.ui.movie = QtGui.QMovie("C:/Users/sanga/Downloads/Siri.gif")
            self.ui.label.setMovie(self.ui.movie)
            self.ui.movie.start()  # Start the GIF when the GUI loads
            self.ui.pushButton.clicked.connect(self.startTask)
            self.ui.pushButton_2.clicked.connect(self.close)
            self.listening_flag = False
        except Exception as e:
            print(f"Initialization error: {e}")
            raise

        # Initialize speech recognition and text-to-speech
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()

    def speak(self, text):
        self.ui.textBrowser.append(text)
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source,duration=2)
            print("Capturing audio...")
            audio = self.recognizer.listen(source, timeout=10, phrase_time_limit=10)
            

        try:
            print("Recognizing...")
            query = self.recognizer.recognize_google(audio, language="en-in")
            print(f"You said: {query}")
            return query.lower()
        # except Exception as e:
        #     import traceback
        #     traceback.print_exc()
        #     print(f"Error in recognition: {e}")
        #     return None
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that. Could you repeat?")
            return None
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return None
        except Exception as e:
            print(f"Error in recognition: {e}")
            return None

    def run_jarvis(self):
        print("Entering run_jarvis...")
        print("OPTIMUS PRIME")
        self.engine.setProperty('rate', 150)
        self.speak("HUMANS")
        self.engine.setProperty('rate', 120)
        self.speak('I am Optimus Prime...')
        self.engine.setProperty('rate', 110)

        def jarvis_thread():
            try:
                while self.listening_flag:
                    self.handle_command()
            except Exception as e:
                print(f"Error in jarvis_thread: {e}")
                self.listening_flag = False
                self.ui.movie.stop()

        # Start a separate thread for continuous execution
        self.thread = Thread(target=jarvis_thread)
        self.thread.start()

    def startTask(self):
        print("Starting task...")
        try:
            self.listening_flag = True
            self.run_jarvis()
        except Exception as e:
            print(f"Error in startTask: {e}")
            self.listening_flag = False
            self.ui.movie.stop()

    def closeEvent(self, event):
        # Stop the GIF when closing the window
        self.ui.movie.stop()
        event.accept()

    def handle_command(self):
        self.command = self.listen()
        print(self.command)
        if self.command:
            if 'play' in self.command:
                song = self.command.replace('playing', '')
                self.speak('playing ' + song)
                pywhatkit.playonyt(song)
            elif 'time' in self.command:
                time = datetime.datetime.now().strftime('%I:%M %p')
                self.speak('Current time is ' + time)
                print(f"Current time is: " + time)
            elif 'who the heck is' in self.command:
                person = self.command.replace('who the heck is', '')
                info = wikipedia.summary(person, 1)
                print(info)
                self.speak(info)
            elif 'date' in self.command:
                self.speak('sorry, I have a headache')
            elif 'are you single' in self.command:
                self.speak('I am in a relationship with wifi')
            elif 'joke' in self.command:
                self.speak(pyjokes.get_joke())
            elif 'open' in self.command:
                for site in [["youtube", "https://www.youtube.com"], ["google", "https://www.google.com"],
                             ["wikipedia", "https://www.wikipedia.com"], ["instagram", "https://www.instagram.com"],
                             ["spotify", "https://open.spotify.com"]]:
                    if f"open {site[0]}".lower() in self.command.lower():
                        self.speak(f"opening {site[0]}...")
                        print(f"Opening {site[0]}...")
                        webbrowser.open(site[1])
            elif 'weather' in self.command:
                self.speak("Sure, which city's weather would you like to know?")
                city = self.listen()
                if city:
                    weather_info = get_weather(city)
                    self.speak(weather_info)
            elif 'camera' in self.command:
                self.speak("Opening the camera...")
                self.open_camera()
            elif 'exit' in self.command:
                self.speak("Thank You!, Good Bye!")
                self.listening_flag = False
            elif 'where am i' in self.command:
                self.speak('please wait sir, let me check')
                try:
                    ipAdd = requests.get('https://api.ipify.org').text
                    print(ipAdd)
                    url = 'https://get.geojs.io/v1/ip/geo/' + ipAdd + '.json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    city = geo_data['city']
                    country = geo_data['country']
                    self.speak(f'Sir currently we are in {city} city of {country} country')
                except Exception as e:
                    self.speak('Sorry sir, I am not able to find the current location')
                    pass
            elif 'instagram profile' in self.command:
                self.speak('Sir please enter the username correctly..')
                name = input('enter the ussername here: ')
                webbrowser.open(f'www.instagram.com/{name}')
                self.speak('Sir here is the instagram profile')
                self.time.sleep(5)
                self.speak('Sir would you like to download profile picture?')

            elif 'battery' in self.command:
                battery = psutil.sensors_battery()
                percentage = battery.percent
                self.speak(f"Sir our system have {percentage} percent battery")


            elif 'activate search engine' in self.command:
                from pywikihow import search_wikihow
                self.speak('Search engine is activated sir tell me what to do')
                how = self.listen()
                max_results = 1
                how_to = search_wikihow(how, max_results)
                assert len(how_to) == 1
                how_to[0].print()
                print(how_to[0].summary)

            elif 'volume up' in self.command:
                pyautogui.press('volumeup')

            elif 'volume down' in self.command:
                pyautogui.press('volumedown')

            elif 'volume mute' in self.command:
                pyautogui.press('volumemute')

            elif 'volume ummute' in self.command:
                pyautogui.press('voulmeunmute')

            elif 'make a call'.lower() in self.command.lower():
                print("received")
                self.speak('Calling ...')

                from twilio.rest import Client

                account_sid = "AC2dec79537f7670dbb88850a65986aa95"
                auth_token = "c16fcb078e38a67a472b65359253dcc7"
                client = Client(account_sid, auth_token)

                call = client.calls.create(
                    url="http://demo.twilio.com/docs/voice.xml",
                    twiml='<Response><say>i am optimus prime the king of transforms</say></Resonse>',
                    to="+917975070214",
                    from_="+13129574983"
                )
                print(call.sid)
                sys.exit()

            elif 'send message'.lower() in self.command.lower():
                print("received")
                self.speak('sending message ...')

                from twilio.rest import Client

                account_sid = 'AC00030600def55972c59f7300b98a0021'
                auth_token = '875403b8464dc5bf2de5f84f0a08cde0'
                client = Client(account_sid, auth_token)

                message = client.messages.create(
                    from_='whatsapp:+14155238886',
                    body='THIS IS OPTIMUS PRIME',
                    to='whatsapp:+919035531011'
                )

                print(message.sid)
            else:
                self.speak('Please say the command again')

    def open_camera(self):
        # Add logic to open the camera using OpenCV
        # For example, you can use cv2.VideoCapture(0) to open the default camera
        # Remember to install OpenCV using: pip install opencv-python
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            cv2.imshow('Camera', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()


def get_weather(city):
    print("Received")
    base_url = "https://api.openweathermap.org/data/2.5/weather?q="
    response = requests.get(base_url + city + "&appid=" + 'd1d10dd217f80c0077dda159cc374372')
    weather_data = response.json()
    if response.status_code == 200:
        main_weather = weather_data['weather'][0]['description']
        temperature = weather_data['main']['temp']
        return f"The weather in {city} is {main_weather} with a temperature of {temperature} degrees Celsius"
    else:
        return "Sorry, I couldn't retrieve the weather information"


if __name__ == "__main__":

    try:
        app = QApplication(sys.argv)
        optimus = Main()
        optimus.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(f"An error occurred: {e}")
