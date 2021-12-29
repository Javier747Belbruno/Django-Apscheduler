# Running on Local server

start python manage.py runserver 0.0.0.0:8000 & python manage.py runapscheduler & 


# Bash File running on Remote Server

python -m pip install django
python -m pip install apscheduler

python manage.py makemigrations
python manage.py migrate

#python initDB.py
python manage.py runapscheduler & start python manage.py runserver 0.0.0.0:3000 & 


start python manage.py runapscheduler & start python manage.py runserver 0.0.0.0:3000 &