# Webscraper-Workshop

## Overview
Welcome to the Wikipedia Game Webscraper Workshop codebase for ACM@UMD! This repository contains Python scripts designed for Automating the Wikipedia Game using web scraping and various graph algorithms.

## Getting Started
#### 1. Create project directory
Open your terminal or command prompt IN ADMIN

Create a new directory for the workshop

`mkdir webscraper-workshop`

`cd webscraper-workshop`

#### 2. Set up a virtual environment
Create a virtual environment 

`python -m venv ACMworkshop` (you can substitute another name for ACMWorkshop)

(If you get an error on this step you probably do not have python installed run: `python` without any arguments to install it)

Windows: `ACMWorkshop\Scripts\activate`

macOS/Linux: `source ACMWorkshop/bin/activate`

(If you get an error on this step run `Set-ExecutionPolicy RemoteSigned`)

#### 3. Clone the repo
If you have git installed: 

`git clone https://github.com/The-ACM-UMD/Webscraper-Workshop.git`

Otherwise:

Download the code for this workshop: 
Windows: `Invoke-WebRequest -Uri https://github.com/The-ACM-UMD/Webscraper-Workshop/archive/refs/heads/main.zip -OutFile Webscraper-Workshop.zip`
Mac: `curl -L -o Webscraper-Workshop.zip https://github.com/The-ACM-UMD/Webscraper-Workshop/archive/refs/heads/main.zip`

Unzip the code:
Windows: `Expand-Archive -Path Webscraper-Workshop.zip -DestinationPath ./Webscraper-Workshop`
Mac: `unzip Webscraper-Workshop.zip`

Finally: `cd Webscraper-Workshop`

#### 4. Install Dependencies
`pip install -r requirements.txt`

#### 4.5. Open in file explorer
On Windows: `explorer .`

On Mac: `open .`

#### 5. Open the code
`code WebscraperDFS.py` <- to open code in VSCode, you can also simply use open or notepad instead of code to open it in a txt file (on Mac use `open -a TextEdit WebscraperDFS.py`)

Alternatively you can use the editor of your choice to open it from the file explorer window that we opened in the last step

#### 6. Run the script being shown
`python WebscraperDFS.py`

## Project Structure
The code base consists of three main scripts, each implementing a different web scraping strategy. Each is more advanced than the last and will be released in ten minute intervals
#### WebscraperDFS
A recursive link-following web scraper that continues navigating through links until its locates the target link. 
#### WebscraperBFS 
Implements a Breadth-First Search (BFS) approach to scraper using a queue.
Every link is now added to a visited set and the scraper cross references this set to make sure it isn't revisiting it's path
#### WebscraperAStar
Similar to the BFS scraper, but uses a heuristic which evaluates how many words from a user-defined list appear in the link or page description.
Example: If the heuristic list includes ["University", "ACM", "Maryland"], a link description like "ACM at University of Minnesota" would yield a heuristic score of 2. The higher the score ,(and the lower the path length is so far), the more priority is given to searching that link first.

### Expected Output
When running any of the following implementations above you should see a similar output to this :
`Visiting Category:Accuracy disputes from February 2019 - Wikipedia at https://en.wikipedia.org/wiki/Category:Accuracy_disputes_from_February_2019`

However you may experience some time out errors like: 
`Error fetching https://en.wikipedia.org/wiki/Category:Tracking_categories: HTTPSConnectionPool(host='en.wikipedia.org', port=443): Read timed out. (read timeout=0.5)`

If you are seeing both outputs, then proceed to the challenge!

## Challenge
Find the shortest path, least number of links, from the UMD Wikipedia page to the ACM Wikipedia page.

Implement your own algorithms, there are a number of ways to improve the default scraping function in main, such as implementing better heuristics and better filtering. If you're confident in your coding abilities you can even change the scrape function as you wish!

The person with the shortest path at the end of the workshop wins some ACM merch!
