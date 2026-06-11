import speech_recognition as sr


def speech_to_text(audio_path):

    recognizer = sr.Recognizer()

    try:

        with sr.AudioFile(audio_path) as source:

            audio = recognizer.record(source)

        text = recognizer.recognize_google(audio)

        return text

    except sr.UnknownValueError:

        return "Could not understand audio."

    except sr.RequestError:

        return "Speech Recognition service unavailable."

    except Exception as e:

        return f"Error: {e}"