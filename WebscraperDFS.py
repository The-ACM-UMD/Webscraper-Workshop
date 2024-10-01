# Import necessary libraries

import requests  # to handle HTTP requests
from bs4 import BeautifulSoup  # to parse HTML content of web pages
from urllib.parse import urljoin  # to join relative URLs to the base URL
import time

def fetch_with_retry(url, retries=3, delay=1):
    for attempt in range(retries):
        try:
            response = requests.get(url, timeout=1)  # Increased timeout
            if response.status_code == 200:
                return response
        except requests.exceptions.Timeout:
            time.sleep(delay)  # Wait before retrying
    print("Max retries reached. Unable to fetch the URL.")
    return None

# Define a recursive web scraper function
def scrape(url: str, depth_left: int, path: list[str], filter_func, target):
    """
    Recursively scrapes web pages starting from a given URL up to a specified depth, 
    searching for a target URL and printing the path of visited URLs.
    Args:
        url (str): The starting URL to scrape.
        depth_left (int): The remaining depth to continue scraping.
        path (list): The list of URLs visited so far.
        filter_func (function): A function to filter URLs to visit.
        target (str): The target URL to find.
    Returns:
        None
    """
    
    # If the current URL matches the target, return the path of visited URLs
    if url == target:
        print(f"path of length {len(path)} found: {path}")
        quit()
    
    # If the depth limit is reached, stop the recursion
    elif depth_left == 0:
        print("This is going nowhere\n")
        return
    
    else:
        try:
            # Send a GET request to the URL with a timeout of 0.05 seconds
            response = fetch_with_retry(url)

            
            
            # If the response status code is not 200 (OK), print an error message and stop
            # 200 indicates sucessfull connection, the standard 404 error is page not found.
            if response.status_code != 200:
                print(f"Error fetching {url}: Status code {response.status_code}")
                return
            
            # Parse the HTML content of the page using BeautifulSoup
            # BeautifulSoup has several webpage parsers that converts the contents of the webpage,
            # In this case the raw html code, and converts it to an easy to reference and read object
            # lxml and html5lib are also good options but html.parser is built into python and is good
            # enough for our purposes
            # documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/  (very cool!)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Get the page's title if available; otherwise, assign 'No Title'
            # <value_if_true> if <condition> else <value_if_false>
            title = soup.title.string if soup.title else 'No Title'
            
            # Print the current page title and URL
            print(f"Visiting {title} at {url}\n")

            # in html the code we want to scrape looks like this: 
            # <a href="/wiki/Learned_society" title="Learned society">learned society</a>
            # Find all anchor (<a>) tags with the href attribute to get links
            links = soup.find_all('a', href=True)
            
            # Create a list of full URLs by joining the base URL with relative links
            hrefs = [urljoin(url, link['href']) for link in links]

            hrefs = list(set(hrefs)) #converts to  a set then back to a list to remove duplicates

            # Filter the links to only include valid Wikipedia article URLs
            hrefs_filtered = filter(
                lambda x: filter_func(x, url, path, title),  # avoid visiting the same or closely related pages
                hrefs
            )

            # Recursively visit each filtered link
            for href in hrefs_filtered:
                print(f"Attempting to visit {href}\n")
                # Add the current link to the path and continue scraping with reduced depth
                return scrape(href, depth_left - 1, path + [href], filter_func, target)
        
        # Handle any exceptions that occur during the request or scraping process
        except Exception as e:
            print(f"Error fetching {url}: {e}")

# Main block to start scraping
if __name__ == "__main__":

    # The target URL we are trying to reach
    target = "https://en.wikipedia.org/wiki/University_of_Maryland,_College_Park"
    # Starting URL for scraping
    start_url = 'https://en.wikipedia.org/wiki/Association_for_Computing_Machinery'

    # CHANGE THESE AS YOU PLEASE
    max_depth = 10 # Maximum recursion depth
    def filter_func(next_url,current_url,path,title):
        return next_url.startswith("https://en.wikipedia.org/wiki/") and not ((next_url in current_url) or (current_url in next_url))  and next_url not in path

    # Start the scraping process from the start_url with the specified maximum depth
    scrape(start_url, max_depth, [], filter_func, target)