
# RZM-Outlet Project

## Overview
This is a school project that I created with my classmates. It is a working flask webapp with a mysql database. It displays already existing merch (for sale) and the possibility to add new ones.

---

## Prerequisites
Make sure the user has the necessary tools and software installed before running the project:
- Python 3.x
- MySQL Server
- `pip` (Python package installer)

---

## Setup Instructions

### 1. **Clone the Repository**

```bash
git clone https://github.com/TeckSpudy/RZM.git
cd RZM
```

### 2. **Install Dependencies**

Ensure that all Python dependencies are installed. The program should install them automatically; if it doesn't, try to install them manually. The project utilizes a requirements.txt file to specify the dependencies:
```bash
pip install -r requirements.txt
```

### 3. **Database Setup**

#### Option 1: Importing the SQL Dump
1. Open MySQL and create the database:
    ```sql
    CREATE DATABASE your_database_name;
    ```
2. Import the database dump (`RZM.sql`):
    ```bash
    mysql -u root -p your_database_name < DB/RZM.sql
    ```

#### Option 2: Database Initialization via the Application
The app can create the database schema automatically upon the first run. Ensure your MySQL server is running, and adjust the database connection settings in the `config` section of the app:
```python
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'rzm'
```

---

### 4. **Update Configuration**

You may need to adjust certain configuration variables like the MySQL credentials, upload folder paths, etc.

1. Open the main configuration file (`rzm.py`).
2. Modify these lines to match your local setup:
```python
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'your_password'
app.config['MYSQL_DB'] = 'rzm'
```

### 5. **Run the Application**

Once everything is set up, run the application:

```bash
python rzm.py
```

The app will be available at `http://127.0.0.1:5000`.

---

### 6. **Optional: Virtual Environment Setup**
It's recommended to run the app inside a virtual environment to avoid conflicts with other projects:

1. Create a virtual environment:
    ```bash
    python3 -m venv rzmenv
    ```
2. Activate the virtual environment:
    - On macOS/Linux:
        ```bash
        source rzmenv/bin/activate
        ```
    - On Windows:
        ```bash
        rzmenv\Scripts\activate
        ```
3. Install the dependencies inside the virtual environment:
    ```bash
    pip install -r requirements.txt
    ```

---

## Common Issues

### 1. **MySQL Error: Access Denied**
Make sure your MySQL server is running and you have the correct credentials in your config.

---

## License
This project is completely open source software!
