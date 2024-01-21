FROM python:3.9

# Install necessary packages
RUN apt-get update && \
    apt-get install -y git && \
    pip install tox

# Set working directory
WORKDIR /app

# Copy the project files into the container
COPY . /app

# Run tox
CMD ["tox"]