#!/usr/bin/env python
"""This program grabs a joke from the internet and if you like it, saves it in a file. You can look at the jokes you liked"""
__author__ = "Ken Vanden Branden"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "kenvdb@gmail.com"
import requests # To make http requests
import sys # to exit the programm
import urllib3 #to disable certificate check on web requests
import json #to parse the jokes coming from the joke-website.
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
jokesUri = "https://v2.jokeapi.dev/joke/Programming"
infinite_loop = True #infinite loop variable to redraw the menu until user exits
#Grabbing the joke
def get_Joke(jokeUri):
    uri = jokeUri
    print(uri)
    try:
        #print("\n---\nGET %s?%s"%(jokeUri))
        resp = requests.get(uri,verify=False)
        return resp
    except:
        print("Status: %s" % resp.status_code)
        print("Response: %s" % resp.text)
        sys.exit()
#Parsing the joke
def parse_Joke(data):
    joke            = data
    if joke["type"] == "twopart":
        jokeresp    = "Question:\n {} \n\n\n\n\n\n\n\n\n\nAnswer:\n {} \n".format(joke["setup"],joke["delivery"])
        return jokeresp
    else:
        jokeresp    = "Joke:\n {} \n".format(joke["joke"])
        return jokeresp
#Providing simple menu for the user
def menu():
    multiline_menu= "Menu\n" \
                    "1: Do you want to hear a joke?\n"\
                    "2: Let me show you the jokes you liked\n"\
                    "3: Exit\n"\
                    "Your choice: "
    val = input(multiline_menu)
    return val
#Handling user input.
def menuchoice(val):
    if val == "1":
        resp = get_Joke(jokesUri) 
        json_data       = resp.json()
        responsemessage = parse_Joke(json_data)
        print(responsemessage)
        savejoke(responsemessage)
    elif val =="2":
        readjoke()
    elif val =="3":
        print("Thank you for laughing, goodbye!")
        sys.exit()
    else:
        print("Print this is not a correct choice, please try again\n")
# Save jokes to a file
def savejoke(writejoke):
    responsemessage = writejoke
    question = input("Do you want to save the joke? y/n: ")
    if question =="y":
        print("Saving joke...\n")
        with open("savedjokes.txt",'a') as file:
            file.write(writejoke)
    elif question =="n":
        print("OK, back to main menu it is then...\n")
    else:
        print("Please answer with y or n:")
        savejoke(responsemessage)
# Read joke from the file.
def readjoke():
        print("Here are the jokes you liked: \n")
        try:
            with open("savedjokes.txt",'r') as file:
                data = file.read()
                print(data)
        except:
            print("Can't read or find \"savedjokes.txt\" You probably didn't save any jokes yet.\n")
#Start of the programm
while infinite_loop:
    val = menu()
    menuchoice(val)
