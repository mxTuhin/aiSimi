import nltk
# nltk.download('punkt')
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import numpy
import tflearn
import tensorflow
import random
import json
import pickle

#Voice Assistant Imports

import speech_recognition as sr
import cv2
import pyglet
from time import ctime
import time
import os
from gtts import gTTS
from subprocess import call
from subprocess import Popen

#Voice Assitant Imports
tensorflow.reset_default_graph()

with open("intents.json", encoding='utf-8') as file:
    data = json.load(file)

with open("data.pickle", "rb") as f:
    words, labels, training, output = pickle.load(f)



net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)

model.load("model.tflearn")


def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w== se:
                bag[i]=1

    return numpy.array(bag)

def chat(inp):
    results=model.predict([bag_of_words(inp, words)])
    results_index=numpy.argmax(results)
    tag=labels[results_index]
    for tg in data["intents"]:
        if tg['tag'] == tag:
            responses = tg['responses']
    answer=random.choice(responses)
    speak(answer)
    print(answer)

def speak(audioString):
    # print(audioString)
    tts = gTTS(text=audioString, lang='bn')
    tts.save("audio.mp3")
    # os.system("mpg321 audio.mp3")
    playPyglet()

def playPyglet():
    music = pyglet.resource.media('audio.mp3')
    music.play()

def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio, language='bn-BD')
        # data = r.recognize_google(audio, language='en')
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return data
# initialization
# time.sleep(5)

while True:
    dataX = recordAudio()
    chat(dataX)
