# Use Python base image
FROM python:3.11

# Set working directory in the container
WORKDIR /app

# Copy the project files into the container
COPY . .

# Install project dependencies
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "./src/script.py", "--INPUT", "./papers", "--OUTPUT", "./output"]
