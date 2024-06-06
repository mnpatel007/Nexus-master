from Nexus import NexusAssistant
import re
import os
import random
import pprint
import datetime
import requests
import sys
import urllib.parse
import webbrowser
import pyjokes
import time
import pyautogui
import pywhatkit
import wolframalpha
import subprocess
from PIL import Image
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUiType
from Nexus.features.gui import Ui_MainWindow
from Nexus.config import config

obj = NexusAssistant()

# ================================ MEMORY ===========================================================================================================

GREETINGS = ["hello nexus", "nexus", "wake up nexus", "you there nexus", "time to work nexus", "hey nexus",
             "ok nexus", "are you there", "hi nexus", "okay nexus"]
GREETINGS_RES = ["always there for you sir", "i am ready sir",
                 "your wish my command", "how can i help you sir?", "i am online and ready sir"]

End = ["goodbye nexus", "good bye nexus", "bye nexus", "go offline", "go offline nexus"]
End_Res = ["Alright sir, going offline. It was nice working with you"]

EMAIL_DIC = {
    'myself': 'meetnp007@gmail.com',
    'my official email': 'meetnpatel0808@gmail.com',
    'my second email': 'meet882005@gmail.com',
    'my official mail': 'mnpatel43@myseneca.ca.com',
    'my second mail': 'atharvaaingle@gmail.com'
}

CALENDAR_STRS = ["what do i have", "do i have plans", "am i busy"]


# =======================================================================================================================================================


def speak(text):
    obj.tts(text)


app_id = config.wolframalpha_id
window = QMainWindow

def loc(place):
    import webbrowser
    from geopy.geocoders import Nominatim
    from geopy.distance import great_circle
    import geocoder
    try:
        # Construct the URL
        url = "https://www.google.com/maps/place/" + place
        print(f"Opening URL: {url}")  # Debug statement
        webbrowser.open(url)

        # Initialize the geolocator
        geolocator = Nominatim(user_agent="myGeocoder")

        # Get the location details
        location = geolocator.geocode(place, addressdetails=True)
        if location is None:
            raise ValueError("Location not found")

        # Extract latitude and longitude
        target_latlng = (location.latitude, location.longitude)

        # Extract address details
        location_details = location.raw['address']
        target_loc = {
            'city': location_details.get('city', ''),
            'state': location_details.get('state', ''),
            'country': location_details.get('country', '')
        }
        city = target_loc.get('city', '')
        state = target_loc.get('state', '')
        country = target_loc.get('country', '')

        # Get the current location based on IP
        current_loc = geocoder.ip('me')
        current_latlng = current_loc.latlng

        # Calculate the distance
        distance = great_circle(current_latlng, target_latlng).km
        distance = round(distance, 2)

        # Construct the response
        if city:
            res = f"{place} is in {state} state and country {country}. It is {distance} km away from your current location."
        else:
            res = f"{state} is a state in {country}. It is {distance} km away from your current location."

        print(res)
        speak(res)

    except Exception as e:
        print(e)
        res = "Sir, I have opened it in Google maps for you."
        print(res)
        speak(res)


def my_location():
    try:
        ip_add = requests.get('https://api.ipify.org').text
        url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'
        geo_requests = requests.get(url)
        geo_data = geo_requests.json()
        city = geo_data['city']
        state = geo_data['region']
        country = geo_data['country']
        return city, state, country
    except Exception as e:
        print(e)
        return None, None, None


def open_calculator():
    # Open the calculator app (Windows example)
    try:
        subprocess.Popen('calc.exe')
    except Exception as e:
        print(e)
        speak("Sorry, I couldn't open the calculator app.")


def perform_calculation(query):
    try:
        # Safely evaluate the mathematical expression
        result = eval(query)
        return result
    except Exception as e:
        print(e)
        return None


def take_screenshot(name):
    img = pyautogui.screenshot()
    name = f"{name}.png"
    img.save(name)
    speak("The screenshot has been successfully captured.")
    return name


def show_screenshot(file_path):
    try:
        img = Image.open(file_path)
        img.show()
        speak("Here it is.")
        time.sleep(2)
    except IOError:
        speak("Sorry, I am unable to display the screenshot.")

def whatsapp_message():
    speak("Whom would you like to send the message to?")
    person = obj.mic_input()

    speak("What's the message")
    message =obj.mic_input()


import csv
import webbrowser

def load_contacts(file_path):
    contacts = {}
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            name, phone_number = row
            contacts[name.lower()] = phone_number
    return contacts


def send_whatsapp_message(contact_name, message, contacts):
    from datetime import timedelta,datetime
    contact_name = contact_name.lower()
    if contact_name in contacts:
        phone_number = contacts[contact_name]

        # Calculate target time (1 minute from now)
        now = datetime.now()
        target_time = now + timedelta(minutes=1)
        time_hour = target_time.hour
        time_min = target_time.minute

        pywhatkit.sendwhatmsg(phone_number, message, time_hour, time_min, wait_time=40, print_waitTime=True)
        speak(f"Message sent to {contact_name}.")
    else:
        speak(f"Sorry, I don't have the phone number for {contact_name}.")


def get_system_stats():
    from datetime import datetime
    import psutil
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    battery_percent = psutil.sensors_battery()
    memory_usage = memory_info.percent
    speak(f"Battery percentage is at {battery_percent} percent. ")
    speak(f"Current time and date is {current_time}. ")
    speak(f"CPU usage is at {cpu_usage} percent. ")
    speak(f"Memory usage is at {memory_usage} percent.")


def take_note():
    speak("What would you like to write down?")
    note_content = obj.mic_input()

    speak("By what name should the note be saved?")
    note_name = obj.mic_input()

    date = datetime.datetime.now()
    file_name = f"{note_name}.txt"

    # Write the note content to the file
    with open(file_name, "w") as f:
        f.write(note_content)
    notepad_path = "C:\\Windows\\System32\\notepad.exe"
    subprocess.Popen([notepad_path, file_name])

import cv2
def start_camera():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open camera.")
        speak("Error: Could not open camera.")
        return
    img_counter = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            speak("Failed to grab frame")
            break
        cv2.imshow('Camera', frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('c'):
            speak("what should be the name for the capture?")
            img_name=obj.mic_input()
            img_name = img_name.strip()
            if img_name == "":
                img_name = f"opencv_frame_{img_counter}.png"
            else:
                img_name = f"{img_name}.png"  # Add extension
            cv2.imwrite(img_name, frame)
            print(f"{img_name} written!")
            speak(f"Captured {img_name}")
            img_counter += 1
    cap.release()
    cv2.destroyAllWindows()


def startup():
    speak("Initializing Nexus")
    speak("Starting all systems applications")
    speak("Installing and checking all drivers")
    speak("Caliberating and examining all the core processors")
    speak("Checking the internet connection")
    speak("Wait a moment sir")
    speak("All drivers are up and running")
    speak("All systems have been activated")
    speak("Now I am online")


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good Morning")
    elif hour > 12 and hour < 18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    c_time = obj.tell_time()
    speak(f"Currently it is {c_time}")
    speak("I am Nexus. Online and ready sir. Please tell me how may I help you")

def ask_password(window):
    correct_password = "hi seneca"
    attempts = 3

    speak("Please speak the password to continue")
    while attempts > 0:
        password = obj.mic_input()

        if password == correct_password:
            speak("Password accepted!Welcome")
            return True
        else:
            attempts -= 1
            if attempts > 0:
                speak(f"Incorrect password. {attempts} attempts left. Please try again.")
            else:
                speak("Incorrect password. No attempts left. Exiting...")
                speak("You cannot go ahead.")
                window.close()
# if __name__ == "__main__":


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExecution()

    def TaskExecution(self):
        #startup()
        #ask_password(window)
        #wish()

        while True:
            command = obj.mic_input()

            if re.search('system', command):
                get_system_stats()
                continue

            elif "shutdown" in command:
                speak("Shutting down the system.")
                os.system("shutdown /s /t 1")
            elif "restart" in command:
                speak("Restarting the system.")
                os.system("shutdown /r /t 1")
            elif "log off" in command:
                speak("Logging off the system.")
                os.system("shutdown /l")

            elif "start camera" in command or "open camera" in command or "camera" in command:
                speak("Opening camera.")
                speak("press Q to quit and C to capture")
                print("press Q to quit and C to capture")
                start_camera()
                continue

            elif "make a note" in command or "write this down" in command or "remember this" in command:
                take_note()
                speak("I've made a note of that")
                continue

            elif "close the note" in command or "close notepad" in command:
                speak("Okay sir, closing notepad")
                os.system("taskkill /f /im notepad.exe")
                continue

            elif "take screenshot" in command or "take a screenshot" in command or "capture the screen" in command:
                speak("By what name do you want to save the screenshot?")
                name = obj.mic_input()
                file_path = take_screenshot(name)
                continue

            elif "show me the screenshot" in command:
                speak("Please provide the name of the screenshot file you want to view.")
                name = obj.mic_input()
                file_path = f"{name}.png"
                if os.path.exists(file_path):
                    show_screenshot(file_path)
                else:
                    speak("Sorry, the specified screenshot does not exist.")



            elif "change tab" in command or "switch tab" in command or "switch window" in command or "switch the window" in command:
                speak("Okay sir, switching the window")
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")

            elif "joke" in command:
                joke = pyjokes.get_joke()
                print(joke)
                speak(joke)

            elif re.search('where is ', command):
                place = command.split('where is ', 1)[1]
                loc(place)
                time.sleep(1)

            elif "time" in command:
                time_c = obj.tell_time()
                print(time_c)
                speak(f"Sir the time is {time_c}")
            elif re.search('date', command):
                date = obj.tell_me_date()
                print(date)
                speak(date)

            elif re.search('hide all files', command):
                os.system("attrib +h /s /d")
                speak("Sir, all the files in this folder are now hidden")

            elif re.search("make all files visible", command):
                os.system("attrib -h /s /d")
                speak(
                    "Sir, all the files in this folder are now visible to everyone. I hope you are taking this decision in your own peace")

            elif "whatsapp" in command:
                speak("Sure, whom do you want to message")
                contact_name = obj.mic_input()
                speak("What message would you like to send")
                message = obj.mic_input()
                file_path = "C:\\Users\\DELL\\Downloads\\contacts.csv"
                contacts = load_contacts(file_path)
                send_whatsapp_message(contact_name, message, contacts)


            elif re.search('location', command):
                city, state, country = my_location()
                if city and state and country:
                    print(city, state, country)
                    speak(f"You are currently in {city} city which is in {state} state and country {country}")
                else:
                    speak("Sorry, I couldn't fetch your current location. Please try again.")
                time.sleep(1)

            elif re.search('ip address', command):
                ip = requests.get('https://api.ipify.org').text
                print(ip)
                speak(f"Your ip address is {ip}")

            elif re.search('launch', command):
                dict_app = {
                    'chrome': "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
                    'excel': "C:\\Program Files\\Microsoft Office\\root\\Office16\\excel.exe",
                    'vs code': "D:\\Microsoft VS Code\\Code.exe",
                    'visual studio': "C:\\Program Files\\Microsoft Visual Studio\\2022\\Community\\Common7\\IDE\\devenv.exe",
                }

                app = command.split(' ', 1)[1]
                path = dict_app.get(app)

                if path is None:
                    speak('Application path not found')
                    print('Application path not found')

                else:
                    speak('Launching: ' + app + 'for you sir!')
                    obj.launch_any_app(path_of_app=path)

            elif command in GREETINGS:
                speak(random.choice(GREETINGS_RES))

            elif command in End:
                speak(random.choice(End_Res))
                window.close()
                sys.exit()

            elif re.search('open', command):
                domain = command.split(' ')[-1]
                open_result = obj.website_opener(domain)
                speak(f'Alright sir !! Opening {domain}')
                print(open_result)

            elif re.search('weather', command):
                city = command.split(' ')[-1]
                weather_res = obj.weather(city=city)
                print(weather_res)
                speak(weather_res)

            elif re.search('tell me about', command):
                topic = command.split(' ')[-1]
                if topic:
                    wiki_res = obj.tell_me(topic)
                    print(wiki_res)
                    speak(wiki_res)
                else:
                    speak(
                        "Sorry sir. I couldn't load your query from my database. Please try again")

            elif "buzzing" in command or "news" in command or "headlines" in command:
                news_res = obj.news()
                speak('Source: The Times Of India')
                speak('Todays Headlines are..')
                for index, articles in enumerate(news_res):
                    pprint.pprint(articles['title'])
                    speak(articles['title'])
                    if index == len(news_res) - 2:
                        break
                speak('These were the top headlines, Have a nice day Sir!!..')

            elif "play music" in command or "hit some music" in command:
                music_dir = "F://Songs//Imagine_Dragons"
                songs = os.listdir(music_dir)
                for song in songs:
                    os.startfile(os.path.join(music_dir, song))

            elif 'youtube' in command:
                video = command.split(' ')[1]
                speak(f"Okay sir, playing {video} on youtube")
                pywhatkit.playonyt(video)

            elif "email" in command or "send email" in command:
                sender_email = config.email
                sender_password = config.email_password

                try:
                    speak("Whom do you want to email sir ?")
                    recipient = obj.mic_input()
                    receiver_email = EMAIL_DIC.get(recipient)
                    if receiver_email:

                        speak("What is the subject sir ?")
                        subject = obj.mic_input()
                        speak("What should I say?")
                        message = obj.mic_input()
                        msg = 'Subject: {}\n\n{}'.format(subject, message)
                        obj.send_mail(receiver_email, msg)
                        speak("Email has been successfully sent")
                        time.sleep(2)

                    else:
                        speak(
                            "I coudn't find the requested person's email in my database. Please try again with a different name")

                except:
                    speak("Sorry sir. Couldn't send your mail. Please try again")

            elif re.search('calculate', command):
                query = command.replace("calculate", "").strip()
                if query:
                    result = perform_calculation(query)
                    if result is not None:
                        speak(f"The result is {result}")
                        print(f"The result is {result}")
                    else:
                        speak("Sorry, I couldn't calculate the result.")
                else:
                    speak("Please provide a valid calculation query.")

            else:
                speak("This command is not in my database. Please try another command.")




startExecution = MainThread()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def __del__(self):
        sys.stdout = sys.__stdout__

    # def run(self):
    #     self.TaskExection
    def startTask(self):
        self.ui.movie = QtGui.QMovie("Nexus/utils/images/nexus.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("Nexus/utils/images/initiating.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("Nexus/utils/images/a15hko.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)

    def create_gui(self):
        import tkinter as tk
        from tkinter import messagebox
        root = tk.Tk()
        root.title("Face Detection App")
        root.geometry("300x200")

        start_button = tk.Button(root, text="Start Camera", command=start_camera)
        start_button.pack(pady=20)

        exit_button = tk.Button(root, text="Exit", command=root.quit)
        exit_button.pack(pady=20)

        root.mainloop()


app = QApplication(sys.argv)
Nexus = Main()
Nexus.show()
exit(app.exec_())
