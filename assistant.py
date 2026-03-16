import streamlit as st
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# ---------- Background Style ----------
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        background-size: cover;
    }

    h1 {
        text-align: center;
        color: navy blue;
        font-size: 45px;
    }

    .stButton>button {
        background-color: #4CAF50;
        color: navy blue;
        font-size: 18px;
        border-radius: 10px;
        padding: 10px 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------- Title ----------
st.title("🎤 Simple Voice Assistant")

recognizer = sr.Recognizer()

# initialize engine once
engine = pyttsx3.init()


def speak(text):
    try:
        engine.stop()
        engine.say(text)
        engine.runAndWait()
    except:
        pass


def listen_command():
    with sr.Microphone() as source:
        st.info("Listening...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        return command.lower()

    except:
        return "sorry i did not understand"


def process_command(command):

    if "hello" in command:
        response = "Hello, how can I help you?"

    elif "time" in command:
        now = datetime.datetime.now().strftime("%H:%M")
        response = f"The time is {now}"

    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        response = "Opening Google"

    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        response = "Opening YouTube"

    else:
        response = "Sorry I cannot perform that task"

    speak(response)

    return response


# ---------- Button ----------
if st.button("🎤 Start Listening"):

    command = listen_command()

    st.write("You said:", command)

    response = process_command(command)

    st.success(response)