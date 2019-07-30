import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bs

# URLs
url_nasa = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
url_jpl = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
url_weather = "https://twitter.com/marswxreport?lang=en"
url_facts = "https://space-facts.com/mars/"
url_hemispheres = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"


# ### Chromedriver initiation
def init_browser():
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

# ### NASA Mars News Site
def scrape_nasa_mars_news(url):
    
    browser = init_browser()    
    browser.visit(url)
    html = browser.html
    soup = bs(html, "html.parser")
    
    news_title = soup.find(class_="content_title").get_text()
    news_text = soup.find(class_="article_teaser_body").get_text()
    
    news = {
            'news_title': news_title,
            'news_text': news_text
        }
    
    browser.quit()
    
    return news

# ### JPL Featured Space Image
def scrape_jpl_featured_space_image(url):
    
    browser = init_browser()
    browser.visit(url)

    browser.find_by_id('full_image').click()

    html = browser.html
    soup = bs(html, "html.parser")

    image = soup.find(class_='fancybox')['data-fancybox-href']

    featured_image_url = 'https://www.jpl.nasa.gov' + image
    featured_image_url
    
    featured_image = {
        'featured_image_url': featured_image_url
    }
    
    browser.quit()

    return featured_image

# ### Mars Weather
def scrape_mars_weather(url):
    
    browser = init_browser()
    browser.visit(url)
    html = browser.html
    soup = bs(html, "html.parser")

    weather = soup.find("p", class_="tweet-text").get_text()
    
    mars_weather = {
        'mars_weather_tweet_text': weather
    }
    
    browser.quit()
    
    return mars_weather


# ### Mars Facts
def scrape_mars_facts(url):
    
    browser = init_browser()
    browser.visit(url)

    facts = []
    c1 = 0
    c2 = 0
    
    ths = browser.find_by_tag("th")
    tds = browser.find_by_tag("td")

    while c1 < 3:
        facts.append(ths[c1].value)
        c1 = c1 + 1

    while c2 < 18:
        facts.append(tds[c2].value)
        c2 = c2 + 1
        
    mars_facts = {
        'facts_table': facts
    }
    
    return mars_facts

# ### Mars Hemispheres
def scrape_mars_hemispheres(url):

    browser = init_browser()
    browser.visit(url)
    html = browser.html
    soup = bs(html, "html.parser")

    links = []
    for a in soup.find_all('a', class_='itemLink product-item', href=True):
        if a['href'] not in links:
            links.append(a['href'])        

    hemispheres = {}
    
    for link in links:

        path = 'https://astrogeology.usgs.gov' + link
        browser.visit(path)
        soup.clear()
        html = browser.html
        soup = bs(html, "html.parser")

        title  = soup.find('h2').get_text()
        title_temp = title.replace(' Hemisphere Enhanced', '')
        title_clean = title_temp.replace(' ', '_')

        img_url = 'https://astrogeology.usgs.gov' + soup.find(class_='wide-image')['src']
        
        hemispheres[title_clean] = img_url
            
    browser.quit()
    
    return hemispheres

# ### Scrape function
def scrape_all():
    mars_data = {}
    
#     News
    news = scrape_nasa_mars_news(url_nasa)
    mars_data['news'] = news
    
#     JPL
    featured_image = scrape_jpl_featured_space_image(url_jpl)
    mars_data['jpl'] = featured_image
    
#     Weather
    mars_weather = scrape_mars_weather(url_weather)
    mars_data['weather'] = mars_weather
    
#     Facts
    mars_facts = scrape_mars_facts(url_facts)
    mars_data['facts'] = mars_facts
    
#     Hemispheres
    hemispheres = scrape_mars_hemispheres(url_hemispheres)
    mars_data['hemispheres'] = hemispheres
        
    return mars_data
