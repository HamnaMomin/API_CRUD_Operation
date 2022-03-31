# API_CRUD_Operation
This project is all about CRUD Api of Student data, for security purpose JWT authentication is also added.

**Steps for set up -**
1-Create Virtual environment in any directory -Here I have created ApiEnv
python -m venv ApiEnv

2-Activate virtual environment you have created using beloww command
ApiEnv/Scripts/activate

3-Install the packages according to the configuration file requirements.txt using beloww command
pip install -r requirements.txt

4- Go to CRUD_API project directory and create superuser to see data in admin panel
python manage.py createsuperuser username

5-start your server 
python manage.py runserver

6-Go to urls specified in urls.py file to check CRUD functionality.

Optional-home page is added to show all student data

Optional Step-Uncomment below 2 line in views.py firl for applying JWT authentication-

authentication_classes = [JWTAuthentication]
permission_classes = [IsAuthenticated]

