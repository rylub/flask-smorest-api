import os
import requests
from dotenv import load_dotenv
import jinja2

load_dotenv()

# ✅ Correct: Load the Mailgun domain directly (don't wrap it in os.getenv again later)
DOMAIN = os.getenv("MAILGUN_DOMAIN")

# ✅ Proper Jinja2 environment setup for Flask-style templates
template_loader = jinja2.FileSystemLoader("app/templates")
template_env = jinja2.Environment(loader=template_loader)


def render_template(template_filename, **context):
    """Render Jinja2 template with context."""
    return template_env.get_template(template_filename).render(**context)


def send_simple_message(to, subject, body, html):
    """Send an email via Mailgun with both plain text and HTML content."""
    return requests.post(
        f"https://api.mailgun.net/v3/{DOMAIN}/messages", # ❌ FIXED: Removed os.getenv() wrapper
        auth=("api", os.getenv("MAILGUN_API_KEY")),
        data={
            "from": f"Stores API <{os.getenv('MAILGUN_FROM_EMAIL')}>",
            "to": [to],
            "subject": subject,
            "text": body,
            "html": html
        }
    )


def send_user_registration_email(email, username):
    """Send welcome email when user registers."""
    return send_simple_message(
        email,
        "Successfully signed up",
        f"Hi {username}! You have successfully signed up to the Stores REST API.",
         render_template("email/action.html", username=username)
    )
