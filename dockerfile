# Use the official Miniconda3 image
FROM continuumio/miniconda3

# Set the working directory inside the container
WORKDIR /app

# Copy environment.yml (if you have it)
COPY . /app/

# Create the environment using the environment.yml file
RUN conda env create -f environment.yml

# Activate the environment and install any additional dependencies
SHELL ["conda", "run", "-n", "receipt_processor", "/bin/bash", "-c"]

# Expose the port for FastAPI
EXPOSE 8000

# Run the FastAPI app using Uvicorn
CMD ["conda", "run", "-n", "receipt_processor", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
