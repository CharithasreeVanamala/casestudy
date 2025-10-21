# Use a small, supported Python base
FROM python:3.9-slim-buster

# Set a working directory
WORKDIR /app

# Copy requirements first (caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . /app

# Expose port used by Flask
EXPOSE 5000

# Use a non-root user (optional but good practice)
# create app user and set ownership
RUN useradd --create-home appuser && chown -R appuser /app
USER appuser

# Run the app
CMD ["python3", "app.py"]
