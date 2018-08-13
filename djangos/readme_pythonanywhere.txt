1. Once you've created an account, go to https://www.pythonanywhere.com/user/nmmarcelnv/
2. open a bash console
3. upload your project (you can clone from github)
4. create a virtual environment
	mkvirtualenv --python=/usr/bin/python3.5 myenv 
	(myenv is the virtual environment name you want)
5. install packages on your virtual environmant
	pip install django
6. go to you pythonanywhere dashborad and click on Web
7. click on Add a new web page
	- select python version
	- select manual
8. Edit the file https://www.pythonanywhere.com/user/nmmarcelnv/files/var/www/nmmarcelnv_pythonanywhere_com_wsgi.py

# +++++++++++ DJANGO +++++++++++
# To use your own django app use code like this:
import os
import sys

## assuming your django settings file is at '/home/nmmarcelnv/mysite/mysite/settings.py'
## and your manage.py is is at '/home/nmmarcelnv/mysite/manage.py'
path = '/home/nmmarcelnv/portfolio/djangos/mysite'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

## then:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()



set the virtual environment (just enter myenv)
/home/nmmarcelnv/portfolio/djangos/mysite/static

mv to the home directory of project and execute
python manage.py collectstatic

9. Edit your project settings.py file to add the ALLOWED_HOST
ALLOWED_HOSTS = ['nmmarcelnv.pythonanywhere.com'] 
DEBUG=FALSE

10. Go to your dashborad, reload, then open the link
	 nmmarcelnv.pythonanywhere.com

11. to deal with static files
	- go to settings.py 
	- specify a path where your want the static files to reside
	e.g STATIC_ROOT = '/home/nmmarcelnv/portfolio/djangos/mysite/static'

	then do to the console, navigate to /home/nmmarcelnv/portfolio/djangos/mysite
	and execute python manage.py collectstatic

	The above command will collect all the static files available in your project
	and place them in the /home/nmmarcelnv/portfolio/djangos/mysite/static dicrectory

	Now on the pythonanywhere web home page, go to the static files section
	- Under URL enter       : /static/
	- Under Directory enter : /home/nmmarcelnv/portfolio/djangos/mysite/static
