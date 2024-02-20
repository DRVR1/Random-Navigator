# USAGE

1) Grab a lot of websites you would like to "visit", that has some HREF (links) in their's HTML code

2) list those websites in the file "inputsites.txt" (the "/" at the end of the URL doesnt matter)

3) execute: python generator.py

4) there will be generated a file called "randomsites.txt" that has a list of all the links displayed inside the before listed sites.

(alternatively, you can just type your links into randomsites.txt if you want to omit scrapping)

5) configure the time settings in resources/config.py

6) execute: python main.py

## what is navigator?
navigator is a bot, that uses your browser to search all those sites one by one, before visiting another site.

## Why would you need this?

To simulate browsing activity, in random or not random websites.

When using a vpn, this adds a layer of privacy, getting difficult to hackers from using an end-to-end confirmation attack. Remember that you will need to obfuscate package sizes.

# Requirements: 

bs4==0.0.1

requests

selenium==4.7.2

fake-useragent==1.1.1

pyperclip==1.8.2

PyAutoGUI==0.9.53

pynput==1.7.6

# tested in windows 11 and ubuntu 22.04

## linux specific requirements

sudo apt install xclip

sudo apt install python3-tk

sudo apt install python3-dev

# CLI
![cli](https://i.imgur.com/V1liKkf.png)
