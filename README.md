# TMDB-Movie-Data-Processor-From-API-to-Database-with-FastAPI

This project demonstrates how to build an ETL pipeline (Extract, Transform, Load) using FastAPI and SQLite. It extracts movie data from the TMDB API, processes the data using Pandas, and stores the cleaned data in an SQLite database. It also includes an API for receiving and sending Excel files and uses OpenPyXL to generate and modify Excel reports.

Project Features

Fetch Raw Data: Fetch movie data in JSON format from the TMDB API.
Data Processing: Clean and transform the raw data using Pandas to structure it for further use.
Store Data: Store the cleaned data in an SQLite database.
API Development: Build an API to receive and send Excel files.
Excel File Generation: Use OpenPyXL to create and modify Excel files for reporting.
Testing Locally: Run the entire project locally using FastAPI and Uvicorn.
Project Requirements

Before running the project, make sure you have the following installed:

Python 3.7 or higher
SQLite (should come with Python)
FastAPI
Uvicorn
Pandas
OpenPyXL
Requests (for making HTTP requests to the TMDB API)

You can install the required dependencies using pip: pip install fastapi uvicorn pandas openpyxl requests

**Project Structure**
```
TMDB-Movie-Data-Processor-From-API-to-Database-with-FastAPI/
├── main.py            # FastAPI app
├── database.py        # SQLite database handling
├── models.py          # Pydantic models
├── etl.py             # ETL functions (fetching, processing, and storing data)
├── requirements.txt   # List of dependencies
└── README.md          # Project documentation
```


## **Running the Project**
### Step 1: Clone the Repository
Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/antrovibin/TMDB-Movie-Data-Processor-From-API-to-Database-with-FastAPI.git
```

### Step 2: Install Dependencies
Navigate to your project directory and install the required dependencies:

```
cd TMDB-Movie-Data-Processor-From-API-to-Database-with-FastAPI
pip install -r requirements.txt
```

### Step 3: Run the API Locally
To start the FastAPI application, run the following command in the project directory:

```
uvicorn main:app --reload
```
This will start the FastAPI server locally at http://127.0.0.1:8000.

### Step 4: Open the API Documentation
Once the server is running, you can view the interactive API documentation by navigating to:
```
http://127.0.0.1:8000/docs
```
This will open the Swagger UI, where you can interact with the API, test endpoints, and upload/download Excel files.

### Step 5: Test the Endpoints
You can test the following API endpoints:
```
GET /movies: Fetches a list of movies stored in the SQLite database.
POST /upload-excel: Uploads an Excel file to the API. The file will be processed and saved to the database.
GET /download-excel: Downloads the processed movie data as an Excel file.
```


## ETL Process

### Extract
The movie data is fetched from the TMDB API. The API returns movie details in JSON format. The etl.py script is responsible for extracting this raw data from the API.

### Transform
After extracting the raw data, we use Pandas to clean and transform it. The data is processed to include relevant columns such as:

Movie title
Release date
Genre
Rating
Overview
Load
Once the data is processed, it is loaded into an SQLite database for easy querying and future reference. The database is managed through the database.py script.
