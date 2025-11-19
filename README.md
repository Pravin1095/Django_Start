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

For letting django know what urls to accept we need to create urls.py file where we need to have an array of urls in which we need to display the urls. Syntax : urlpatterns = [path("january", views.index)]. 2nd argument is mentioning the function that needs to be called when this url is hit.

Now, challenges is the first url endpoint which we need to put in monthly_challenges url file and there in 2nd argument import include and then mention the file path in it where we have challenges url which is challenges.urls.

Overall flow is as follows:

Client (Sends request to Server) -> Server (Django) -> checks for UrlConfig files -> This further checks for the Views files.

Dynamic url endpoints:

Let's say it is redundant to have all 12 months url individually in our urls file. Instead we can pass a placeholder as first argument to path (syntax : path("<month>")). Here the month is the url endpoint that user is entering after challenges in the browser. So now in views file we need to get this month as argument in our logic function Eg : def monthly_challenge(request, month): Now this month is passed from the urls file to our views file and we can write our logic based on this.

reverse:

This function in the views.py , we use it for setting the url endpoints as dynamic instead of hardcoding (We hardcoded as /challenges in HttpRedirectResponse). In reverse the first argument we get from urls.py file where we send as 3rd argument and that contains the endpoint /challenges in it. For the other endpoint like jan or feb we need to pass 2nd argument to reverse with the endpoint name in an array (args=[redirect_month])