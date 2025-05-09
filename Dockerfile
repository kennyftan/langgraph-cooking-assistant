# Use an official Python runtime as a parent image
FROM python:3.13

# Set the working directory in the container
WORKDIR /app

# Install any dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY src/ /app/src/
COPY main.py /app/

# Command to run the application
CMD ["python", "main.py"]