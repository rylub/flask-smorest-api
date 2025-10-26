FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Copy requirements first for layer caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the project
COPY . .

# Expose Flask port
EXPOSE 5000

# Set Flask environment variables
ENV FLASK_APP=app.app:create_app
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development
ENV PYTHONPATH=/app

# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0", "--debug"]
