# Python - APIs - Create REST APIs I

## Creating REST APIs and protecting them

1st exercise with Django REST

After an introduction to Django REST Framework and basic authentication, it is now time for you to get acquainted with DRF.

## Exercise Instructions

- For this exercise, we will be using the Django/DRF project created for the class demo presented in the Create Rest APIs lecture. The only difference is that this project uses the out-of-the-box SQLit3 database, rather than a PostgreSQL database. 

- You can find this project in the ```dciproject``` folder. 
Here is the folder tree structure:
```
python-apis-create-I
├─ 
├─ README.md
└─ dciproject
   ├─ env
   ├  ├─ lib/
   │  ├─ bin/
   │  └─ pyvenv.cfg
   └─ my_project
      ├─ customer
      │  ├─ __init__.py
      │  ├─ admin.py
      │  ├─ apps.py
      │  ├─ migrations
      │  │  └─ __init__.py
      │  ├─ models.py
      │  ├─ tests.py
      │  └─ views.py
      ├─ manage.py
      └─ my_project
         ├─ __init__.py
         ├─ __pycache__/
         ├─ asgi.py
         ├─ settings.py
         ├─ urls.py
         └─ wsgi.py

```


- In order to start the ```my_project``` app, run the following in your terminal:

````
$ cd dciproject & cd my_project
````
Activate the virtual environment 
````
$ source env/bin/activate
````
Run the Django server
````
(env)$ python3 manage.py runserver
````


- Please follow the steps below.

### 0. Create a new Django REST app (following the lecture slides) called Product and add it to the `INSTALLED_APPs` list in ```my_project/settings.py``` 

### 1. Create a new model named **Product**, which should have the following data fields:

- product_name (String)
- product_id (ID)
- product_category
- product_description (String)
- product_image_url (String)
- product_price (Integer)

### 2. Create a ```product/serializers.py``` file and add the ModelSerializer for the Product model in ```customer/serializers.py```

### 3. Add the views to customer/ GET and POST:

- GET all products
- GET products by name
- POST new products
- DELETE products 

**NOTE: Use Generic Views**

### 4. Create a ```Product/urls.py``` file and add the ```urlpatterns```

### 5. Add the path ```product/``` to the ```my_project/urls.py``` file

### 6. Add token based authentication to the Products APIs 

### 7. Test your APIs in Postman