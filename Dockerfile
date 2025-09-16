FROM python:3.11-slim

WORKDIR /app

# Copy the requirements file into the image
COPY requirements1.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements1.txt

# Copy the rest of the application files
COPY . .

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
