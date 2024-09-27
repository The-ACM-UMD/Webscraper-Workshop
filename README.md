# Webscraper-Workshop
Code for the ACM@UMD's webscraper workshop

Notes:
Written in python

Webscraping done using beautifulsoup (selenium turned out to be too slow, however the selenium version is still up and ready to go as a visual demo) (install using pip install)

For DFS the code is finished and it needs to be abstracted, we need to take the current scrape method and split it into two parts, one that takes in the url to search, depth left and the current path and returns a list of href links in the page (all this code is in the current scrape method) and a filter method that filters the hrefs and returns a filtered set of urls (this code is also already in DFS code)

TODO:

code is in four different scripts

WebscraperDFS - A recursive link following webscraper that just keeps going through the first link until it finds the target link - This is mostly finished only abstraction needs to be done

WebscraperBFS - Recursive (Or Queue based) link following webscraper that instead implements Breadth first search, this passes in a visited list at each set that contains a list of visited links to make sure there's no retreading

WebscraperAStar - the same as above but this time implementing a heuristic, the heuristic is how many words in a user defined list the link/page has in it (e.g if a user has a heuristic list of [University, ACM, Maryland] and the webscraper sees a link/link description with the words 
"ACM at University of Minnesota" the heuristic score would be 2) 

WebscraperMThread - A* Webscraper with multithreading

Once you have completed writing and testing a script commit it to main and leave a comment with your name in the script


