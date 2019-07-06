from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars


# Create Flask instance
app = Flask(__name__)

# PyMongo establishes Mongo connection
mongo = PyMongo(app, uri='mongodb://localhost:27017/mars_app')

# Route to use index.html template with mongo data
@app.route('/')
def home():
    destination_data = mongo.db.collection.find_one()
    return render_template('index.html', mars=destination_data)


# Route that triggers scrape function from scrape_mars.py
@app.route('/scrape')
def scrape():
    mars_data = scrape_mars.scrape_all()
    
    mongo.db.collection.update({}, mars_data, upsert=True)

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
