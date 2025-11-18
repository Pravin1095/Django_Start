# Django_Start

Pdf for Django :

https://github.com/academind/django-practical-guide-course-code/tree/setup-zz-extra-files


Django: 

A python web development framework.

Starting a development server:

To preview our dev server give the command python manage.py runserver

Creating new folder (Django Apps):

Use the command python manage.py startapp ${folderName} to create new App.
We can say App to be Module. Apps are building blocks for overall projects

URL config/routes:

URL-Action markings which ensure that certain results are achieved when user enters certain urls.
Views:
The logic (function or class) that is executed for different URLs (and HTTP methods). Views are responsible for processing the requests(parsing url) and creating a response. In views.py file we write the logic where that function is executed when the user enters a particular url. That function returns a http rsponse to the client. This function gets the request as the argument and we can also use this in our server for business logics.

For letting django know what urls to accept we need to create urls.py file where we need to have an array of urls in which we need to display the urls. Syntax : urlpatterns = [path("january", views.index)]. 2nd argument is mentioning the function that needs to be called when this url is hit