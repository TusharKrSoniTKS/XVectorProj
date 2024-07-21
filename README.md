# XVectorProj
# Flask Data Visualization App

Welcome to the Flask Data Visualization App! This project allows you to upload CSV files, store them in a PostgreSQL database, and visualize the data using Plotly. Follow the steps below to set up and run the project.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
  - [1. Clone the Repository](#1-clone-the-repository)
  - [2. Setup PostgreSQL](#2-setup-postgresql)
  - [3. Configure the Environment](#3-configure-the-environment)
  - [4. Install Dependencies](#4-install-dependencies)
  - [5. Run the Application](#5-run-the-application)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [License](#license)

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8+**
- **PostgreSQL**
- **Git**

## Setup Instructions

### 1. Clone the Repository

Clone the repository to your local machine using the following command:

```sh
git clone https://github.com/TusharKrSoniTKS/XVectorProj.git
cd 1
cd my_flask_app
```

### 2. Setup PostgreSQL

Start PostgreSQL: Ensure PostgreSQL is running on your machine.

Create a Database: Create a new database for the project.

```sql
CREATE DATABASE mydatabase;
CREATE USER myuser WITH PASSWORD 'mypassword';
GRANT ALL PRIVILEGES ON DATABASE mydatabase TO myuser;
```
### 3. Configure the Environment

Set Environment Variables: Configure the database URL in your environment. Create a `init.py` file in the root directory with the following content: (PATH of the File-: XVectorProj/1/my_flask_app/app/__init__.py)

```env
DATABASE_URL=postgresql://myuser:mypassword@localhost/mydatabase
SECRET_KEY=your_secret_key
```

### 4. Install Dependencies

Install dependencies using pip:

```sh
pip install Flask psycopg2-binary pandas
pip install SQLAlchemy
```

### 5. Run the Application

Run the application using the following command:

```sh
python run.py
```

## Usage

### Uploading CSV Files

1. Navigate to the Data page.
2. Enter a table name and choose a CSV file.
3. Click the Upload button to upload the file and save it to the database.

### Viewing Data and Plots

1. Navigate to the Home page.
2. View the data from the database in the left column.
3. Select columns to plot in the right column and click Plot to visualize the data.


## Project Structure

```plaintext
flask-data-visualization-app/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── data.html
│   │   ├── index.html
│   │   └── plots.html
│   ├── static/
│   │   └── styles.css
│
├── uploads/
│
├── .env
├── run.py
└── README.md
```

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

### Apache License 2.0


