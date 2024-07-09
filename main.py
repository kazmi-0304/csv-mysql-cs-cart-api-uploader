import tkinter as tk
from tkinter import filedialog
import pandas as pd
import mysql.connector
from mysql.connector import Error
import time

def upload_to_mysql(file_path):
    try:
        # Connect to your MySQL database
        connection = mysql.connector.connect(host='localhost',
                                             database='allmbe_db',
                                             user='root',
                                             password='')

        # Fetching column names from the database table
        cursor = connection.cursor()
        cursor.execute("DESCRIBE cscart_products")  # Replace 'cart' with your actual table name
        columns = cursor.fetchall()
        cols = [f"`{col[0]}`" for col in columns]  # Extracting column names
        cursor.execute('SELECT * FROM cscart_products LIMIT 1')
        
        # Fetch the first row
        first_row = cursor.fetchone()
        print(len(first_row))
        # Read CSV file into DataFrame
        df = pd.read_csv(file_path)
        df = df.fillna('')

        # Insert DataFrame records one by one
        # for i, row in df.iterrows():
        while True:
            # Check if Item ID already exists
            record = ['', 'PPPP', 'A', 1, '0.00', 0, '0.000', 0, 0, 0, '0.00', 0, 1706057373, 1706057373, '0', 'N', 'N', 'N', None, 'N', None, 'N', 'N', 'N', 'Y', 10, 0, 'N', '', None, None, None, None, '', 'N', 0, None, None, '', 'a:5:{s:16:"min_items_in_box";i:0;s:16:"max_items_in_box";i:0;s:10:"box_length";i:0;s:9:"box_width";i:0;s:10:"box_height";i:0;}', '', 0, '', '0.000', '1.000']
            # print(row)
            # print(record)
            # # Preparing the SQL query
            sql = f"INSERT INTO cscart_products ({', '.join(cols[1:])}) VALUES ({', '.join(['%s'] * len(cols[1:]))})"
            print(len(record))
            # Fetch the first row
            # Executing the SQL query
            cursor = connection.cursor()
            cursor.execute(sql, record)
            connection.commit()

            time.sleep(0.5)
        else:
            print(f"Item ID already exists. Skipping.")


    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        # Close the connection and cursor
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def open_file_dialog():
    file_path = filedialog.askopenfilename()
    upload_to_mysql(file_path)

# Set up the tkinter UI
root = tk.Tk()
root.title("CSV to MySQL Uploader")
root.geometry("300x150")

open_file_button = tk.Button(root, text="Open CSV File", command=open_file_dialog)
open_file_button.pack(pady=20)

root.mainloop()
