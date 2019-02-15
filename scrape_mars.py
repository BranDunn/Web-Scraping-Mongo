# create scraper function based on jupyter notebook scrape work

#import dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import time
from time import sleep
import pandas as pd
import requests

def init_browser():
    executable_path = {"executable_path": 'chromedriver'}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    #create empty dict to contain all scraped data
    total_scrape_dict = {}


    #scrape Mars New site

    browser = init_browser()
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.find('div', class_="content_title").get_text()
    paragraph = soup.find('div', class_="article_teaser_body").get_text()
    browser.quit()
#store component in total_scrape_dict
    total_scrape_dict['news_title'] = title
    total_scrape_dict['news_text'] = paragraph

    #visit https://www.jpl.nasa.gov/spaceimages/
    #use splinter to navigate site, find and assign (fullsize) url string to variable

    url = 'https://www.jpl.nasa.gov/spaceimages'

    browser = init_browser()

    browser.visit(url)
    time.sleep(2)
    #click 'full image'
    browser.click_link_by_id('full_image')
    # time.sleep(5)
    # browser.click_link_by_partial_text(' actual ')
    # time.sleep(5)
    browser.quit()
    featured_image_url = browser.find_by_tag('img')['src']
#hard coded from previous scrape as nasa.gov has blocked my ip address(too many retries error)
    featured_image_url = 'https://www.jpl.nasa.gov/assets/images/logo_nasa_trio_black@2x.png'

#store component in total_scrape_dict
    total_scrape_dict['featured_image'] = featured_image_url

    #scrape mars weather twitter
    url = "https://twitter.com/MarsWxReport"

    #open browser
    browser = init_browser()

    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    # time.sleep(2)
    mars_weather = soup.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').get_text()
    # time.sleep(2)
    browser.quit()

#store component in total_scrape_dict
    total_scrape_dict['current_weather'] = mars_weather

      
    #use pandas to scrape table Mars Facts page
    url = 'https://space-facts.com/mars/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'lxml')
    table = soup.find('table', class_='tablepress tablepress-id-mars')
    df = pd.read_html(str(table))
    print(df[0].to_json(orient='records'))
    df = df[0]
    df

    #use pandas to convert data to HTML table string
    html_table = df.to_html()

#store component in total_scrape_dict
    total_scrape_dict['mars_facts'] = html_table


    #Use a Python dictionary to store the data using the keys img_url and title

    #Append the dictionary with the image url string and the hemisphere title to a list
    #Save both the image url string for the full resolution hemisphere image, 
    #and the Hemisphere title containing the hemisphere name.



    #create empty list to append with dicts
    hemisphere_image_urls = []

    #open browser
    browser = init_browser()

    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

    products = soup.find("div", class_ = "result-list") 

    hemispheres = products.find_all("div", class_="item")

    for hemisphere in hemispheres:
        title = hemisphere.find("h3").text
        title = title.replace("Enhanced", "")
        end_link = hemisphere.find("a")["href"]
        image = "https://astrogeology.usgs.gov/" + end_link    
        browser.visit(image)
        html = browser.html
        soup=BeautifulSoup(html, "html.parser")
        downloads = soup.find("div", class_="downloads")
        image_url = downloads.find("a")["href"]
        hemisphere_image_urls.append({"title": title, "img_url": image_url})
        
    browser.quit()

#store component in total_scrape_dict
    total_scrape_dict['hemisphere_image_urls'] = hemisphere_image_urls

    return total_scrape_dict


