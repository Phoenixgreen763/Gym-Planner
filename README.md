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
    * ![Logged out navbar](/static/images/logged-out-navbar.png)
    * These allow the user to register an account if they do not have one, or if they are a pre-exisitng user, will allow them to login freely.
    * If a user is already logged in, then the navbar will display 4 seperate links instead.
    * These links include exercises, planner, calendar, and logout.
    * ![Logged in navbar](/static/images/logged-in-navbar.png)

* Landing page
    * The user is initially introduced to the landing page, this displays messages based on if a user is logged in, or if they are not.
    * When a user is not logged in this page will give a welcome message, and invite them to create an account to continue.
    * ![Logged out homepage](/static/images/logged-out-home.png)
    * When a user creates an acount and views this page it will give them a welcome message, and display their username.
    * If a user is logged in, this page will also give them a brief message describing the different uses of the app for ease of use.
    * ![Logged in homepage](/static/images/logged-in-home.png)

* Register page
    * This page allows new users to register an account.
    * This page includes a form to register an account, including the desired username and password of the user.
    * If a user attempts to enter a username that is already in use, a flash message appears to warn them off this, so they can choose a suitable username.
    * ![Username already exists](/static/images/username-flash.png)
    * If a user enters a unqiue username, there is a register button that will create their account and log them in to the site.
    * ![Register form](/static/images/register.png)
    * Underneath the form there is a link for the login page, this allows users with an account to quickly redirect to their desired page.
    * ![Login redirect](/static/images/login-redirect.png)

* Login page
    * This page allows exisiting users to login to their account.
    * Like the register page, login displays a form for users.
    * This form is identical in styling to the register form, except the form button logs the user in, using the pre-exisitng data they created prior.
    * ![Login form](/static/images/login.png)
    * If a user inputs a wrong name, or password a flash message is shown to indicate this. 
    * ![Wrong username/password flash](/static/images/login-error.png)
    * Similar to the register page, underneath the form is a link, this link instead redirects the user to the register page if they do not already have an account.
    * ![Register redirect](/static/images/register-redirect.png)
  
* Exercises page
    * This page allows users to add, edit, delete, search for and view exercises added by other users.
    * The search bar includes a search, and reset button. This allows users to search for exercises by muscle group, or exercise name. The reset button allows the user to refresh the list and show the full range of exercises.
    * ![Search bar](/static/images/search-bar.png)
    * This page has an add exercise button for users. This lets all users add an exercise to the list. 
    * Users can also see who the exercise was submitted by.
    * This includes exercise-category, exercise-name, and a description of the exercise
    * ![Exercise list](/static/images/Exercise-list.png)
    * If a user attempts to submit an exercise that is already in the list, they will be given a flash message to indicate that the exercise already exists within the current list.
    * If a user is viewing an exercise they submitted, they will have the option to delete the exercise from the list, or edit the exercise.
    * ![Edit exercise](/static/images/edit-exercise.png)
    * If the user wishes to edit their own exercise, they will be redirected to a form.
    * This will be preopulated with the exisitng information that the user previously submitted.
    * The user will have the option to cancel the edit, or submit the edit. If they choose to edit, it will update the information that is displayed on the exercise list.
    * ![Edit form](/static/images/edit-form.png)

* Planner page
    * This page allows the users to create a weekly plan for their training.
    * Only exercises submitted by the user will be displayed to themselves.
    * Users can add exercises in the same format as the exercise list, with the additional ability to select which day of the week the exercise needs to be added to.
    * ![Planner page](/static/images/planner.png)
    * Instead of the forms that the exercise list uses, the planner instead utilises a popup modal instead.
    * When a user submits the information in the modal form, it will be added to their planner, inside the specific day they selected.
    * ![Planner modal](/static/images/planner-modal.png)
    * The user also has the ability to delete exercises that they no longer want in their planner.
    * ![Delete exercise](/static/images/planner-exercise.png)
    * When a user deletes an exercise from the planner, a flash message is shown to  the user, to indicate this was successful.
    * ![Deleted exercise](/static/images/delete-planner.png)

* Calendar page
    * This page is used for displaying a calendar, containing events in the community for people to partake in.
    * There is a button like the other pages for adding events.
    * This button is only available for admin users of the site to use, and add events to the calendar.
    * This calendar spans the entirety of the page for easy readability.
    * The calendar also includes a "today" button at the top of the calendar.
    * This button allows users to easily jump back to the current date to view events.

* Footer
    * Each page also consists of a footer.
    * This is located at the bottom of each page.
    * It includes links to various social media platforms, and the copyright, which automatically updates each year.
    * The colour and styling is consistent with the rest of the page to keep a uniform look as explained above.
  
### Features to Implement

* Planner Edit form modal
    * An edit form modal could be implemented for the planner exercises.
    * This would allow ease of use for the user, to edit a task, instead of having to fully delete it.
    * This was attempted, but there were consistent bugs, when trying to preopulate the form exercise categories.

* User Profile 
    * Potential to add a profile section to the app.
    * This could be used to track specific goals that the user sets.
    * This could include current weight, and goal weight.
    * It could also include tracking of weekly training that has been completed.
    * It may be engaging for the user to add "levels", this would give the user the sense of accomplishment, and add more interactivity. 

* User forum
    * This could be implemented to allow all users to share, and discuss their journey.
    * This would bring users together more, and allow them to share information or experiences. Like the exercise list already implemented does.

## User Stories

* User - A
    * User A is a middle aged parent. They primarily use the site for utilizing their planner, and viewing community events.
    * This user finds it difficult to manage their routine due to a busy lifestyle, so the planner enabels them to organize a routine, and easily keep track of what they need to do.
    * They also use the calendar to see when there are suitable events to attend, as they enjoy the community aspect.

* User - B
    * User B is a teenager. This user primarily uses the exercise list, and the planner.
    * This user is likely inexperienced, therefore they use the exercise list to learn about specific training movements to suit their needs.
    * This user will also likely utilize the planner aswell, as it allows them to keep a routine, and maintain a consistent and easy journey in the gym.

* User - C
    * This user is an admin. They have access to all other features of the site as others, however they have the ability to add events to the community calendar.
    * This user primarily visits the site to view the calendar and organize events. However, they still have the ability to share exercises, find exercises created by others, or even make their own plan if they desire.
    * This user can add events so the community can view and participate.

## Testing

* The testing done on the project consisted of automated validator testing to discover any errors in the code, and lighthouse was used, this was done to optomise page loading or any potential issues. Also manual user testing to find potential bugs.

## Manual Testing

* The site was tested by multiple freinds and family
* Everyone found the design to be visually appealing and readable. All users found the site easy to navigate, and explained the ease of use was helpful.
* Multiple types of devices, such as laptops, desktops, phones and tablets were used to ensure the site maintained no issues, regardless of size or hardware.
* Manual testing from all users found no additional bugs, other than the bugs already known and accounted for below.
* All users had no issue creating an account, or logging in.
* Manual testing however, did show that when exercises on the list page were edited, a new exercise would be added instead and would not remove the old information. This has now been fixed, so the information stored in the database is changed, and a new form is not added instead.

## Validator Testing 

* CSS Validator 
    * [CSS results](http://jigsaw.w3.org/css-validator/validator$link)
    * ![CSS results image](/static/images/CSS.png)

* HTML Validator

* Light House Testing
    * Lighthouse was used to check for errors or optimisation issues
    * The lighthouse score was 83 overall.
    * Optimisations were made, such as deferring javscript scripts, until they were needed. This allows the page to run smoother, and have faster loading times.
    * ![Lighthouse Score](/static/images/lighthouse.png)

## All Known Bugs

* When adding exercises to the planner, the user has to hard reload the page at times to display this new info.
    * Methods were added in an attempt to reload the page instance, however at times this bug is still persistent.
    * This should however now be working as intended, but has been a persistent issue.

* When loading the calendar page, there are times when the events dont load correctly. This results in the user occassionaly needing to refresh the page, in order to view the events.

* On some smaller screen sizes, the calendar can sometimes display the event name too small for the user to see.

* There is a bug on some mobile browers, that allows you to add exisitng exercises to the exercise list. This should not be possible, but may be due to a server-side issue when submitting the form.

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

The live link can be found here - https://gym-planner-e895d22abc86.herokuapp.com/

## Technologies Used

* HTML5
* CSS
* JavaScript
* Python

## Credits

* Code
    * The user authentication method used, is from the mini walkthrough flask project. This was reused, as it was suggested in the course material. All other code is written by the developer.

* Content
    * All content was written by the developer

* Imagery
    * No images have been used throughout the app, this was due to the feeling of it being uneccessary, as it may clutter the page.

* Icons
    * All icons were sourced from fontawesome. They have been used on the lives and time bars to give a visually appealing appearance.
    

