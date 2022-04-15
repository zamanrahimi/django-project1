1. check python version 
python --version 

2. How to check pip --version
pip --version

3. how to check django --version (general not specific to any virtual env)
django-admin --verision 

4. How to install virtual envirement 
pip3 install virtualenv

5. make virtual envirement - windows 
py -m venv django-project-env

6. install django in the created enviroment 
pip install django

7. create a project folder alongside django-project-env
mkdir django-project

8. create a project 
django-admin startproject django-app

9. run django server 
python manage.py runserver