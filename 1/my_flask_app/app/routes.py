from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from werkzeug.utils import secure_filename
import pandas as pd
import os
from app import db
from sqlalchemy.sql import text
import json

main = Blueprint('main', __name__)
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'csv'}
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@main.route('/')
def index():
    tables = []
    with db.engine.connect() as connection:
        result = connection.execute(text("SELECT table_name FROM information_schema.tables WHERE table_schema='public'"))
        tables = [row[0] for row in result]
    
    table_data = {}
    for table in tables:
        with db.engine.connect() as connection:
            query = f'SELECT * FROM "{table}" LIMIT 10'
            result = connection.execute(text(query))
            columns = list(result.keys())  # Convert RMKeyView to a list
            rows = [list(row) for row in result]
            table_data[table] = {
                'columns': columns,
                'rows': rows
            }
    
    return render_template('index.html', tables=tables, table_data=table_data)

@main.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        if 'file' not in request.files or 'table_name' not in request.form:
            flash('No file or table name provided')
            return redirect(request.url)
        file = request.files['file']
        table_name = request.form['table_name']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            file.save(filepath)
            
            # Load CSV file into DataFrame
            df = pd.read_csv(filepath)
            
            # Save DataFrame to PostgreSQL
            df.to_sql(table_name, db.engine, if_exists='replace', index=False)
            
            flash('File successfully uploaded and saved to database')
            return redirect(url_for('main.data'))
    
    # Fetch existing table names
    with db.engine.connect() as connection:
        result = connection.execute(text("SELECT table_name FROM information_schema.tables WHERE table_schema='public'"))
        table_names = [row[0] for row in result]

    return render_template('data.html', table_names=table_names)

@main.route('/get_columns', methods=['GET'])
def get_columns():
    table_name = request.args.get('table_name')
    columns = []
    if table_name:
        with db.engine.connect() as connection:
            result = connection.execute(text(f"SELECT column_name FROM information_schema.columns WHERE table_name = :table_name"), {'table_name': table_name})
            columns = [row[0] for row in result]
    return jsonify(columns)

@main.route('/plot_data', methods=['POST'])
def plot_data():
    data_name = request.form.get('data_name')
    column1 = request.form.get('column1')
    column2 = request.form.get('column2')
    
    if data_name and column1 and column2:
        with db.engine.connect() as connection:
            result = connection.execute(text(f'SELECT "{column1}", "{column2}" FROM "{data_name}" LIMIT 25'))
            data = [{"x": row[0], "y": row[1]} for row in result]
        return jsonify({'data': data, 'column1': column1, 'column2': column2, 'data_name': data_name})
    
    return jsonify({'error': 'Invalid request'}), 400

@main.route('/plots', methods=['GET', 'POST'])
def plots():
    value = None
    data = None
    operation = None
    column_name = None
    column1 = None
    column2 = None
    data_name = None
    
    if request.method == 'POST':
        data_name = request.form.get('data_name')
        column_name = request.form.get('column_name')
        operation = request.form.get('operation')
        
        if data_name and column_name and operation:
            # Fetch the data and perform the operation
            with db.engine.connect() as connection:
                result = connection.execute(text(f'SELECT {operation}("{column_name}") FROM "{data_name}"'))
                value = [row[0] for row in result][0]
            return jsonify({'value': value, 'operation': operation, 'column_name': column_name, 'data_name': data_name})
        
        column1 = request.form.get('column1')
        column2 = request.form.get('column2')
        
        if data_name and column1 and column2:
            # Fetch the data for plotting
            with db.engine.connect() as connection:
                result = connection.execute(text(f'SELECT "{column1}", "{column2}" FROM "{data_name}" LIMIT 25'))
                data = [{"x": row[0], "y": row[1]} for row in result]
                return jsonify({'data': data, 'column1': column1, 'column2': column2, 'data_name': data_name})
    
    # Fetch existing table names
    with db.engine.connect() as connection:
        result = connection.execute(text("SELECT table_name FROM information_schema.tables WHERE table_schema='public'"))
        table_names = [row[0] for row in result]
    
    return render_template('plots.html', table_names=table_names)
