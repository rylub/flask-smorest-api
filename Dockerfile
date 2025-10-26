FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Copy requirements first for layer caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the rest of the project
COPY . .

# Expose Flask port
EXPOSE 5000

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV FLASK_ENV=production

# Use gunicorn to run your Flask factory app
CMD ["gunicorn", "app.app:create_app()", "--bind", "0.0.0.0:80"]
