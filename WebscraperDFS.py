# Import necessary libraries

import requests  # to handle HTTP requests
from bs4 import BeautifulSoup  # to parse HTML content of web pages
from urllib.parse import urljoin  # to join relative URLs to the base URL

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
            response = requests.get(url, timeout=0.05)
            
            # If the response status code is not 200 (OK), print an error message and stop
            if response.status_code != 200:
                print(f"Error fetching {url}: Status code {response.status_code}")
                return
            
            # Parse the HTML content of the page using BeautifulSoup
            # BeautifulSoup has several webpage parsers that converts the contents of the webpage,
            # In this case the raw html code, and converts it to an easy to reference and read object
            # lxml and html5lib are also good options but html.parser is built into python and is good
            # enough for our purposes
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Get the page's title if available; otherwise, assign 'No Title'
            title = soup.title.string if soup.title else 'No Title'
            
            # Print the current page title and URL
            print(f"Visiting {title} at {url}\n")

            # Find all anchor (<a>) tags with the href attribute to get links
            links = soup.find_all('a', href=True)
            
            # Create a list of full URLs by joining the base URL with relative links
            hrefs = [urljoin(url, link['href']) for link in links]
            
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
    
    # Maximum recursion depth
    max_depth = 10

    # CHANGE THESE AS YOU PLEASE
    def filter_func(next_url,current_url,path,title):
        return next_url.startswith("https://en.wikipedia.org/wiki/") and not ((next_url in current_url) or (current_url in next_url))

    # Start the scraping process from the start_url with the specified maximum depth
    scrape(start_url, max_depth, [], filter_func, target)