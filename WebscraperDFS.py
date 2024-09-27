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
            driver.implicitly_wait(0.01) # time driver waits for page to load

            title = driver.title # current page title
            print(f"Visiting {title} at {url}\n") # print with url

            links = driver.find_elements(By.TAG_NAME, 'a') # we get all elements in the webpage that have the tag 'a', i.e anchor elements/hyperlinks
            # Filter to only Wikipedia article links
            hrefs = [link.get_attribute('href') for link in links if link.get_attribute('href')]
            hrefs_filtered = filter(lambda x: x.startswith("https://en.wikipedia.org/wiki/") and not ((x in url) or (url in x)), hrefs)
            print(hrefs_filtered)

            for href in hrefs_filtered:
                print(f"Attempting to visit {href}\n")
                return scrape(href, depth_left - 1, driver, path + [href])       
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


