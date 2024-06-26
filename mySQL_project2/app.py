from flask import Flask, request, render_template, jsonify, send_from_directory
import pymysql
from pymysql.cursors import DictCursor
import os

app = Flask(__name__)

# Get MySQL password from environment variable
mysql_password = os.getenv("MYSQL_PASSWORD")

# Database connection
def get_db_connection():
    return pymysql.connect(user='root', password=mysql_password, host='localhost', database='research_papers_db')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT title, authors, keywords, file_name FROM papers WHERE title LIKE %s OR keywords LIKE %s"
            cursor.execute(sql, ('%' + query + '%', '%' + query + '%'))
            results = cursor.fetchall()
    finally:
        connection.close()
    return jsonify(results)

@app.route('/ai_papers/<path:filename>')
def pdf(filename):
    return send_from_directory('ai_papers', filename)

if __name__ == '__main__': # Commented out or removed for Gunicorn
    # Find the ip address of system using ifconfig command
    # Replace the host ip in code with your ip
    app.run(host='127.0.0.1', port=5000, debug=True, threaded=False) # Commented out or removed for Gunicorn
    # pip3 install gunicorn
    # gunicorn -w 4 -b 127.0.0.1:5000 app:app
    # gunicorn -w 4 -b 127.0.0.1:5000 --access-logfile access.log app:app
