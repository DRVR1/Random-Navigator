## important updates on its way !

# USAGE

1) Grab a lot of websites you would like to "visit", that has some HREF (links) in their's HTML code

2) list those websites in the file "inputsites.txt" (the "/" at the end of the URL doesnt matter)

3) execute generator.py from its folder

4) there will be generated a file called "randomsites.txt" that has a list of all the links displayed inside the before listed sites.

5) execute visitor.py

## what is navigator?
navigator is a bot, that uses your browser to search all those sites one by one, before visiting another site.

## Why would you need this?

Beacuse its cool to watch how your computer search random sites like there was a ghost

To simulate browsing activity like a human, you could modify all the "randomsites.txt" list) and increase the time it stays in the site.

## what config is avaliable?

### config section of visitor.py:

#### you can change the used browser

driver = webdriver.Chrome()

driver = webdriver.Edge()

driver = webdriver.Firefox()

#### Change the ammount of time the bot stays in a random time in seconds

# Requirements: 

bs4==0.0.1

requests==2.28.2

selenium==4.7.2

