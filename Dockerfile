FROM python:slim

WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

# Run the script when the container launches
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
