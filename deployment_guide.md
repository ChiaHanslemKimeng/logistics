# Logistics System Deployment Guide

This guide outlines the steps to deploy your **Global Courier Tracking System** from your local machine to **GitHub** and finally to **PythonAnywhere**.

---

## Part 1: GitHub Repository (Version Control)

1. **Create Repository**: Log in to [GitHub](https://github.com) and create a new public or private repository named `Logistics`.
2. **Initialize Local Git**:
   ```powershell
   git init
   git add .
   git commit -m "Initial commit: Professional Logistics System"
   ```
3. **Ignore Secrets**: Ensure your `.env` file is NOT uploaded. Create a `.gitignore` file if it doesn't exist:
   ```text
   .env
   __pycache__/
   db.sqlite3
   media/
   staticfiles/
   ```
4. **Push to GitHub**:
   ```powershell
   git remote add origin https://github.com/YOUR_USERNAME/Logistics.git
   git branch -M main
   git push -u origin main
   ```

---

## Part 2: PythonAnywhere Deployment

### 1. Setup Environment
1. Log in to [PythonAnywhere](https://www.pythonanywhere.com/).
2. Open a **Bash Console** and clone your repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/Logistics.git
   cd Logistics
   ```
3. Create a **Virtual Environment**:
   ```bash
   mkvirtualenv --python=/usr/bin/python3.12 logistics-env
   pip install django python-dotenv pillow
   ```

### 2. Configure Web App
1. Go to the **Web** tab in PythonAnywhere dashboard.
2. Click **Add a new web app**.
3. Choose **Manual Configuration** (do not choose Django) and select **Python 3.12**.
4. Set **Source Code Directory**: `/home/YOUR_USERNAME/Logistics`
5. Set **Virtualenv Directory**: `/home/YOUR_USERNAME/.virtualenvs/logistics-env`
6. **Static Files Configuration**:
   - URL: `/static/` -> Path: `/home/YOUR_USERNAME/Logistics/staticfiles`
   - URL: `/media/` -> Path: `/home/YOUR_USERNAME/Logistics/media`

### 3. WSGI Configuration
Open the "WSGI configuration file" link on the Web tab and replace its content with:
```python
import os
import sys

path = '/home/YOUR_USERNAME/Logistics'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'logistics_system.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

### 4. Database & Environment
1. **Upload Database**: Use the **Files** tab to upload your local `db.sqlite3` to `/home/YOUR_USERNAME/Logistics/` if you want to keep your local data.
2. **Setup Secrets**: 
   - Create a `.env` file in `/home/YOUR_USERNAME/Logistics/` via the Files tab.
   - Add your `EMAIL_USER`, `EMAIL_PASS`, and a new `SECRET_KEY`.
3. **Collect Static**:
   In the Bash console (virtualenv active):
   ```bash
   python manage.py collectstatic
   ```

### 5. Final Step
Go to the **Web** tab and click **Reload**. Your site is now live at `YOUR_USERNAME.pythonanywhere.com`!
