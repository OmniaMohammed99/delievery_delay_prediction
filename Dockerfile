FROM python:3.11-slim

# Prevent Python from creating .pyc files
# and make logs appear immediately
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create application directory
WORKDIR /app

# Copy runtime requirements
COPY requirements/requirements.txt requirements-dev.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements-dev.txt

# Copy project files
COPY app/ app/
COPY config/ config/
COPY models/ models/
COPY src/ src/
COPY run.py run.py

# Flask port
EXPOSE 5000

# Start Flask application
CMD ["python", "run.py"]