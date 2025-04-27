**README.md**

# AIwave - AI SaaS Website

> Full-stack Django web application based on the AIwave UI Kit.  
> **Deployed with Nginx, Gunicorn, Supervisor, and SSL (Let's Encrypt pending).**

---

## Features
- Django 5.2 backend
- HTML5 + CSS3 Frontend (AIwave theme)
- User-friendly modern design
- Fully Responsive
- Static files handled with Django's `collectstatic`
- Ready for production deployment with Gunicorn and Nginx
- Git Version Control Setup
- SSL Certificate Setup (Next Step)

---

## Project Structure
```
├── AIwave/           # Django project (settings, urls, wsgi)
├── static/           # Static assets (css, js, images)
├── templates/        # HTML templates
├── media/            # Media files (optional)
├── manage.py
├── venv/             # Python virtual environment
├── db.sqlite3        # Database (default)
└── README.md
```

---

## Setup Instructions

1. Clone the repository
   ```bash
   git clone YOUR_REPO_URL
   cd public_html/
   ```

2. Create a virtual environment
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Collect static files
   ```bash
   python manage.py collectstatic
   ```

5. Start the development server (for local testing)
   ```bash
   python manage.py runserver
   ```

6. Production ready with Gunicorn and Nginx.

---

## Environment Variables

- `.env` file recommended
- Variables:
  - `DJANGO_SECRET_KEY`
  - `DEBUG`
  - `ALLOWED_HOSTS`

---

## Deployment

- **Gunicorn** serves the Django app
- **Nginx** proxies requests and serves static files
- **Supervisor** ensures the app runs 24/7
- **Let's Encrypt SSL** *(to be configured)*

---

## Next Steps

- Setup SSL (Let's Encrypt) 🔒
- Create production settings
- Configure automatic deployment (optional)

---

## License
This project uses purchased AIwave UI Kit assets — commercial use is based on your license.
