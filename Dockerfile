FROM python:3.11-slim

# Set up the application directory
WORKDIR /app
COPY . /app

# Create a virtual environment and install dependencies
RUN python -m venv /venv
RUN /venv/bin/pip install -r requirements.txt

# Ensure the virtual environment is used by default
ENV PATH="/venv/bin:$PATH"

# Specify the command to run your application
CMD ["python", "app.py"]
