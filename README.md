# "One For All" Newsletter

"One For All" Newsletter was created solve one problem for avid readers. The problem of wasting time jumping from one site to another to keep updated with the latest news.  

"One For All" Newsletter to allow users to use only one website to view the latest news & articles from several popular magazine/newspaper sites of their choice.

<img src="https://raw.githubusercontent.com/yichen101/Oneforallnewsletter/main/images/Homepage.PNG" width="356" height="200"> <img src="https://raw.githubusercontent.com/yichen101/Oneforallnewsletter/main/images/Tabpages.png" width="356" height="200">

# Pipeline
The Scrapy library is used in Python to scrap articles & links from sites such as the Financial Times, The Telegraph, etc. The scraped data for each site is saved into it's own json file which is then uploaded to Firebase Realtime Database.

Using React, fetch the data via a Firebase API and load the correct data onto the correct page.

<img src="https://raw.githubusercontent.com/yichen101/Oneforallnewsletter/main/images/Pipeline.PNG" width="700" height="270">

# Features
* Each page has the feature to search, a menu bar to quickly scroll to a desired section of the page, and a 'Back to top' button.
* The Home page contains articles across ALL sites, making it the ideal page to use the 'Search' feature.

# Code Files Explained
* The 'python-code' folder contains code for web scraping and uploading data to Firebase.
* The 'react-code' folder contains front-end react code.

# Libraries/Packages to install, enter into terminal
**REACT**:
* To create React app: `npx create-react-app .`
* To run the app in development mode: `npm start` 
* To fetch data from API: `npm install axios`
* To enable routing in app: `npm install react-router-dom`

**PYTHON**:
* To install Scrapy: `pip install scrapy`
* To upload to Firebase: `pip install pyrebase4`

# System information
Platform: Windows-10
