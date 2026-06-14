# Use a lightweight Python base image
FROM python:3.9-slim-buster

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the trained model
# Assuming the model was saved as 'best_random_forest_model.joblib' in the root of the project
COPY best_random_forest_model.joblib .

# Copy the application code
COPY app.py .

# Expose the port your Flask app will run on
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
