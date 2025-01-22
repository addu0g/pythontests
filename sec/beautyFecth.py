from bs4 import BeautifulSoup
import requests

class WebScraping:
    def print_website_content(self, url) -> None: 
       request = requests.get(url) 
       soup = BeautifulSoup(request.content, 'html5lib')
       for link in soup.find_all('a'):
           print(link.get('href')) 

if __name__ == "__main__": 
    web_scraping_content = WebScraping() 
    print("Enter a URL" )
    res = input('Which website do you want to analyze?')
    if 'http://' in res or 'https://' in res:
        web_scraping_content.print_website_content(res)
    else:
        print("Make sure you are using http or https.")
    