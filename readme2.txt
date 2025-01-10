GIT CLONE:
git clone https://github.com/loukaspavliotis/codingFactory.git
cd codingFactory


Create New Env: python -m venv myenv
ACTIVATE new env
 .\myenv\Scripts\activate    

pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
python manage.py runserver


DESCRIPTION: