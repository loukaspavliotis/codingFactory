# User Management System

The **User Management System** is a web application designed to handle user-related 
functionalities, including registration, login, user statistics, 
and project management. Built with the Django framework, 
it leverages Django's built-in authentication system to provide a 
secure and efficient platform for managing user accounts.

## Features
The system offers the following functionalities:
1. **User Registration**  
   - Ensures passwords and emails adhere to secure formats.  

2. **User Login**  
   - Displays appropriate messages for failed logins due to incorrect credentials or deactivated accounts.  

3. **Home Page**  
   - Presents user statistics, including:  
     - Total number of registered users.  
     - Total number of active users.  
     - Latest registered user timestamps.  

4. **Manage Users Page**  
   - Allows administrators to:  
     - Delete users.  
     - Edit usernames and email addresses.  
     - Activate or deactivate user accounts.  
5. **Get User statistics from api call**  

## Technologies Used
- **Django**: A high-level Python web framework for rapid development and clean design.  
- **SQLite**: A lightweight, disk-based database used during development.  
- **HTML5 & CSS3**: Standard technologies for structuring and styling web pages.  
- **Bootstrap**: A popular front-end framework for building responsive, mobile-first websites.  
- **JavaScript**: Enhances interactivity and client-side functionality.  
- **Git**: A version control system for tracking changes and enabling collaboration.

## Architectures 
- **DTOS**
- **DAOS**
- **RESTAPI**
- **Server-Side Rendering**
- **MTV (Model-Template-View)**

## Pages
- **Login**: [http://127.0.0.1:8000/login/](http://127.0.0.1:8000/login/)  
- **Home**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)  
- **Manage Users**: [http://127.0.0.1:8000/manage-users/](http://127.0.0.1:8000/manage-users/)  
- **Edit User**: [http://127.0.0.1:8000/edit-user/userId/](http://127.0.0.1:8000/edit-user/userId/)  
- **Swagger**: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)  
- **Api Stats**: [http://127.0.0.1:8000/api/platform-stats/](http://127.0.0.1:8000/api/platform-stats/)  


## How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/loukaspavliotis/codingFactory.git
cd codingFactory
```

### 1. Clone the Repository
```bash
git clone https://github.com/loukaspavliotis/codingFactory.git
cd codingFactory
```

### 2.Create New Env 
```bash
python -m venv myenv
Activate new Env:
.\myenv\Scripts\activate 
```

### 3. INSTALL DEPENDENCIES
```bash
pip install -r requirements.txt
```

### 4. Apply migrations
```bash
python manage.py makemigrations
python manage.py migrate
```


### 5. RUN
```bash
python manage.py runserver
```

### 6.
A . Browse the app  in  http://127.0.0.1:8000/login

B. if already registered the testApi file with your credentials to get user statistics
