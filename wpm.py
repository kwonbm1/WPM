import time
import requests

url = "https://random-word-api.herokuapp.com/word?number="
length = input("How long do you want the phrase to be? ")
url += length
response = requests.get(url)
phrase = response.text.strip('[]').replace("'", "").replace(",", "")

wordCount = len(phrase.split())
phrase = phrase.strip('"')
phrase = phrase.split('""')
finalPhrase = ""
for word in phrase:
    finalPhrase += word + " "
finalPhrase = finalPhrase.strip()
begin = input("Type the following phrase and press enter:\n" + finalPhrase + "\nPress enter when ready.\n")

t0 = time.time()
attempt = input("\n")
t1 = time.time()
attemptTime = (t1 - t0) / 60

wpm = str(round(wordCount / attemptTime, 2))

if attempt == finalPhrase:
    print("\nCongratulations! Your WPM: " + wpm)
else:
    print('\nTyped incorrectly. Please try again.')