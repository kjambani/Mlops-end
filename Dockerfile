FROM python:3.8-slim

# Setup the working directory inside the container
WORKDIR /app

# Update the system, install basic required tools (like awscli if deploying to AWS/EC2)
RUN apt-get update -y && \
    apt-get install -y awscli

# Copy the entire project codebase into the container
COPY . /app

# Upgrade pip and install the necessary Python packages
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Expose the Flask port you defined in app.py
EXPOSE 8080

# Spin up the Flask API
CMD ["python3", "app.py"]