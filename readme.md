# USAGE

Grab a lot of websites you like, that has some HREF (links) in their's HTML code

list those websites in the file "inputsites.txt", separated by a jump of line like this:
https://www.wikipedia.org/\n
https://www.google.com\n
https://www.example.com/\n
the "/" at the end doesnt matter

execute generator.py from its folder

there will be generated a file called "randomsites.txt" that has a list of all the links displayed inside the before listed sites.

execute visitor.py

## what is visitor?
visitor is a bot, that uses your browser to search all those sites one by one, before visiting another site.

## Why would you need this?
-Beacuse its cool to watch how your computer search random sites like there was a ghost

## what config is avaliable?

config section of visitor.py:

you can change the used browser
driver = webdriver.Chrome()
driver = webdriver.Edge()
driver = webdriver.Firefox()

Change the ammount of time the bot stays in a random time in seconds
