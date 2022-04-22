# Notes Application
## Run the application
- Clone the repo
```bash
git clone git@github.com:kzborisov/notesApp.git
cd notesApp
```
- Build the virtual environment
```bash
python3 -m venv env
source env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```
- Build the front-end
```bash
cd frontend
npm install
npm run build
cd ..
```
- Make the migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
- Start the server
```bash
python manage.py runserver
```
- Start the server at http://127.0.0.1:8000/

