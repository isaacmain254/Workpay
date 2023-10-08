# ![workpay logo](static/images/Workpay-removebg-preview.png){width=80 height=30} workPay
----------------------------------------------------------------------


workpay is a freelance job portal

To run the project locally: clone this repository on your computer

```
    cd  #to your preferred directory
    git clone https://github.com/isaacmain254/Workpay.git
    cd Workpay
```

create a virtual environment and install all packages from **requirements.txt**.

 Make sure your are in `$ ...Workpay ` directory


```python
    #create virtual enviroment
    python -m venv venv

    #Activate the virtual environment, for linux users
    #for windows users search on how to activate virtual enviroment
    source venv/bin/activate

    pip install -r requirements.txt
```


Next makemigrations

```python
    #makemigrations
    python manage.py makemigrations

    #migrate
    python manage.py migrate

    #create a super user
    python manage.py createsuperuser
    
    #start the development server
    python manage.py runserver
```

Open the project in your browser `localhost:8000/admin/` and login with your superuser credential

Create 2 groups on the admin dashboard **client** and **freelancer** and assign the super user one group or both 

Every user should be associate with a profile, Bio, Skills and project when registering on the website but since this was created using superuser command you have do it manually on the admin interface

Now you can login into the website `http://workpay.com:8000/`

Now you can register other users using the register page
