import speech_recognition as sr
import pyttsx3
import google 

google.api_key = "AIzaSyAA3SLU_ZQR_8GbmufAbUsKCe0-turHi1Ur"



def speakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

r= sr.Recognizer()



def record_text():
    while(1):
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source,duration=0.2)
                print('I am listening')
                audio2= r.listen(source)
                myText = r.recognize_google(audio2)

                return myText
        except sr.RequestError as e:
            print('Could not request results: {0}'.format(e))
        except sr.UnknownValueError:
            print("Unknown error has occured")





def send_to_chatGPT(messages,model='gpt-3.5-turbo'):
    response = google.ChatCompletion.create(
        model=model,
        messages=messages,
        max_tokens=100,
        n=1,
        stop = None,
        temperature = 0.5,
    )

    message = response.choices[0].message.content
    messages.append(response.choices[0].message)
    return message



messages = [{"role":"user","content":"please act like jarvis from iron man"}]
while(1):
    text = record_text()
    messages.append({"role":"user","content":text})
    response = send_to_chatGPT(messages)
    speakText(response)

    print(response)


