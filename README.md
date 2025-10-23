# Django Tasklist

A simple, straightforward Django app to manage todo tasks with a clean interface.

## Features

- Task management (create, edit, delete, mark as complete)
- Task prioritization
- User authentication
- Responsive design
- Secure HTTPS by default
- Modern security headers and settings

## Requirements

- Python 3.8+
- Django 4.2+
- PostgreSQL/MySQL/SQLite (SQLite is used by default for development)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/django-tasklist.git
   cd django-tasklist
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

5. Run migrations:
   ```bash
   python manage.py migrate
   ```

6. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Security

This application includes several security features out of the box:

- HTTPS enforcement
- Secure cookies (HTTPOnly, Secure flags)
- HSTS (HTTP Strict Transport Security)
- XSS protection
- Clickjacking protection
- MIME-type sniffing protection
- CSRF protection

## Production Deployment

For production deployment, make sure to:

1. Set `DEBUG = False` in `settings.py`
2. Set a strong `SECRET_KEY` in your environment variables
3. Use a production-ready database like PostgreSQL
4. Set up a proper web server (Nginx/Apache) with a valid SSL certificate
5. Configure your web server to handle static files
6. Set up proper logging

## Screenshot

[![Screenshot](https://raw.githubusercontent.com/ragsagar/django-tasklist/master/screenshots/tasklist_screenshot.png)](https://raw.githubusercontent.com/ragsagar/django-tasklist/master/screenshots/tasklist_screenshot.png)

## License

MIT

