import mysql.connector
from mysql.connector import Error

# Function to connect to the database
def connect_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",         # Replace with your MySQL host, e.g., "localhost"
            user="root",              # Replace with your MySQL username, e.g., "root"
            password="",              # Replace with your MySQL password if set
            database="hospital_db"    # Replace with your database name, or create a new one
        )
        if conn.is_connected():
            print("Connected to MySQL database")
        return conn
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

# Function to create the tables
def create_tables():
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()

            # Create `patients` table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS patients (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    phone VARCHAR(20) NOT NULL,
                    registered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)
            print("Table 'patients' created successfully.")

            # Create `tokens` table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS tokens (
                    token_id INT AUTO_INCREMENT PRIMARY KEY,
                    patient_id INT,
                    illness VARCHAR(255),
                    queue_status ENUM('waiting', 'in_progress', 'completed') DEFAULT 'waiting',
                    FOREIGN KEY (patient_id) REFERENCES patients(id) ON DELETE CASCADE
                );
            """)
            print("Table 'tokens' created successfully.")

            # Create `doctors` table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS doctors (
                    doctor_id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    specialization VARCHAR(255) NOT NULL,
                    contact_number VARCHAR(20)
                );
            """)
            print("Table 'doctors' created successfully.")

            # Commit changes to the database
            conn.commit()

        except Error as e:
            print(f"Error creating tables: {e}")
        finally:
            cursor.close()
            conn.close()

# Call the function to create the tables
create_tables()
