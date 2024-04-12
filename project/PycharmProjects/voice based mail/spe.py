import speech_recognition as sr
import pyttsx3
from gtts import gTTS
global text
import pyglet

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
rate = engine.getProperty('rate')  # getting details of current speaking rate
engine.setProperty('rate', 150)
def spe(text):

    engine.say(text)
    engine.runAndWait()


def tex():
    ans=None
    r = sr.Recognizer()

    with sr.Microphone() as source:
        # print(source)


        print("Listenning........ :")
        audio = r.listen(source,timeout=25,phrase_time_limit=10)
        print('Done, Please wait while we are processing what you said...')
        try:
            text = r.recognize_google(audio)
            text=text.lower()
            ans=text
            print("You said : {}".format(ans))

            return ans
        except:
            # tts = gTTS(text="TRY AGAIN", lang='en')  # voice out
            # ttsname = ("TRY.mp3")  # Example: path -> C:\Users\sayak\Desktop> just change with your desktop directory. Don't use my directory.
            # tts.save(ttsname)
            # music = pyglet.media.load(ttsname, streaming=False)
            # music.play()


            print("Sorry we could not recognize what you said. You can try again.")

    print(ans)

    return ans
a=print(tex)
tex()
spe(a)