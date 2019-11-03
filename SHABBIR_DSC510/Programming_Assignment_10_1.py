"""
File: Programming_Assignment_10_1.py
Name: Syed Shabbir
Date: 11/03/2019
Course: Introduction to Programming
Assignment#: 10.1

Purpose of the Program

Desc: Create a program which uses the Request library to make a GET request of the following API: Chuck Norris Jokes.
      The program will receive a JSON resp which includes various pieces of data.
      Parse the JSON data to obtain the “value” key.
      The data associated with the value key should be displayed for the user (i.e., the joke).
      The program should allow the user to request a Chuck Norris joke as many times as they would like.
      You should make sure that your program does error checking at this point.
      If you ask the user to enter “Y” and they enter y, is that ok? Does it fail?
      If it fails, display a message for the user. There are other ways to handle this.
      Think about included string functions you might be able to call.
      The program must include a welcome message for the user.
      The program must generate “pretty” output.
      Simply dumping a bunch of data to the screen with no context doesn’t represent “pretty.”

"""

from IPython.display import clear_output
import requests, json, string, random


# Extracts data from website and puts in in a dictionary and returns it back
def gettingDataFromWebsite(url):
    # error handling the website, in case it doesn't work
    try:
        resp = requests.get(url)  # Extracting data from url
        data = resp.json()  # Inserting json data into data
    except:
        print('Please try again!')        # if the website is down or sends bad data flag an error
        data = None                       # insert an empty set
    return data
def getusrresp(isFirstJoke): # Get a resp from the user whether they want to continue
    isCont = True     # used to keep loop for resp going
    validresps = ('y', 'n')     # putting list of correct responses together
    basePrompt = "\nPlease enter y-yes or n-no."  # basePrompt tells the user how to continue
    promptList = ["Do you want to continue?"]    # promptList is a list of questions, asking the user to continue
    errorPromptList = ["Incorrect entry. Please enter y/n to continue"] # errorpromtList is a list of responses for the user if they do not enter y/n.
    # Welcome message for the user
    if isFirstJoke:
        initialPrompt = "Welcome to my program, this program displays instructions on how to return a Chuck Norris joke"
        promptUsr = "{0} {1}\n".format(initialPrompt, basePrompt)
    else:
        promptUsr = "\n{0} {1}\n".format(random.choice(promptList), basePrompt)
    while (isCont == True):     # loop through until the user provides a valid resp
        # error handling the user input
        try:
            usrresp = input(promptUsr)
            assert usrresp.lower() in validresps    # make sure the user entered a y or n
            if (usrresp.lower() == 'y'):            # if resp is y then send back true to continue else return false
                return True
            else:
                return False
        except:
            # let user know they need to choose y/n
            promptUsr = "\n{0} {1}\n".format(random.choice(errorPromptList), basePrompt)

def prettyPrint(data, n):   # Neat and clean the data to look pretty for the user
    clear_output()     # clears the output so it is easier to read the joke
    output = "Joke {0}:  {1}".format(n, data["value"])     # include the joke number
    print(output)

def main():
    # website to pull from
    url = 'https://api.chucknorris.io/jokes/random'
    # Show the number of iterations the user has gone through
    i = 0
    isCont = getusrresp(True)  # Iterate through the loop to keep jokes going

    while isCont:
        data = {}  # construct the data
        data = gettingDataFromWebsite(url)  # retrieving data from website and assign it to data.

        prettyPrint(data, i + 1)
        isCont = getusrresp(False)  # getting permission from user to continue

        i += 1
    # Printing a thanks note to the end user
    print("\nThanks for using my program, I hope you enjoyed Chuck Norris Jokes, please come again :)")


if __name__ == "__main__":
    main()

# End of Program
