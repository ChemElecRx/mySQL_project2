from flask import Flask, request, render_template, jsonify
import pymysql
from pymysql.cursors import DictCursor
import os

app = Flask(__name__)

# Get MySQL password from environment variable
mysql_password = os.getenv("MYSQL_PASSWORD")

# Database connection
def get_db_connection():
    return pymysql.connect(user='root', password=mysql_password, host='localhost', database='research_papers_2')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT title, file_name FROM papers WHERE title LIKE %s OR keywords LIKE %s"
            cursor.execute(sql, ('%' + query + '%', '%' + query + '%'))
            results = cursor.fetchall()
    finally:
        connection.close()
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
