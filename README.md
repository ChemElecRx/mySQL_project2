# mySQL_project2
This project includes two main scripts, app.py and upload_papers.py, which work together to extract metadata from PDF files of research papers and insert the extracted information into a MySQL database. The PyMuPDF library is used for PDF metadata extraction, and the mysql-connector-python library is used for MySQL database operations. Additionally, a simple web interface is provided in the templates folder for searching the database.

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
- mysql-connector-python library
- PyMuPDF (fitz) library

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
