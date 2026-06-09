# INSTALLATION & SETUP GUIDE - UFASH ACCESSORIES

## Quick Start

### Option 1: Automated Setup (Recommended)

#### On Linux/Mac:
```bash
cd "POS APP"
chmod +x setup.sh
./setup.sh
python manage.py createsuperuser
python manage.py runserver
```

#### On Windows:
```cmd
cd "POS APP"
setup.bat
python manage.py createsuperuser
python manage.py runserver
```

---

## Manual Installation

### Prerequisites
- **Python 3.8 or higher** - Download from https://www.python.org
- **pip** - Usually comes with Python
- **Git** (optional) - For version control
- **PostgreSQL** (optional) - For production databases

### Step 1: Navigate to Project Directory
```bash
cd "POS APP"
```

### Step 2: Create Virtual Environment

**On Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows (Command Prompt):**
```cmd
python -m venv venv
venv\Scripts\activate.bat
```

**On Windows (PowerShell):**
```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

### Step 3: Install Dependencies
```bash
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

### Step 4: Create Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Create Superuser (Admin Account)
```bash
python manage.py createsuperuser
```
When prompted:
- Username: `admin` (or your preferred username)
- Email: `admin@example.com` (or your email)
- Password: (enter a secure password)

### Step 6: Start Development Server
```bash
python manage.py runserver
```

### Step 7: Access the Application
- **Main Application:** http://localhost:8000
- **Admin panel:** http://localhost:8000/admin

---

## PostgreSQL Configuration (Production)

### Install PostgreSQL
- **Windows:** https://www.postgresql.org/download/windows/
- **Mac:** `brew install postgresql`
- **Linux:** `sudo apt-get install postgresql`

### Create Database
```sql
CREATE DATABASE pos_system;
CREATE USER postgres WITH PASSWORD 'your_password';
ALTER ROLE postgres SET client_encoding TO 'utf8';
ALTER ROLE postgres SET default_transaction_isolation TO 'read committed';
ALTER ROLE postgres SET default_transaction_deferrable TO on;
ALTER ROLE postgres SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE pos_system TO postgres;
```

### Update Django Settings
Edit `pos_system/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'pos_system',
        'USER': 'postgres',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Install PostgreSQL Adapter
```bash
pip install psycopg2-binary
```

### Run Migrations
```bash
python manage.py migrate
```

---

## Project Structure After Setup

```
POS APP/
├── venv/                       # Virtual environment (created)
├── pos_system/
│   ├── __init__.py
│   ├── settings.py            # Django settings
│   ├── urls.py                # URL routing
│   ├── asgi.py
│   └── wsgi.py
├── inventory/
│   ├── migrations/            # Database migrations
│   ├── __init__.py
│   ├── admin.py               # Admin configuration
│   ├── apps.py
│   ├── forms.py               # Django forms
│   ├── models.py              # Database models
│   ├── tests.py
│   ├── urls.py                # App URLs
│   └── views.py               # Business logic
├── templates/
│   ├── base.html              # Base template
│   └── inventory/             # App templates
│       ├── dashboard.html
│       ├── catalog.html
│       ├── add_product.html
│       ├── edit_product.html
│       ├── cart.html
│       ├── receipt.html
│       ├── sales_report.html
│       ├── restock_alerts.html
│       ├── categories.html
│       └── add_category.html
├── static/
│   ├── css/
│   │   └── style.css          # Custom styles
│   └── js/                    # JavaScript files
├── media/                     # User uploads
├── logs/                      # Application logs
├── manage.py
├── db.sqlite3                 # SQLite database (development)
├── requirements.txt           # Python dependencies
├── .env.example              # Environment variables template
├── setup.sh                  # Linux/Mac setup script
├── setup.bat                 # Windows setup script
├── README.md                 # Documentation
└── INSTALLATION.md           # This file
```

---

## Troubleshooting

### Issue: "Python is not recognized"
**Solution:** 
- Add Python to PATH on Windows
- Or use full path: `C:\Python39\python.exe`

### Issue: "Virtual environment not activating"
**Solution:**
```bash
# Linux/Mac
source venv/bin/activate

# Windows CMD
venv\Scripts\activate.bat

# Windows PowerShell
venv\Scripts\Activate.ps1
```

### Issue: "ModuleNotFoundError: No module named 'django'"
**Solution:**
- Ensure virtual environment is activated
- Run: `pip install -r requirements.txt`

### Issue: "Database error" / "No such table"
**Solution:**
```bash
python manage.py makemigrations
python manage.py migrate
```

### Issue: "Port 8000 already in use"
**Solution:**
```bash
# Use different port
python manage.py runserver 8001

# Or kill the process using port 8000
# Linux/Mac: lsof -ti:8000 | xargs kill -9
# Windows: netstat -ano | findstr :8000
```

### Issue: "Static files not loading"
**Solution:**
```bash
python manage.py collectstatic --noinput
```

### Issue: "Permission denied" on setup.sh
**Solution:**
```bash
chmod +x setup.sh
./setup.sh
```

---

## Deactivating Virtual Environment
```bash
# When you're done, deactivate the virtual environment:
deactivate
```

---

## Production Deployment

### Collect Static Files
```bash
python manage.py collectstatic --noinput
```

### Use Production Server (Gunicorn)
```bash
pip install gunicorn
gunicorn pos_system.wsgi:application --bind 0.0.0.0:8000
```

### Update Settings for Production
Edit `pos_system/settings.py`:
```python
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

---

## Getting Help

- **Django Documentation:** https://docs.djangoproject.com
- **PostgreSQL Documentation:** https://www.postgresql.org/docs
- **Bootstrap Documentation:** https://getbootstrap.com/docs
- **Python Official Site:** https://www.python.org/doc

---

## Next Steps

1. **Create Admin Account:**
   ```bash
   python manage.py createsuperuser
   ```

2. **Login to Admin Panel:**
   - Go to http://localhost:8000/admin
   - Create categories
   - Add products

3. **Start Using the Application:**
   - Go to http://localhost:8000
   - Browse catalog
   - Make test purchases

4. **Check Reports:**
   - View sales reports
   - Monitor restock alerts

---

**Installation Complete! Happy selling!** 🎉
