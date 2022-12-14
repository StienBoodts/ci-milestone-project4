# Seafoam Winter E-commerce Store

This website offers visitors the chance to browse and buy knitwear made by Belgian/Welsh knitter Stien.
The seller can showcase her handmade knitwear and offer a wide choice range to the user.
This website was based on the walk through project 'Boutique Ado' by [Code Institute](https://codeinstitute.net/).

<img src="media/mockup.jpg" width="500"/><br>

## User Experience
---

### _User Stories_

- #### **First Time Visitor Goals:**
1. As a first time user, I want to find out the purpose of the website immediately.
2. As a first time user, I want to find out what products are available.
3. As a first time user, I want to find out how I can buy the products and buy them.

- #### **Returning Visitor Goals:**
1. As a returning user, I want to find out how I can search and filter for specific products.
2. As a returning user, I want to access my profile and view previous orders.
3. As a returning user, I want to access my profile and edit info kept on file.

- #### **Frequent User Goals:**
1. As a frequent user, I want to find out how I can get in touch with the maker for custom orders.


## Features
---

### _Existing Features_

- __Clear Navigation and purpose__

    <img src="media/screen3.png" width="500"/><br>

    Covering user stories: As a first time user, I want to find out the purpose of the website immediately.


- __Product Browsing and Filtering__

    The User can browse the products in many different ways. By collection, filtering and searching.

    <img src="media/screen4.png" width="500"/><br>
    <img src="media/screen5.png" width="500"/><br>
    <img src="media/screen9.png" width="500"/><br>

    Covering user stories: As a returning user, I want to find out how I can search and filter for specific products.


- __User Accounts__

    Users can log in to view their profile address details and previous orders.

    <img src="media/screen1.png" width="500"/><br>

    Covering user stories:
    -   As a returning user, I want to access my profile and view previous orders.
    -   As a returning user, I want to access my profile and edit info kept on file. 

    <img src="media/screen2.png" width="500"/><br>


- __Shopping Bag__

    Users can add products to bag and can view a snippet of the bag whenever new products are added.

    <img src="media/screen6.png" width="500"/><br>

    Covering user stories: As a first time user, I want to find out how I can buy the products and buy them.

     <img src="media/screen7.png" width="500"/><br>


- __About Page__

    Covering user stories: As a frequent user, I want to find out how I can get in touch with the maker for custom orders.

     <img src="media/screen8.png" width="500"/><br>


### _Features Left To Implement_

- __Custom order form__

    A specific order form where users can make custom orders.

## Data Structure
---

The data for the website is stored in 2 places

[Elephant SQL](https://www.elephantsql.com/):

The database is migrated and stored with ElephantSQL. (see deployment section)
It consists of databases Categories and Products, but also all necessary data for the users, orders and authentication procedures.

[AWS S3](https://aws.amazon.com):

Amazon S3 Buckets are used to store static files and media used across the website.

## Technologies Used
---

### _Languages Used_

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [Javascript](https://en.wikipedia.org/wiki/JavaScript)
-   [jQuery](https://en.wikipedia.org/wiki/JQuery)
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### _Frameworks, Libraries & Programs Used_

1. [Django](https://www.djangoproject.com/)
    - Django was used for the structure of the backend.
1. [Bootstrap:](https://getbootstrap.com/docs/5.1/getting-started/introduction/)
    - Bootstrap was used on parts of the website to make them responsive.
1. [Gitpod:](https://gitpod.io/workspaces)
    - Gitpod workspace was used to create and edit code and push them onto the Github repo.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Gitpod.
1. [Heroku](https://www.heroku.com/)
    - Heroku is used to deploy and host the website.
1. [Hover.css:](https://ianlunn.github.io/Hover/)
    - Hover.css was used on to add float effect on buttons.
1. [Google Fonts:](https://fonts.google.com/)
    - Google fonts was used to import the 'Comfortaa' font into the style.css file.
1. [Elephant SQL](https://www.elephantsql.com)
    - Elephant SQL is used to host the database.
1. [AWS](https://aws.amazon.com)
    - AWS S3 is used to store static files like images and files.


## Testing 
---

- [HTML](https://jigsaw.w3.org/css-validator/#validate_by_input)
    No errors, with exception of template logic
- [CSS](https://jigsaw.w3.org/css-validator/validator)
    No errors found
- Manual testing:
    The website was extensively manually tested on different devices in the developing process. The user stories were followed and bugs fixed as I came across them in development: 

    -   Browsed the products using the navigation links and adjusted the order to see if the products re-arrange on the page.
    -   Filtered by colour by clicking on the wool colour, both on home page as on the products page.
    -    Navigated to About Us. Found and fixed bug to send email by clicking on emailaddress.
    -   Tested the navigation menu on mobile. Bug found: no link back to homepage. Fixed by adding a 'Home' link in the hamburger menu.
    -   Logged in as admin, tested CRUD functionality on products and changed personal details to see if they save correctly.
    -   Registered a new account to see if registration emails are received. 
    Clicked on the confirmation link provided to confirm address. Checked Django backend to see if confirmation came through.
    -   Navigated to profile page to see if previous orders show up correctly.
    -   Test Orders were completed, with many different possibilities and information entered to check whether it would throw errors.
    Bug found: images not showing correctly in 'add to cart' toast and on checkout page. The issue was an incorrect url to the image files. The bug was fixed.
    There was also an issue with totals not coming through in the backend, this was a small bug in the signals and has been fixed.
    
    Many smaller bugs were fixed during the development process as I came across them. One of the big issues after deployment was the URLs to the static files on the AWS server. After plenty of digging I finally managed to get the urls linked up correctly.

## Deployment
---

This project was developed on Gitpod, committed to Git and pushed onto the [Github repository](https://github.com/StienBoodts/horizon-animatie-CI-MP2) using Bash. 


##### Hosting of database on ElephantSQL

1. log into [Elephant SQL](https://www.elephantsql.com/)
2. click 'Create New Instance'
3. Give a name and choose the free 'Tiny Turtle' plan, tags can be left blank
4. Select region closest to you
5. click 'Review'
6. then 'Create Instance'
7. return to Elephant SQL database and click database instance for the project
8. copy the database URL
9. Leave tab open, you'll need this in deployment later.

##### Heroku set up for database

1. log into [Heroku](https://www.heroku.com/)
2. Click New to create a new app
3. Give the app a name and select region closest to you
4. Cick 'Create app'
5. Open settings tab
6. Add the config var DATABASE_URL, and for the value, copy in your database url from ElephantSQL
7. Leave tab open, you'll need this in deployment later.

##### Connect the database

1. in the Gitpod terminal, install dj_database_url and psycopg2, both of these are needed to connect to your external database: pip3 install dj_database_url==0.5.0 psycopg2
2. Update your requirements.txt file with the newly installed packages: pip freeze > requirements.txt
3. In your settings.py file, import dj_database_url underneath the import for os
4. Scroll to the DATABASES section and update the code so sqlite3 is commented out and we connect to the new ElephantSQL database instead. Paste in your ElephantSQL database URL. (DO NOT COMMIT)
5. In the terminal, run the showmigrations command to confirm you are connected to the external database
6. Migrate your database models to your new database
7. Load in the fixtures. Please note the order is very important here. We need to load categories first
8. Then products, as the products require a category to be set
9. create a new superuser for your new database
10. to prevent exposing our database when we push to GitHub, delete the url again from our settings.py - set it up using an environment variable
11. On the ElephantSQL page for your database, in the left side navigation, select ???BROWSER???
12. Click the Table queries button, select auth_user
13. When you click ???Execute???, you should see your newly created superuser details displayed. This confirms your tables have been created and you can add data to your database

##### Adjust settings
1. Make sure both databases are connected with an if statement
2. install gunicorn and add it to the requirements
3. Create Procfile
4. log into heroku in the terminal
5. enter heroku config:set DISABLE_COLLECTSTATIC=1 --app with app name added to the end
6. Add host name to Heroku app in allowed host in settings.py (also add local host)
7. Commit and push changes to gitpod
8. initialise heroku app: heroku git:remote -a and name of app
9. push changes to heroku main


##### Set up automatic deployment in Heroku when pushing to Github
1. Go to app in Heroku and navigate to deploy tab
2. Click Connect to github, Search for the repo and Click Connect
3. Enable automatic deploys


## Credits & Resources
---

### _Content_ 


1. [Code Institute](https://codeinstitute.net/)
    - this project was based on the walkthrough project Boutique Ado from Code Institute.
1. [Slack Community]()
    - General trouble shooting to fix bugs in development
1. [https://stackoverflow.com/](https://stackoverflow.com/)
    - General searches to solve issues

### _Media_


1. Developers own :)
