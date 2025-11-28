# This is the backend of a URL Shortner Appliation in Django.

There are 3 folders, 
1. URLShortener  This is the main codebase consisting of the main url mappings and settings.py.
2. users - This is the appliation handling the authentication mechanism.
3. shortener - This is the application where the url shortened are created and stored.


To install it

1. Clone the entire respository.
2. Create a python virtual environment
3. Install dependencies
4. Make Migrations
```
python manage.py makemigrations
python manage.py migrate
```
5. Run the server  ``` python manage.py runserver    ```
