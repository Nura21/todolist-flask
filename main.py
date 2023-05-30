import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request
import requests

@app.route('/create', methods=['POST'])
def create_todo():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    try:
        _json = request.json
        _name = _json['name']
        _description = _json['description']

        if _name and _description and request.method == 'POST':
            sqlQuery = "INSERT INTO todos(name, description) VALUES(%s, %s)"
            bindData = (_name, _description)
            cursor.execute(sqlQuery, bindData)
            conn.commit()

            response = jsonify('Todo added successfully!')
            response.status_code = 200
            
            return response
        else:
            return showMessage()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/todo')
def todo():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        
        cursor.execute("SELECT * FROM todos")
        todoRows = cursor.fetchall()
        
        response = jsonify(todoRows)
        response.status_code = 200
        
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/todo/<int:todo_id>')
def todo_details(todo_id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        
        cursor.execute("SELECT * FROM todos WHERE id =%s", todo_id)
        todoRow = cursor.fetchone()
        
        response = jsonify(todoRow)
        response.status_code = 200

        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/update', methods=['PUT'])
def update_todo():
    try:
        _json = request.json
        _id = _json['id']
        _name = _json['name']
        _description = _json['description']

        if _name and _description and request.method == 'PUT':
            sqlQuery = "UPDATE todos SET name=%s, description=%s WHERE id=%s"
            bindData = (_name, _description, _id)
            conn = mysql.connect()
            cursor = conn.cursor()
            
            cursor.execute(sqlQuery, bindData)
            conn.commit()

            response = jsonify('Todo updated sucessfully!')
            response.status_code = 200

            return response
        else:
            return showMessage()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_todo(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        
        cursor.execute("DELETE FROM todos WHERE id =%s", (id,))
        conn.commit()

        response = jsonify('Todo deleted successfully!')
        response.status_code = 200

        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.errorhandler(404)
def showMessage(error=None):
    message = {
        'status' : 404,
        'message' : 'Record not found: ' + request.url,
    }

    response = jsonify(message)
    response.status_code = 404

    return response

if __name__ == "__main__":
    app.run()