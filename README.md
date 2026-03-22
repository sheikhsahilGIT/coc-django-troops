# Clash of Clans Troops Display

My first full Django web app project!

## What it does
- Shows Clash of Clans troops as beautiful Bootstrap cards
- Live search by troop name
- Click any card → modal with extra details

## Tech stack
- Python 3.12+
- Django 5.x / 6.x
- Bootstrap 5 (CDN)
- SQLite (default dev database)

## How to run locally
```bash
# 1. Clone repo (or you already have it)
git clone https://github.com/YOUR_USERNAME/coc-django-troops.git
cd coc-django-troops

# 2. Create & activate virtual env
python -m venv .venv
.\.venv\Scripts\Activate   # Windows

# 3. Install dependencies
pip install django

# 4. Apply migrations
python manage.py migrate

# 5. Run server
python manage.py runserver