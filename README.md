# mySQL_project2
This project involves extracting metadata from PDF files containing research papers and storing this metadata in a MySQL database. Additionally, it includes a simple web interface for searching through the stored metadata.

## Porject Structure
```
.
├── ai_papers/               # Directory containing PDF files
├── templates/               
│   └── index.html           # HTML template for the search page
├── app.py                   
├── requirements.txt         # List of Python dependencies
├── schema.sql               # SQL schema for setting up the MySQL database
└── upload_papers.py
```
## Prerequisites
- Python 3.x

Install the required libraries using:
```
pip install -r requirements.txt
```
Set up the MySQL database schema using:
```
mysql -u root -p < schema.sql
```


## Modules and Libraries
* mysql.connector: To connect and interact with the MySQL database.
* os: For file and environment variable handling.
* fitz (PyMuPDF): To extract metadata from PDF files.

## Database Connection
Connects to the MySQL database using the mysql.connector.connect() function, with the password retrieved from the environment variable MYSQL_PASSWORD.

## Notes
- Ensure the PDF files contain the required metadata.
- The script logs errors to error_log.txt and prints them to the console.
- The script truncates the authors' field if it exceeds 255 characters to avoid database insertion errors.
