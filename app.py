from flask import Flask, render_template, request
import speech_recognition as sr
import pyttsx3

app = Flask(__name__)

def capture_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please say something")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print("You said: " + text)
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError:
            print("Could not request results; check your network connection.")

def text_to_speech(text, voice_id=None):
    engine = pyttsx3.init()
    if voice_id:
        engine.setProperty('voice', voice_id)
    engine.say(text)
    engine.runAndWait()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    if file:
        text = capture_voice()
        if text:
            text_to_speech(text)
            return text
    return "Error processing the file"

if __name__ == "__main__":
    app.run(debug=True)
