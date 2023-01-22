from bs4 import BeautifulSoup
import requests

#Grab a lot of websites you like, that has some HREF (links) in their's HTML code


class crawler():
    def scrape(self,site):
        list = []
        r = requests.get(site)
        s = BeautifulSoup(r.text,"html.parser")
        ev = s.find_all('a')
        for x in ev:
            href = x.attrs['href']
            #href="#some-id" would scroll to an element on the current page such as <div id="some-id">. 
            #href="//site.com/#some-id" would go to site.com and scroll to the id on that page. 
            if (href.startswith("/") or href.startswith("#")): #invalid link
                continue
            list.append(href)
        return list
        

    # calling function
    def generate(self,sites, howmuchlinks=False):
        '''
        sites: a list of websites, for example https://www.wikipedia.org/
        howmuchlinks: how much links will be extracted for each website
        '''
        output_list = []
        for site in sites:
            print("searching: " + site)
            list = self.scrape(site)
            max = len(list)
            if(max==0):
                print(site + ' is empty, searching another site')
                continue
            i=0
            while(i<max):
                if(howmuchlinks):
                    if(i==howmuchlinks):
                        break
                obtained = list[i]
                if(obtained != '#'): # A hash - `#` within a hyperlink specifies an HTML element id to which the window should be scrolled. 
                    output_list.append(obtained)
                    print("found at index "+str(i)+': ' + obtained)
                i+=1
        return output_list

