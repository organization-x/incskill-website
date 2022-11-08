# IncSkill Website
## Table of Contents
* [Introduction](#introduction)
* [Tech Stack](#tech-stack)
* [Project Status](#project-status)
* [Launch](#launch)

## Introduction
IncSkill is a website that was commissioned by the Washington State Department of the Blind. Its goal is to create an accessible portal for learning about Computer Science with a focus on accessibility for users with visual impariments. To solve this problem, we decided to make a website with the main focus on compatability with a screen reader. Screen readers take text on a webpage and read them aloud to users who are blind, or have difficulty reading text, and it allows them to navigate websites that would otherwise be inaccessible. However, many websites today lack proper accessibility with a screen reader, leaving it difficult for those with sight impairments to use the information they provide. This is a common issue with many learning sites, most of which rely on video to "show" a user how to accomplish a certain task. The problem with this is that video cannot easily be converted into something accessible by a screen reader. To fix this, the website uses solely text for its main content, and any images within the website have been assigned "alternate text" to be read out whenver a user with a screen reader passes over them. We hope that by creating informative content directed specifically at those with visual impairments, we can provide greater opportunity to those who otherwise would not have access to jobs or knowledge due to a lack of accessibility. 
You can learn more [here](https://aicamp.notion.site/IncSkill-Website-Product-Spec-f59270ae31b24c1daad56ec74b821b50).
## Tech Stack
For the backend, we chose to use Django, since it allows easy access to python code in the backend from the HTML code. Since most of our engineers had prior experience with python, we decided to use Django over other alternatives, like JavaScript. For the frontend and styling, we chose to use HTML and CSS, since these allowed us the most flexibility, and had easy compatability with Figma, which we used in the early stages of the project for design. Finally, for deployment, we used Railway, since its integration with GitHub made it easy for us to update the deployed server with new changes each time we made a change, rather than having a long and complex process, which would have meant that we would have had to condense changes into much larger updates, slowing the rollout of new changes. 
## Project Status
This website is currently fully functioning, serving as a template for similar courses in the future. The website has been styled with animations and color schemes, and users can signup, login, and view course material. Currently, we only have the original template course, but all resources within the template course are accessible, both in the sense of accessing them, but also are accessible to blind users through a screen reader. At the end of the course, there is a quiz in which users can test their knowledge of the content in the course, and can see how much they have learned from the course. Finally, any user can monitor their progress, in their profile page or on the dashboard, as they complete assignments. 
## Launch
The website is currently accessible [here](https://courses.incskill.com/dashboard/). However, for those working on a development server, you can start up a local server by doing the following:
### 1. Create a virtual environment
You can do this by entering the following command once you've chosen a suitable directory:

$python -m venv [name of virtual environment]
### 2. Start the virtual environment
Change your directory to the virtual envinronment you've just created using the 'cd' command

Then run the following command:

$Scripts\activate

This will activate the virtual environment, and you should see ([name of virtual environment]) before the directory now.
### 3. Install all the necessary files
To install all the python addons used for the file, simply run the command:

$pip install -r requirements.txt

This will likely take several minutes if there are a large number of installs to be completed.
### 4. Start the server
This is the only step that needs to be repeated to start the server once the previous steps have already been done. To start the local host type the following command. Before running make sure your current directory is incskill-website.

$python manage.py runserver

This will load within a few second, and provide you a link, to open the website, simply ctrl+click the link to open it in your browser.
