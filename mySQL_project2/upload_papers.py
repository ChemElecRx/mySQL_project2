import mysql.connector
import os
import fitz  # PyMuPDF

# Get MySQL password from environment variable
mysql_password = os.getenv("MYSQL_PASSWORD")

# Database connection
try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password=mysql_password,
        database="research_papers_db"
    )
    cursor = db.cursor()
    print("Database connection successful")
except mysql.connector.Error as err:
    print(f"Error: {err}")
    exit(1)

# Directory containing the research papers
papers_dir = "./ai_papers"

# File to store error messages
error_log_file = "error_log.txt"

# Function to log error messages
def log_error(error_message):
    with open(error_log_file, "a") as log_file:
        log_file.write(error_message + "\n")

# Function to extract metadata from PDF file using PyMuPDF (fitz)
def extract_metadata(file_path):
    title, authors, keywords, publication_date = "Unknown Title", "Unknown Authors", "Unknown Keywords", "1900-01-01"
    try:
        doc = fitz.open(file_path)
        metadata = doc.metadata
        
        # Normalize the dictionary keys to lowercase
        metadata_normalized = {k.lower(): v for k, v in metadata.items()}

        title = metadata_normalized.get("title", "Unknown Title")
        authors = metadata_normalized.get("author", "Unknown Authors")
        keywords = metadata_normalized.get("keywords", "Unknown Keywords")
        
        # Extracting publication date in a standard format
        raw_publication_date = metadata_normalized.get("creationdate", "D:19000101000000")
        publication_date = raw_publication_date.split('D:')[1][:8]  # Extracting 'YYYYMMDD' from 'D:20190327235443-07'00''
        
        # Format the publication_date as 'YYYY-MM-DD'
        publication_date = f"{publication_date[:4]}-{publication_date[4:6]}-{publication_date[6:]}"
        
    except Exception as e:
        error_message = f"Error reading PDF '{file_path}': {str(e)}"
        log_error(error_message)
        print(error_message)
    
    return title, authors, keywords, publication_date

# Upload papers
for file_name in os.listdir(papers_dir):
    if file_name.endswith(".pdf"):
        file_path = os.path.join(papers_dir, file_name)
        
        title, authors, keywords, publication_date = extract_metadata(file_path)
        
        # For abstract, set it to None (NULL in MySQL)
        abstract = None

        sql = "INSERT INTO papers (title, authors, abstract, keywords, publication_date, file_name) VALUES (%s, %s, %s, %s, %s, %s)"
        
        # Truncate authors if it exceeds 255 characters
        authors = authors[:255] if len(authors) > 255 else authors
        
        val = (title, authors, abstract, keywords, publication_date, file_name)
        
        try:
            cursor.execute(sql, val)
            db.commit()
            print(f"Inserted {file_name} successfully")
        except mysql.connector.Error as err:
            error_message = f"Error inserting file '{file_name}' into database: {err}"
            log_error(error_message)
            print(error_message)
            continue

cursor.close()
db.close()

