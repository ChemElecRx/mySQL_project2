# mySQL_project2
This script extracts metadata from PDF files of research papers and inserts the extracted information into a MySQL database. It uses the PyMuPDF library for PDF metadata extraction and the mysql.connector library for MySQL database operations.

## Prerequisites
- Python 3.x
- mysql-connector-python library
- PyMuPDF (fitz) library
```pip install -r requirements.txt```

```
CREATE TABLE papers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    authors VARCHAR(255),
    abstract TEXT,
    keywords VARCHAR(255),
    publication_date DATE,
    file_name VARCHAR(255)
);
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
