**Issue Tracker**

**Overview**

-   Unicorn Attractor is a Bug and Feature reporting tool where users can report any issues encountered in the system or can request new features
-   Bug fixes are free of charge however new features require payment (the amount is set by system admin and users can contribute towards it with an amount of their choice (min. £5))
-   The app contains two main sections (bugs and features) which users can browse trough , report a bug, upvote , comment, edit or delete bug(as long as the user is the author), request a new feature , contribute towards one or edit feature(as long as the user is the author)
-   The app also makes use of a shopping cart which will withold the features and allow user to remove an item or adjust the amount of money paid towards a certain feature
-   All items make use of pagination (bugs, features, comments, contributors) and filtering items based on their properties (author , current status, keyword match)

**1. Planning**
1.1 User stories
1.2 Planing Development Steps
1.3 Set out requirements 
1.4 Created Wireframes

**2. UX **

AIMS:
-   Our Main Goal is to provide the end user with a system which enables control over what our app presents and how it behaves

**2.1 User Stories**
** As a User I would like to:**    
-   know the scope of the app
-   have easy accessible navigation items
-   be able to browse trough without an account
-   be able to create a profile and upload a picture
-   be able to reset my password
-   view my profile
-   edit my profile
-   be able to report a bug or request a new feature
-   be able to give feedback to current items
-   be able to see the item’s current status
-   be able to filter items based on their particularities( status, author)
-   see other user’s feedback
-   search an item by title or description
-   be able to contribute towards implementing new features
  
**3 Features:**

-   Welcome page containing a brief description of the app    
-   Navigation Items with buttons relevant to current page
-   User authentication
-   User profile (created automatically when new user registers)
-   Bug reporting (including create, edit, comment, upvote, delete)
-   Feature request (including create and contribute)
-   Search used to filter queries based on various criteria (keyword, status, author) (search input is dynamically displayed throughout the app according to user’s current position)
-   Cart used to collect items user has contributed towards and allowing user to change the amount
-   Checkout used to finalize purchase
-   
** Potential Features **

-   Delete Feature (Currently, system will crash(for user who has feature in cart) due to inconsistency between django session and database (option removed))
-   More Filtering Options (date, properties like amount of views, upvotes, comments, contributors)
-   Profile View (for other than owner)
-   Messages between users
-   Item Report (comments , bugs, features)
-   Notifications (email or section in app) informing users of any recent events
-   E-mail validation (when user changes personal email address) 

**4 Technologies Used :**

-   HTML - markup language
    
-   CSS – used to style content
    
-   Bootstrap 4 – makes use of bootstrap's prebuild functions and used to style elements
    
-   Python / Django – Back-end code has been written in python using django framework
    
-   Javascript – the project uses javascript to provide functionality for StripeAPI (platform used to process payments )
    
-   Font Awesome – the project makes use of font awesome’s icons to style content
    
-   Whitenoise – used to collect static files in one place (S3 bucket)
    
-   AWS S3 bucket – used to host our static files for deployed version
    
-   SQLite3 – database use in development
    
-   PostgreSQL – database used in deployed version
    
-   Psycopg2 – PostgreSQL database adapter for python
    
-   GIT / GitHub – version control and code backup
    
-   Heroku – platform used to deploy and host our project
    
-   Balsamiq – used to create wireframes

**5 Testing:**
**5.1 Automated Testing**
-   Within this application tests have been carried out using Django TestCase testing tools , coverage and continous integration with travis
-   Travis Status ([![Build Status](https://travis-ci.org/toderas/Issue-Tracker.svg?branch=master)](https://travis-ci.org/toderas/Issue-Tracker)) 

 **5.2   Manual Testing**
    
-   Manual testing has been carried out thoroughly for each new piece of functionality at the time of implementation
- Some scenarios can be found  [Here](https://github.com/toderas/Issue-Tracker/blob/master/tests/manual-tests/README.md)
    

The app looks as intended and operates accordingly on all popular browsers (Google Chrome, Mozilla Firefox, Opera , Safari , Internet Explorer

**6 Deployment :**

App deployed on Heroku

Deployment steps:

-   On heroku create new app
-   Add PostgreSQL database (heroku-resource-addons)
-   Created Procfile
-   Whithin heroku dashboard click Deploy and then connect to github repository
-   Click Settings and then reveal Config Vars and add secret keys , database url, email address email password
-   Added deployed app's url to allowed hosts in master/settings.py
-   Comment out “import env” (content has been moved to Config Vars)
-   Set Debug to False
-   Migrate (using heroku cli)
-   Settings to host static files on S3bucket (AWS)
-   Create new superuser (using heroku cli)

**7 Code Validators:**

- [CSS Validator](https://jigsaw.w3.org/css-validator/validator) : Css code passes with no errors or warnings
- [Pep8 Online](http://pep8online.com/): Python code passes with no errors or warnings (appart from some length related warnings but given the fact that git-hub code review length is 130 characters this shoud not cause any issues )
- [HTML Validator](https://validator.w3.org/): Html Code passes W3C validator with no issues or warnings (appart from the ones caused by jinja)


**Acknowledgements :**

- Base Code For this project has been imported from a previous project [E-commerce](https://github.com/toderas/e-commerce)  and modified to suit current project’s requirements
- Stack Overflow users have helped me with code related issues
- Friends have helped me with usability tests and user stories 
- [Bugs](https://qa-platforms.com/most-common-bugs-in-mobile-application/) Content used on deployed version for presentation pourposes
