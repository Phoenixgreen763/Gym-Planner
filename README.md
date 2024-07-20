# Gym-Planner

## Summary

Gym Planner is a web app, that is desgined for users of all ages, who are trying to better their journey of fitness and health. The app consists of an exercise list that allows users to share, or search for exercises if they are inexperienced. It also includes a personal planner with a weekly schedule that they can add exercises to, in order to ensure a smooth and easy gym experience. There is also a communtiy calendar for users to view, if they want to attend classes or events in a gym. The app seeks to give users knowledge and advice on exercises, plan their sessions for the week, and also integrate themselves into the community with events that they may be interested in partaking in.

View the live website here - https://gym-planner-e895d22abc86.herokuapp.com/

![UX Mockup](/static/images/UX.jpg)

## Features 

### Existing features
 
* Navbar
    * Each page of the app displays the same navbar at the top of the page.
    * This navbar includes the app name on the left, which redirects to the landing page of the app.
    * If a user is not currently logged in then 2 seperate links will be present on the navbar, these include a login and a register page.
    * These allow the user to register an account if they do not have one, or if they are a pre-exisitng user, will allow them to login freely.
    * If a user is already logged in, then the navbar will display 4 seperate links instead.
    * These links include exercises, planner, calendar, and logout.

* Landing page
    * The user is initially introduced to the landing page, this displays messages based on if a user is logged in, or if they are not.
    * When a user is not logged in this page will give a welcome message, and invite them to create an account to continue.
    * When a user creates an acount and views this page it will give them a welcome message, and display their username.
    * If a user is logged in, this page will also give them a brief message describing the different uses of the app for ease of use.

* Register page
    * This page allows new users to register an account.
    * This page includes a form to register an account, including the desired username and password of the user.
    * If a user attempts to enter a username that is already in use, a flash message appears to warn them off this, so they can choose a suitable username.
    * If a user enters a unqiue username, there is a register button that will create their accountm and log them in to the site.
    * Underneath the form there is a link for the login page, this allows users with an account to quickly redirect to their desired page.

* Login page
    * This page allows exisiting users to login to their account.
    * Like the register page, login displays a form for users.
    * This form is identical in styling to the register form, except the form button logs the user in, using the pre-exisitng data they created prior.
    * Similar to the register page, underneath the form is a link, this link instead redirects the user to the register page if they do not already have an account.
  
* 

## Design

* Fonts
   * Google fonts were used
   * The font used for all the text is Merienda as it was stylistic, yet maintained readability 

* Color design
    * The colours used, were blue and white. This gives a clean, uniform look to the page.
    * These colors are consistent through the background design, and all the text on page

## Deployment Of The Website

* The website was deployed to Heroku. The steps to deploy are shown, as follows:
    * On the heroku app, navigate to deploy.
    * On the deploy page, select Github as deployment method.
    * Connect the app using the GitHub repository name.
    * Allow automatic deployments, this will push through any changes made automatically. Select deploy branch and the app will be available for use.

The live link can be found here -

## Technologies Used

* HTML5
* CSS
* JavaScript
* Python

## Credits

* Code
    * The user authentication method used, is from the mini walkthrough project. This was reused, as it was suggested in the course material. All other code is written by the developer.

* Content
    * All content was written by the developer

* Imagery
    * No images have been used throughout the app, this was due to the feeling of it being uneccessary, as it may clutter the page.

* Icons
    * All icons were sourced from fontawesome. They have been used on the lives and time bars to give a visually appealing appearance.
    

