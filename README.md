# Search Stackoverflow with in your Terminal


I find myself always keep the browser open while working on a project, because if I need to find something on the stackoverflow I need to switch to the browser and google it.

Keeping the browser open sometime distract me from my work, whenever I switch to the browser I always check my facebook before switching back to my IDE.

To solve this I created this simple terminal bot that allows me to search for answers in Stackoverflow and look through them without getting distracted. There few commands built into the bot to make navigation easier.


* `!q` or `!quit` or `!exit` - will exit out of the process
* `!b` or `!back` or `!break` - switch to previous page
* `!next` - switch to next page

You can also type an answer number to go to that answer. If press enter without typing anything you will go to the next answer.

> Code snippets are highlighted in green


### Todo

* [ ] store the pages in memory so that when I type `!next` again, I don't have to fetch the page again.
* [ ] ask a new question without leaving the process
