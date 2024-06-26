# <img src ="https://github.com/isaacmain254/Workpay/blob/main/static/images/Workpay-removebg-preview.png" width="120" height="100" alt="workpay logo"> workPay
----------------------------------------------------------------------


workpay is a freelance job portal

To run the project locally: clone this repository on your computer

```
    cd  #to your preferred directory
    git clone https://github.com/isaacmain254/Workpay.git
    cd Workpay
```

create a virtual environment and install all packages from **requirements.txt**.

 Make sure you are in the `$ ...Workpay ` directory


```python
    #create a virtual environment
    python -m venv venv

    #Activate the virtual environment, for Linux users
    # For Windows users search on how to activate a virtual environment
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

Every user should be associated with a profile, Bio, Skills, and project when registering on the website but since this was created using the superuser command you have to do it manually on the admin interface

Now you can log into the website `http://workpay.com:8000/` in order to use Google authentication

> :bulb: **Tip:** If you use `http://localhost:8000/` or `http://127.0.0.1:8000/` you can't authenticate using Google because Google OAuth is configured to redirect to `http://workpay.com:8000/` after login

Now you can register other users using the register page
