# ChessOpeningWebScraper
A simple web scraper for testing chess opening knowledge

# Disclaimers and Warnings
+ Never use a web scraper for purposes outside of normal website use (at risk of having your IP blocked).
+ I have no affiliation with the website that I am scraping in this repository, but I doubt anyone will have a problem with its use.
+ Scraping is a product of the current state of a website and can easily become outdated/broken upon the update of a website.
+ Chess move popularity will vary from database to database (and I've chosen the one that I thought was best).
+ Link to the opening explorer: https://www.365chess.com/opening.php

# Running this code on your machine:
1. Have a functioning Python 2.7+ version installed
2. Make sure that Beautiful Soup is installed and working properly (urllib2, bs4, and lxml are all needed)
3. Clone this repository
4. Open a terminal and cd into src
5. Run python and import main
6. Run either main.move\_test() or main.index\_test()

# Explanation of the Tests
+ Each test will start at the opening position of chess and play a move.
+ The move it plays is random and proportional to the popularity of that move (for example, if a position has been reached 100 times, a move that has been played 50 times will have a 50% chance of being selected while a move that has been played only 10 times will have a 10% chance of being selected).
+ Depending on the test you have selected, the program will tell you either the move itself or the index of its popularity.
+ Whichever you are given, you must input the other to pass the test (ie. '1. e4' => 1 or 'Move Choice 1' => '1. e4')
+ For inputing the index, simply the number will pass.
+ For inputing the name of the move, you must enter a string that matches perfectly (including the single quotes and the move number).
+ The test will continue until you either get an answer wrong, or you've reached the end of the positions that the website will supply.
