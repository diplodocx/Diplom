import speech_recognition as sr
import soundfile


def recognize():
    r = sr.Recognizer()
    data, samplerate = soundfile.read('tmp.wav')
    soundfile.write('tmp.wav', data, samplerate, subtype='PCM_16')
    harvard = sr.AudioFile('tmp.wav')
    with harvard as source:
        audio = r.record(source)

    text = r.recognize_google(audio, language='ru-RU')
    return text
