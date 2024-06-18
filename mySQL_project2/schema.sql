-- Create database if not exists
CREATE DATABASE IF NOT EXISTS research_papers_db;

-- Use the created database
USE research_papers_db;

-- Table to store information about research papers
CREATE TABLE IF NOT EXISTS papers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    authors VARCHAR(255),
    abstract TEXT,
    keywords VARCHAR(255),
    publication_date DATE,
    file_name VARCHAR(255)
);