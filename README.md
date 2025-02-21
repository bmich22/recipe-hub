# recipe-hub
The recipe hub is a recipe sharing website. Visitors can peruse recipes and if they'd like to join the community they can register and begin sharing recipes immediately. As a member they can also comment on recipes.  The site offers an easy recipe form to fill in and after approval, the recipes appear organized by most recent day in a visually pleasing manner with an image, a short description, an easy to read list of ingredients and instructions.   

[Here is the live version of the recipe hub project.](https://.herokuapp.com/)

### Screenshots of Home Page
| Large and Medium Screen | Small Screen 
| ----------- | ----------- 
| ![large screen](static/images/readme-images/large-screen.png)![med-screen](static/images/readme-images/med-screen.png)| ![small-screen](static/images/readme-images/small-screen.png) 

### UX / Wireframes / User Stories / Database Models / Colors
The initial building blocks of the project were the wireframes and user stories. The wireframes served as a visual blueprint for the layout and structure of the site and the user stories provided insight into what functions were needed. Planning the databases helped visualize how the data is linked and how we could query the databases to pull information.  

WIREFRAMES

| Home | Login | Member | CRUD | Recipe Detail
| ---- | ----- | ----- | ---- | ------------- 
| ![home](static/images/readme-images/wf-home.png) | ![login](static/images/readme-images/wf-login.png) | ![member](static/images/readme-images/wf-member.png) | ![add](static/images/readme-images/wf-add-recipe.png) | ![recipe-detail](static/images/readme-images/wf-recipe-detail.png)

USER STORIES

| As a... | I can... | So that.. | Features
|----------|----------|--------- | --------
| Site User  | view list of recipes   | I can select which recipe I want to view | Create recipe database, create recipe list view
| Site User  | view a recipe | I can see the rexipe details and any comments | Create a function so user can go from  list to specific recipe, create recipe detail view
| Site User  | search for recipes by ingredient   | I can find what recipes that interest me | Create search bar, implement search functionality, use recipe list view with search criteria
| Site User  | register an account   | I can submit recipes and comment on my own and other recipes | Create registration form and link from home page
| Site User  | create and submit recipes  | I can share recipes with the community | Create form for adding recipe, implement upload and save function
 Site User  | modify or delete my recipe   | I can correct mistakes or come back to it later | Add edit and delete recipe function
 | Site User  | see the About section   | I can read about the site and who is running it | Create about section
 | Site Admin  | approve and/or disapprove recipes  | I can keep content on the site current | Create admin panel and give access to site admin
 | Site Admin  |  approve and/or disapprove comments  | I can keep content on the site current and filter out objectional comments | Create comments section in admin panel with approve/disapprove/delete comment function
 | Site Admin  | create or update the about page content  | information about the site owner is available to the users | Create add, edit, delete function on about page
 

 DATABASE MODELS

 | Home | Login 
 | ---- | ----- 
 ![models-1](static/images/readme-images/models-1.png) | ![models-2](static/images/readme-images/models-2.png)

 COLORS

 ![colors](static/images/readme-images/colors.png) 

### Features
| Feature | Screenshot 
| ------- | ----------
| The site is responsive and displays nicely on all screen sizes.  Bootstrap was used to format the content, utilizing its columns and grids, as well as utility styling on text, padding and margins. |  ![med-screen](static/images/readme-images/med-screen.png)
| Home page displays a visually pleasing view of four recipes at a time with ‘next’ and ‘back’ arrows to navigate through the list. | ![prev-next](static/images/readme-images/prev-next.png)
| Search field enables visitors to search recipes by ingredient. | ![search](static/images/readme-images/search.png)
| Visitors can become members by filling an easy registration sign up form, supplying username, email address and password.| ![reg](static/images/readme-images/reg.png)
| Once logged in, members can add recipes to the site by clicking the “create a recipe” button and filling in a form. Members can save a draft of their recipe and come back to finish it later or click “publish” and the recipe will be ready for approval by the admin. | ![add](static/images/readme-images/add.png)
| Members can click on the 'manage recipes' button and a list of their recipes will appear.  On this screen they can easily see if a recipe has not yet been approved by a red message that appears at the bottom of the recipe card. | ![my-recipes](static/images/readme-images/my-recipes.png)
| Members can make comments on any recipe and they can edit and delete those comments later. | ![comment](static/images/readme-images/comment.png) ![comment-msg](static/images/readme-images/comment-msg.png) 
| The superuser has access to the admin panel directly from the member screen.  Their welcome message will display three buttons – create recipe, manage recipes and admin panel, rather than the normal two – create recipe, manage recipes, for regular members. | ![su-welcome](static/images/readme-images/su-welcome.png)
| The superuser can add recipes either through the form on the website or via the admin panel. | ![su-recipe](static/images/readme-images/su-recipe.png)
| The superuser can approve recipes through the admin panel, one at a time so that the superuser can be certain that all elements are in place and formatting and syntax is good. | ![rec-approve](static/images/readme-images/rec-approve.png)
| Comments can be approved and deleted in bulk, directly from the Comments Panel.  This makes approving comments very quick and easy. | ![bulk-comments](static/images/readme-images/bulk-comments.jpg)
| There is an About section that displays information about the site and the site owner. The information is in a database so that in the future there could be a group of contributor showcased on these pages. | ![about](static/images/readme-images/about.png)
| The superuser manages the About content through the Admin panel.  The text editor has rich text formatting capability. | ![su-about](static/images/readme-images/su-about.png) 

### Future Features
Recipe Box
Members should be able to choose favorites and save them in a “recipe box” so they can access the recipes easily at a later time.

Message to the Site Administrator. 
Visitors and/or members should be able to send the Site Administrator a message through the site.

Ratings
Members should be able to rate recipes and these ratings would be shared on the recipe details page.

Add Nutrition Information

















