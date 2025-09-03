# Step 1: Base image (Python environment)
FROM python:3.10

# Step 2: Set working directory inside container
WORKDIR ./app .

# Step 3: Copy dependencies
COPY requirements.txt .

# Step 4: Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy rest of the app
COPY . .

# Step 6: Run Flask app
CMD ["python", "app.py"]
