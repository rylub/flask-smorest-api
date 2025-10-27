# Contributing

## Running the Project Locally with Docker

To run the Flask-Smorest API locally using Docker, use the following command:

```bash
docker run -dp 5000:80 -w /app -v "%cd%:/app" flask-smorest-api
