# Webscraper-Workshop

## Overview
Welcome to the Webscraper Workshop codebase for ACM@UMD! This repository contains Python scripts designed for web scraping using various algorithms.

## Getting Started
#### 1. Create project directory
Open your terminal or command prompt
Create a new directory for the workshop
`mkdir webscraper-workshop`
`cd webscraper-workshop`

#### 2. Set up a virtual environment
Create a virtual environment 
`python -m venv /path/to/new/virtual/environment`
###### Windows: `venv\Scripts\activate`
###### macOS/Linux: `source venv/bin/activate`

#### 3. Install Dependencies
`pip install BeautifulSoup4 requests`
`pip install selenium`

#### 4. Clone the repo
`git clone` <repository-url>
`cd` <repository-directory>

#### 5. Open the code
`code` <- to open code in VSCode

### Project Structure
The code base consists of four main scripts, each implementing a different web scraping startegy. 
#### WebscraperDFS
A recusive link-following web scraper that continues navigating through links until its locates the target link. 
#### WebscraperBFS 
Implements a Breadth-First Search (BFS) approach to scraper using a queue.
#### WebscraperAStar
Similar to the BFS scraper, but uses a heuristic which evaluates how many words from a user-defined list appear in the link or page description.
Example: If the heuristic list includes ["University", "ACM", "Maryland"], a link description like "ACM at University of Minnesota" would yield a heuristic score of 2.
#### WebscraperMThread
A web scraper that utilizes multithreading to enhance performance and efficiency.

## Challenge
Find the shortest path, least number of links, from the UMD Wikipedia page to the ACM Wikipedia page. 
Implement your own algorithms and use the scraper(keywords (A*),filter) to find the shortest path and scrape(keywords (A*),filter) to find the list of links that match those the path found by scraper().
The person with the shortest path wins some ACM merch!