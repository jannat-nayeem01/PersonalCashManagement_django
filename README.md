# personal-cash-management

Basic Setup to get this personal cash management app up and running.

## 1. Local Setup & Package Installs
First check python version, spin up the virtual env, and grab django.

```bash
python3 --version

python3 -m venv venv (for mac)
source venv/bin/activate  # venv\Scripts\activate on windows

pip install django
python -m django --version
```

## 2. Start Project and App
Creating the project root, the main app, and initializing git.

```bash
django-admin startproject cashproject .
django-admin startapp cashapp

git init
touch .gitignore
touch README.md
```

## 3. Initial Migrations & Superuser
Run the base migrations first, then set up the local admin account.

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
* **User:** admin
* **Email:** (leave blank)
* **Pass:** admin

## 4. Hooking Up Settings & URLs
Open up `cashproject/settings.py` and register `cashapp` in installed apps:

```python
INSTALLED_APPS = [
    ...
    'cashapp',
]
```

### Main URLs (`cashproject/urls.py`)
Import `include` and route the root path to our app.

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cashapp.urls')),
]
```

### App URLs (`cashapp/urls.py`)
Create this file manually in the app folder to handle the profile, transaction, and dashboard views.

```python
from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('transaction/', views.transaction, name='transaction'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
```

## 5. Models, Auth & Forms Workflow

### Auth Setup
1. Build the `CustomUser` model in `cashapp/models.py` for user login/registration.
2. Tell Django to use it by adding this to `settings.py`:
```python
   AUTH_USER_MODEL = 'cashapp.CustomUser'
```
3. Run migrations right away so it doesn't break the database:
```bash
   python manage.py makemigrations
   python manage.py migrate
```

### Core App Logic
* Make `forms.py` in `cashapp` to handle `AddCashForm` and `ExpenseForm`.
* Create a `templates/` folder inside `cashapp` for the HTML pages (`base.html`, `navbar.html`, `transaction.html`, `dashboard.html`, `profile.html`).
* Add models to `cashapp/models.py` (`CustomUser`, `AddCash`, `Expense`).
* Register them in `cashapp/admin.py`:
```python
  from django.contrib import admin
  from .models import CustomUser, AddCash, Expense

  admin.site.register(CustomUser)
  admin.site.register(AddCash)
  admin.site.register(Expense)
```
* Run the usual migration commands after adding them:
```bash
  python manage.py makemigrations
  python manage.py migrate
```

### Key Logic Notes
* `AddCash` and `Expense` both use `ForeignKey(CustomUser)` — every view filters by `request.user` so users only see their own entries.
* `transaction` view handles both forms on one page using `prefix='cash'` / `prefix='expense'` to avoid field-name collisions (both forms have an `amount` field), plus a hidden `form_type` input to know which form was submitted.
* Expense submission checks available balance (`total cash - total expenses`) before saving — blocks the entry with an error message if the amount exceeds what's available.
* `dashboard` view uses `aggregate(Sum('amount'))` for all-time totals, and `datetime__date=today` (via `timezone.localdate()`) to scope the recent-activity tables to today only.

## 6. Styling & Linters (Optional)
* Bootstrap 5.3.8 is loaded via CDN in `base.html` — no separate install needed.
* Grab `djlint` to format the HTML/Jinja templates nicely:
```bash
  pip install djlint
```

## 7. Run Server
Fire it up and check `http://127.0.0.1:8000`
```bash
python manage.py runserver
```

## Dependencies
Freeze installed packages any time you add a new one, and keep this file committed:
```bash
pip freeze > requirements.txt
```
To rebuild the environment elsewhere:
```bash
pip install -r requirements.txt
```

## Git
```bash
git config --list
git remote -v
git status
```