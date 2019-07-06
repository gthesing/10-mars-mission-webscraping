# mars-mission-webscraping
UT data bootcamp webscraping project, using jupyter, BeautifulSoup, Flask, PyMongo, MongoDB, HTML and Bootstrap CSS

The majority of the development for this project was done as a collection of functions in the [mission_to_mars notebook](https://github.com/gthesing/10-mars-mission-webscraping/blob/master/mission_to_mars.ipynb) which was later reformatted into a [python file](https://github.com/gthesing/10-mars-mission-webscraping/blob/master/scrape_mars.py).  Running the app.py file establishes a connection with Mongo and creates a Flask instance. The Flask app references python functions which use BeautifulSoup to scrape data from various websites and store it in the local Mongo database. Finally, the app populates a locally hosted [html page](https://github.com/gthesing/10-mars-mission-webscraping/blob/master/templates/index.html) with images and string stored in the Mongo database. 

![screenshot1](https://github.com/gthesing/10-mars-mission-webscraping/blob/master/images/mars_ss1.JPG)
![screenshot2](https://github.com/gthesing/10-mars-mission-webscraping/blob/master/images/mars_ss2.JPG)

