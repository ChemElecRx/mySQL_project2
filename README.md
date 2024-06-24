# mySQL_project2
This project involves extracting metadata from PDF files containing research papers and storing this metadata in a MySQL database. Additionally, it includes a simple web interface for searching through the stored metadata.

## Porject Structure
```
.
├── ai_papers/               # Directory containing PDF files
├── app.py
├── requirements.txt         # List of Python dependencies
├── schema.sql               # SQL schema for setting up the MySQL database
├── scripts
│   └── cleanup.sh
├── templates
│   └── index.html           # HTML template for the search page
└── upload_papers.py
```
## Prerequisites
- Python 3.x
- MySQL

## Python Environment Setup
Create a virtual environment:
```
python3 -m venv env
```
Activate the virtual environment:

- On macOS and Linux:
```
source env/bin/activate
```
- On Windows:
```
.\env\Scripts\activate
```
Install the required libraries using:
```
pip3 install -r requirements.txt
```
Deactivate the virtual environment after use:
```
deactivate
```
## MySQL Database Setup
Start MySQL (macOS using Homebrew):
```
brew services start mysql
```
Set up the MySQL database schema using:
```
mysql -u root -p < schema.sql
```
Stop MySQL (macOS using Homebrew):
```
brew services stop mysql
```
## Running the Application
```
python3 upload_papers.py
python3 app.py
```
Open your web browser and navigate to the specified URL to use the web interface for searching through the stored metadata.
## Cleanup Script

1. Set the executable permission for the cleanup script:
    ```
    chmod +x cleanup.sh
    ```

2. Run the cleanup script:
    ```
    ./cleanup.sh
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
