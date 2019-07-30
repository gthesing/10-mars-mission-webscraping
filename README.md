# mars-mission-webscraping
UT data bootcamp webscraping project, using jupyter, Splinter (abstraction layer built on Selenium), BeautifulSoup, Flask, PyMongo, MongoDB, HTML, and Bootstrap CSS

*****

The majority of the development for this project was done as a collection of functions in the <a href="https://github.com/gthesing/10-mars-mission-webscraping/blob/master/mission_to_mars.ipynb" target="_blank">mission_to_mars notebook</a> which was later reformatted into a <a href="https://github.com/gthesing/10-mars-mission-webscraping/blob/master/scrape_mars.py" target="_blank">python file</a>.  Running the app.py file establishes a connection with Mongo and creates a Flask instance.

The flask app starts by populating a locally hosted [html page](https://github.com/gthesing/10-mars-mission-webscraping/blob/master/templates/index.html) with with images and string stored in the Mongo database.  At the top of the page is a "Click to get current data" button, which when clicked will run various BeatifulSoup scraping functions to update the Mongo database with the most recent data. 

***** 

![screenshot3](https://github.com/gthesing/10-mars-mission-webscraping/blob/master/images/mars_ss3.JPG)
![screenshot2](https://github.com/gthesing/10-mars-mission-webscraping/blob/master/images/mars_ss2.JPG)

