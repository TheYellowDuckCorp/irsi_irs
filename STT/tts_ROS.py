from time import sleep

import rospy
import speech_recognition as sr

import control_uav

r = sr.Recognizer()
rospy.init_node("JESUS_DRONE")
control_uav.setMode("GUIDED")
sleep(2)

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Escuchando...")
    while True:
        try:
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio, language="es-MX")
                text = text.lower() + "."
                print(text)
                if text == "levántate." or text == "levántate.":
                    control_uav.setArm()
                    sleep(2)
                    control_uav.setTakeofMode()
                    sleep(5)
                    print("Escuchando...")
                if text == "siéntate." or text == "siéntate.":
                    control_uav.setLandMode()
                    sleep(15)
                    control_uav.setMode("GUIDED")
                    sleep(2)
                if text == "adiós." or text == "adiós.":
                    break
            except sr.UnknownValueError:
                print("Esperando dictado...")
        except KeyboardInterrupt:
            break
