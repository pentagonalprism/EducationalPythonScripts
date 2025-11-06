from bs4 import BeautifulSoup
import urllib.request
import re


initial_url = 'http://py4e-data.dr-chuck.net/known_by_Zhuo.html'

class looper:
    def __init__(self, url,pos,num):
        self.url = url
        self.num = num
        self.pos = pos
    
    # Use urllib to make the request to read and decode the body of the webpage. We are looking for <anchor> in the HTML
    def make_request(self):
        lib  = urllib.request.Request(self.url)
        
        
        with urllib.request.urlopen(lib) as response:
            txt = response.read().decode()

        # get all <anchor> in a list
        bs = BeautifulSoup(txt,'html.parser').find_all('a')[self.pos]
        
        return str(bs.get('href'))


    def url_loop(self):
        #initial_input = self.make_request()
        x = [self.url]
        #print(x)
        for i in range(0,self.num):
            x.append(self.make_request())
            #redifine self.url to the latest URL within the for loop.
            self.url = self.make_request()

        #Use regex search to pull the last name from the url string
        return re.search(r'by_([A-z]+)\.html',x[-1]).group(1)
    

#Define the parameters of the query
query = looper(initial_url,17,7)

#print the output
print(query.url_loop())
