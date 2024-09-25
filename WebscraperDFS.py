from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.parse import urljoin, urlparse
import time # used in case we get hit by anti ddos measures

path = []
target = "https://en.wikipedia.org/wiki/University_of_Maryland,_College_Park"

def scrape(url,depth_left,driver,path):
    if url == target:
        return path
    
    elif depth_left == 0:
        return "This is going nowhere\n"
    
    else:
        try:
            driver.get(url)
            driver.implicitly_wait(0.5) # time driver waits for page to load

            title = driver.title # current page title
            print(f"Visiting {title} at {url}\n") # print with url

            # This block is currently bugged, need a better way to make sure this is scraping links off of the wikipedia body and not just random hrefs
            links = driver.find_elements(By.TAG_NAME, 'a') # we get all elements in the webpage that have the tag 'a', i.e anchor elements/hyperlinks

            for link in links:
                absolute_url = urljoin(url, link.get_attribute('href')) # most urls in wikipedia are relative therefore we must get the url (href) and then join it with our current url to get the absolute url
                # couldn't really figure out a better way to do this but this essentially makes sure the domain of the url we're going to is 
                # the same as the url we're on, this prevents it from going off wikipedia
                if urlparse(absolute_url).netloc == urlparse(url).netloc: 
                    return scrape(absolute_url, depth_left - 1, driver, path.append(absolute_url))       
        except Exception as e:
            print(f"Error fetching {url}: {e}")

if __name__ == "__main__":
    start_url = 'https://en.wikipedia.org/wiki/Association_for_Computing_Machinery'  # starting url
    max_depth = 10  # recursion limit

    # Set up the WebDriver
    driver = webdriver.Chrome()

    try:
        scrape(start_url, max_depth, driver,[])
    finally:
        driver.quit()


