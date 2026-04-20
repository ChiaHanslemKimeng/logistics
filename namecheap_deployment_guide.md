# Namecheap Shared Hosting Deployment Guide
## Fleet Direct Delivery — Django 6.0.4

> **Never deploy directly to `public_html`**. This guide uses an **Addon Domain** with its own document root, keeping `public_html` free for other sites.

---

## Overview

| Item | Value |
|---|---|
| Domain | `fleetdirectdelivery.com` |
| App Root | `~/fleetdirect/` |
| Document Root (cPanel) | `~/fleetdirect/public/` |
| Python | 3.12+ |
| Server | Passenger (WSGI) |

---

## Step 1 — Add the Domain in cPanel

1. Log in to **cPanel → Addon Domains**
2. **Domain:** `fleetdirectdelivery.com`
3. **Document Root:** Set to `fleetdirect/public` *(not `public_html/fleetdirect`)*
4. Click **Add Domain**

This creates:
- `~/fleetdirect/` — your app lives here
- `~/fleetdirect/public/` — Passenger's document root

---

## Step 2 — Enable Python App in cPanel

1. **cPanel → Setup Python App → Create Application**
2. Set:
   - **Python version:** `3.12`
   - **Application root:** `fleetdirect`
   - **Application URL:** `fleetdirectdelivery.com`
   - **Application startup file:** `passenger_wsgi.py`
   - **Application Entry point:** `application`
3. Click **Create**

cPanel will auto-generate a virtual environment at `~/virtualenv/fleetdirect/3.12/`

---

## Step 3 — Upload Your Project Files

Upload via **cPanel File Manager** or **FTP/SFTP** to `~/fleetdirect/`:

```
~/fleetdirect/
├── core/
├── users/
├── shipments/
├── notifications/
├── logistics_system/
├── templates/
├── static/
├── media/
├── manage.py
├── requirements.txt
├── .env                  ← Create manually on server (Step 5)
└── passenger_wsgi.py     ← Create manually (Step 4)
```

> ⚠️ **Never upload `.env` via Git.** Create it manually on the server.

---

## Step 4 — Create `passenger_wsgi.py`

Create `~/fleetdirect/passenger_wsgi.py`:

```python
import sys
import os

# Path to the virtual environment
VENV_PATH = '/home/YOUR_CPANEL_USERNAME/virtualenv/fleetdirect/3.12/lib/python3.12/site-packages'
sys.path.insert(0, VENV_PATH)

# Path to your project root
PROJECT_PATH = '/home/YOUR_CPANEL_USERNAME/fleetdirect'
sys.path.insert(0, PROJECT_PATH)

os.environ['DJANGO_SETTINGS_MODULE'] = 'logistics_system.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

> Replace `YOUR_CPANEL_USERNAME` with your actual cPanel username (visible in cPanel top-right corner).

---

## Step 5 — Configure Production Settings

### 5a. Update `settings.py`

```python
DEBUG = False

ALLOWED_HOSTS = ['fleetdirectdelivery.com', 'www.fleetdirectdelivery.com']

SECRET_KEY = os.environ.get('SECRET_KEY')

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

### 5b. Create `.env` on the Server

Via **cPanel File Manager**, create `~/fleetdirect/.env`:

```env
SECRET_KEY=your-very-secret-production-key-here
EMAIL_USER=your@gmail.com
EMAIL_PASS=your-gmail-app-password
ADMIN_EMAIL=your@gmail.com
```

> Generate a secret key:
> ```bash
> python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
> ```

---

## Step 6 — Install Dependencies

Via **cPanel → Setup Python App → Enter virtual environment**, or SSH:

```bash
source ~/virtualenv/fleetdirect/3.12/bin/activate
cd ~/fleetdirect
pip install -r requirements.txt
```

---

## Step 7 — Collect Static Files & Migrate

```bash
python manage.py collectstatic --noinput
python manage.py migrate
python manage.py createsuperuser
```

---

## Step 8 — Serve Static & Media Files via `.htaccess`

Create `~/fleetdirect/public/.htaccess`:

```apache
Alias /static/ /home/YOUR_CPANEL_USERNAME/fleetdirect/staticfiles/
Alias /media/ /home/YOUR_CPANEL_USERNAME/fleetdirect/media/

<Directory /home/YOUR_CPANEL_USERNAME/fleetdirect/staticfiles>
    Require all granted
</Directory>

<Directory /home/YOUR_CPANEL_USERNAME/fleetdirect/media>
    Require all granted
</Directory>

# Force HTTPS
RewriteEngine On
RewriteCond %{HTTPS} off
RewriteRule ^ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
```

---

## Step 9 — Install SSL Certificate

Go to **cPanel → SSL/TLS → AutoSSL** and apply a free Let's Encrypt SSL to `fleetdirectdelivery.com`.

---

## Step 10 — Restart & Test

1. **cPanel → Setup Python App → Restart** your application
2. Visit `https://fleetdirectdelivery.com` — site should load
3. Visit `https://fleetdirectdelivery.com/admin` — log in with superuser

---

## Troubleshooting

| Problem | Fix |
|---|---|
| **500 Error** | Check cPanel Error Logs. Usually wrong path in `passenger_wsgi.py` or missing package |
| **Static files not loading** | Run `collectstatic` and verify `.htaccess` Alias paths |
| **Media files not showing** | Check `MEDIA_ROOT` and `.htaccess` Alias for `/media/` |
| **Import errors** | Confirm `VENV_PATH` matches exact Python version in `~/virtualenv/fleetdirect/` |
| **Database errors** | Run `python manage.py migrate` again |

---

## Hosting Multiple Sites (Keeping Things Clean)

Each new site gets its own addon domain and folder — `public_html` stays untouched:

| Site | Addon Domain | App Root | Document Root |
|---|---|---|---|
| **This site** | `fleetdirectdelivery.com` | `~/fleetdirect/` | `~/fleetdirect/public/` |
| Site 2 | `yoursite2.com` | `~/site2/` | `~/site2/public/` |
| Site 3 | `yoursite3.com` | `~/site3/` | `~/site3/public/` |
