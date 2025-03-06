# receipt_fastapi

The purpose of this project is to experiment with and learn the fastapi framework. This includes pydantic validation, lifecycle, and pytest cases.
This is a FastAPI application that processes receipts, calculates points based on defined rules, and returns the points for a given receipt ID.

## Requirements

- Docker (Docker Desktop should work fine)
- Git

## Setup

1. **Clone the Repository**  
   Clone the repository to your local machine:

   ```bash
   git clone https://github.com/sahilmtayade/receipt_fastapi.git
   cd receipt_fastapi
   ```

2. **Build the Docker Image**  
   Build the Docker image using the following command:

   ```bash
   docker build -t fastapi-receipt-processor .
   ```

3. **Run the Application**  
   Run the application using Docker:

   ```bash
   docker run -p 8000:8000 fastapi-receipt-processor
   ```

   This will start the FastAPI application on port 8000. You can access the FastAPI documentation and test the endpoints at http://localhost:8000/docs. To change ports, change `-p <port>:8000` with your desired port.
### Swagger UI
![image](https://github.com/user-attachments/assets/6aeee4c1-d370-4600-bcd8-ad2dc1b396e8)
![image](https://github.com/user-attachments/assets/6d54ff4b-84d7-4cbd-885b-6265eb02aedd)
![image](https://github.com/user-attachments/assets/dd154f69-08e1-4edf-8d02-07510189a2f4)
### Redoc
![image](https://github.com/user-attachments/assets/257da9e4-1722-4136-869c-08710a8a18c4)
