# The Impossible
**Too many good ideas are left in the dust. Sometimes, a world changing idea never sees daylight because we are too reluctant to share it with others, afraid that people will reject it, laugh at us, or claim as their own. All ideas deservers a chance to be developed. If you have a great idea but are not taking any actions, then share it and let it discovered by entrepenures makers and innovators. The Impossible is a social media that allows you to share your ideas and thoughts with the world. A place for inspiration, discussion and feedbacks.**

# Site Preview
## (Added darkmode to the entire site)

![Dashboard Light](preview_imgs/dashboard_light.png)
![Dashboard Dark](preview_imgs/dashboard_dark.png)
![Explore Section Light](preview_imgs/explore_light.png)
![Explore Section Dark](preview_imgs/explore_dark.png)
![Detail Section](preview_imgs/detail.png)
![Idea Editor](preview_imgs/edit_idea.png)
![Edit Profile](preview_imgs/edit_profile.png)

##
__Development progress:__ 7/10 complete

__Current *site* version:__ *v0.1*

__Current library versions:__
  * [Python](https://www.python.org/) 3.6.4
  * [Django](https://www.djangoproject.com/) 2.2.7
  * Pytz 2019.3
  * Sqlparse 0.3.1
  * [Bootstrap](https://getbootstrap.com/) 4

__Icons used are from [Feather](https://feathericons.com/)__

# Start a local server for testing:
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
""" 
Create a file under the_impossible folder called secret_key.txt
Then add ur own secret key, (Generate one from https://djecrety.ir/)

Now, because thsi site sends email to users, you need to configure your own email address in settings.py and create a file under the_impossible folder called email_password.txt which contains your email password

"""
# Create a folder under src staticfiles, then run
python manage.py collectstatic
# Create database and create superuser
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
# Runserver
python manage.py runserver
# Start another terminal session to run periodic tasks
python manage.py process_tasks
```