import requests
from urllib.parse import quote
from bs4 import BeautifulSoup
import sys, os

from spidy.spidy import Spidy


def main():
    inp = input("Question ? ") + " Stackoverflow"
    urls = []
    for u in Spidy("https://www.google.com/search?q={}".format(quote(inp))).css("a[href^='/url?q=']").attr("href"):
        url = u.split("?q=")[-1]
        if url.find("stackoverflow.com") > -1:
            urls.append(url)

    fetch_answers(urls, needle=0)


def fetch_answers(urls, needle=0):
    url = urls[needle]
    boxes = Spidy(url).css(".answer .post-text")
    codes = boxes.css("code").text()

    for i, el in enumerate(boxes.css("code")):
        el.text(colored(194, 235, 10, codes[i]))

    answers = boxes.text()

    count = 0
    while True:
        if count >= len(answers):
            count = 0

        os.system('cls')
        print(answers[count])
        inp = input("\n#{} ({}/{}): ".format(needle+1, count+1, len(answers)))
        os.system('cls')

        if inp == "!q" or inp == "!quit" or inp == "!exit":
            sys.exit(0)
        elif inp == "!b" or inp == "!back" or inp == "!break":
            break
        elif inp == "!next":
            fetch_answers(urls, needle=needle+1)
        elif inp.strip() == "":
            count += 1
        else:
            try:
                count = int(inp) - 1
            except: pass


def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


if __name__ == "__main__":
    main()
