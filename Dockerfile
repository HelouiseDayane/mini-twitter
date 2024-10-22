FROM python:3.9

# Set the working directory
WORKDIR /usr/src/app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

# Expose the port the app runs on
EXPOSE 8080

# Start Gunicorn
CMD ["gunicorn", "mini_twitter.wsgi:application", "--bind", "0.0.0.0:8080"]
