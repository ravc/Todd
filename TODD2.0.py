import speech_recognition as sr
import os

r = sr.Recognizer()
m = sr.Microphone()

with m as source: r.adjust_for_ambient_noise(source)
print('Minimum Threshold {}'.format(r.energy_threshold))
while True:
    try:
        with m as source: audio = r.listen(source)
        try:
            value = r.recognize_google(audio)
            if value[0:4].lower() == 'open':
                for line in open('path/to/text/file.txt', 'r'):
                    if line[0:len(value[5:])].lower() == value[5:].lower():
                        print('"' + line[len(value[5:])+2:] + '"')
                        os.system('"' + line[len(value[5:])+2:-1] + '"')
        except sr.UnknownValueError:
            print('unknown')
            pass
        except sr.RequestError as e:
            print('server error')
            pass
        pass
    except KeyboardInterrupt:
        pass
    pass
