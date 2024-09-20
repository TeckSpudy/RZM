
# Project Name

## Overview
A brief description of what the web application does and its key features.

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
git clone https://github.com/yourusername/yourproject.git
cd yourproject
```

### 2. **Install Dependencies**

Ensure all Python dependencies are installed. The project uses a `requirements.txt` file to list them:

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
    mysql -u root -p your_database_name < RZM.sql
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

### 2. **MySQL Error: Data Too Long for Column 'immagine'**
Ensure that the `immagine` column in the database has sufficient size (e.g., use `VARCHAR(255)`).

---

## Contributions
Explain how others can contribute to the project (optional).

---

## License
Specify the license under which the project is released (e.g., MIT License).
