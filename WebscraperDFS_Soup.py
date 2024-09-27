import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

path = []
target = "https://en.wikipedia.org/wiki/University_of_Maryland,_College_Park"

def scrape(url, depth_left, path):
    if url == target:
        return path
    
    elif depth_left == 0:
        return "This is going nowhere\n"
    
    else:
        try:
            response = requests.get(url, timeout=0.01)
            if response.status_code != 200:
                print(f"Error fetching {url}: Status code {response.status_code}")
                return
            
            soup = BeautifulSoup(response.content, 'html.parser')
            title = soup.title.string if soup.title else 'No Title'
            print(f"Visiting {title} at {url}\n") # print with url

            links = soup.find_all('a', href=True)  # get all anchor tags with href attribute
            # Filter to only Wikipedia article links
            hrefs = [urljoin(url, link['href']) for link in links]
            hrefs_filtered = filter(lambda x: x.startswith("https://en.wikipedia.org/wiki/") and not ((x in url) or (url in x)), hrefs)

            for href in hrefs_filtered:
                print(f"Attempting to visit {href}\n")
                return scrape(href, depth_left - 1, path + [href])
        
        except Exception as e:
            print(f"Error fetching {url}: {e}")

if __name__ == "__main__":
    start_url = 'https://en.wikipedia.org/wiki/Association_for_Computing_Machinery'  # starting url
    max_depth = 10  # recursion limit

    # Start the scraping process
    scrape(start_url, max_depth, [])