import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibary
import requests
import random
engein=pyttsx3.init()
def speak(text):
    voices = engein.getProperty('voices')
    engein.setProperty('voice', voices[1].id)
    engein.say(text)
    engein.runAndWait()

newapi="48353340582449289f62ad3ff77940ae"
def commendpass(c:str):
   print(c.lower())
   if "open google" in c.lower():
      webbrowser.open("http://www.google.com")
   elif "open youtube" in c.lower():
      webbrowser.open("https://www.youtube.com")
   elif "open facebook" in c.lower():
      webbrowser.open("http://www.facebook.com")
   elif c.startswith("play"):
      song=c.lower().split(" ")[1]
      link=musiclibary.music[song]
      webbrowser.open(link)
   elif "news" in c.lower():
      ran=random.randint(1,10)
      r=requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newapi}")
      if r.status_code == 200:
    # Parse the JSON response
       data = r.json()
     
    # Fetch the title of the first article
      if data['articles']:
        first_article_title = data['articles'][ran]['title']
        speak(first_article_title)



if __name__=="__main__":
    speak("jarvis is running")

#inisilation jarvis
while True:
  r = sr.Recognizer()
  try:
     print("lisining.......")
     with sr.Microphone() as soures:
        audio=r.listen(soures,timeout=2,phrase_time_limit=1)
        print("recognition...")
        word=r.recognize_google(audio)
        print(word)
     if(word.lower()=="hey jarvis" or word.lower()=="jarvis" or  word.lower()=="chintu"  ):
        speak("how can i help you..")
        print("jarvis is active.")
        # listion for commend..
        print(" in lisining.......")
        with sr.Microphone() as soures:
              audio=r.listen(soures,timeout=3)
              print("in recognition...")
              commend=r.recognize_google(audio)
              print(commend)
              commendpass(commend)
        
  except Exception as e:
     print(f"This is a error:{e}")
    
     