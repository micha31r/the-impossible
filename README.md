# The Impossible
A platform to:
	share ideas and turn them into reality
	find collaborators to work on a project

Preview 1
![Explore Section](preview_imgs/explore.png)
Preview 2
![Discover Section](preview_imgs/discover.png)

__Current *site* version:__ *v0.1*

__Current library versions:__
  * [Python](https://www.python.org/) 3.6.4
  * [Django](https://www.djangoproject.com/) 2.2.7
  * Pytz 2019.3
  * Sqlparse 0.3.1

## Start a local server for testing:
(secret key and database is excluded from repository)
```bash
# Clone this repository
git clone https://github.com/micha31r/The-Impossible.git
# Go into repository
cd The-Impossible
# Create a virtual environment
python3 -m venv .
# Install libraries
pip install -r requirements.txt
# Activate python virtual environment on Mac
source bin/activate && cd src
# (On Windows)
Scripts\activate
cd src
# Create a file under the_impossible folder called secret_key.txt
# Then add ur own secret key, (Generate one from https://djecrety.ir/)
...
# Create database and create superuser
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
# Runserver
python manage.py runserver
```
##
*MD Written with [StackEdit](https://stackedit.io/).*