import requests
from bs4 import BeautifulSoup

class TftDecks:

  def __init__(self):
    """Constructs a new TftDecks object and initializes headers and url attributes."""

    self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}
    self.url = 'https://lolchess.gg/meta'
    self.champs = ['ahri', 'alistar', 'ashe', 'blitzcrank', 'brand', 'braum', 'caitlyn', 'camille', 'chogath', 'corki', 'darius', 'draven', 'ekko', 'ezreal', 'galio', 'gangplank', 'gnar', 'illaoi', 'irelia', 'jarvaniv', 'jayce', 'jhin', 'jinx', 'kaisa', 'kassadin', 'khazix', 'leona', 'lucian', 'lulu', 'malzahar', 'missfortune', 'morgana', 'nocturne', 'orianna', 'poppy', 'quinn', 'reksai', 'renata', 'sejuani', 'senna', 'seraphine', 'silco', 'singed', 'sivir', 'swain', 'syndra', 'tahmkench', 'talon', 'tryndamere', 'twitch', 'veigar', 'vex', 'vi', 'viktor', 'warwick', 'zac', 'zeri', 'ziggs', 'zilean', 'zyra']
    self.champurl = 'https://lolchess.gg/champions/set6.5/'

  
  def search(self):
    """returns a list of strings of all the team compositions listed on the Lolchess.gg website."""

    page = requests.get(self.url, headers = self.headers)

    soup = BeautifulSoup(page.content, 'html.parser') #parses through the html code

    allComps = soup.find_all('div', class_= 'guide-meta__deck__column name mr-3') #refines the search to elements with a 'div' tag with the given class that stores the name of the team composition

    compList = []

    for i in allComps:
  
      compList.append(i.contents[0]) #adds the name of the team comp(the element inside of the tag) to a final list.
    
    finalList = [j.strip() for j in compList] 

    return finalList

  
  def findLink(self, index):
    """takes an integer 'index' as input, uses Beautiful Soup to scrape all of the necessary links on the page, and returns the desired comp from a list of the links as strings using the inputted index."""

    page = requests.get(self.url, headers = self.headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    builderTab = soup.find_all('div', class_= 'guide-meta__deck__column open-builder mr-3')

    allLinks = []

    for i in builderTab: #cleans out unnecessary characters that were scraped
      j = str(i.contents[1]).replace('<a href="', '')
      allLinks.append(j.split('"', 1)[0])
      
    return allLinks[index]

  
  def findItems(self, champ):
      
    page = requests.get(self.champurl + champ, headers =     self.headers)

    soup = BeautifulSoup(page.content, 'html.parser')
  
    itemsTab = soup.find('div', class_= 'guide-champion-detail__recommend-items__content')

    items = itemsTab.find_all('img')

    allItems = []
    for i in items:
      imageLink = i['src']
      imageLink = 'https:' + imageLink
      allItems.append(imageLink)
    
    return allItems