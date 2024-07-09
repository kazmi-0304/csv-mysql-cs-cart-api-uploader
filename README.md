# Integrated CSV to MySQL & CS-Cart API Uploader

## Overview

The Integrated CSV to MySQL & CS-Cart API Uploader is a versatile Python application designed for seamless data management and synchronization between local CSV files, MySQL databases, and CS-Cart platforms. This utility enables users to efficiently upload data from CSV files into a MySQL database and simultaneously create product entries on a CS-Cart store through its API, ensuring data consistency across systems. Featuring a graphical user interface for file selection and comprehensive error handling, this tool caters to database administrators, e-commerce managers, and developers looking for an automated solution to manage product inventories and data workflows.

![Project Image Overview](https://github.com/DevRex-0201/Project-Images/blob/main/Py-CS-Cart-Products-Uploader.jpeg)

## Features

- **GUI for File Selection**: Offers a user-friendly interface for selecting CSV files, making it accessible for users of all technical levels.
- **MySQL Database Integration**: Automatically uploads CSV data into a MySQL database, with column mapping and validation checks to prevent duplicate entries.
- **CS-Cart API Integration**: Utilizes the CS-Cart API to create product entries on a CS-Cart platform, streamlining the e-commerce management process.
- **Comprehensive Error Handling**: Provides detailed error messages for troubleshooting connection issues, data insertion errors, and API response failures.
- **Configurable Data Mapping**: Allows for easy customization of data mapping between CSV columns, MySQL database fields, and CS-Cart product attributes.
- **Efficient Data Processing**: Implements a loop mechanism for continuous data processing, suitable for large data sets and bulk uploads.

## Prerequisites

- **Python 3.x**: Ensure Python 3.x is installed. Download from [the official Python website](https://www.python.org/downloads/).
- **MySQL Server**: Access to a MySQL server is required. Install MySQL on a local or remote server.
- **CS-Cart Store**: Access to a CS-Cart store and valid API credentials (email and API key) are necessary for API integration.
- **Python Libraries**: The script uses `tkinter`, `pandas`, `mysql.connector`, and `requests`. Install via pip:
  ```
  pip install pandas mysql-connector-python requests
  ```

## Installation

1. **Clone or Download the Repository**: Obtain the script files from the repository.
2. **Install Dependencies**: Use pip to install the required Python libraries.
3. **Configure Database and API Settings**: Edit the script to include your MySQL database details and CS-Cart API credentials.

## Configuration

- **Database Connection**: Adjust the `mysql.connector.connect` parameters to match your MySQL server's host, database, user, and password.
- **CS-Cart API Credentials**: Replace `email` and `api_key` variables with your CS-Cart store's API email and key.
- **Data Mapping**: Modify the data mapping in the `upload_to_mysql` function and `product_data` dictionary to align with your CSV format, MySQL schema, and CS-Cart product fields.

## Usage

1. **Run the Script**: Execute the script with Python to launch the GUI.
   ```
   python integrated_uploader.py
   ```
2. **Select CSV File**: Click on "Open CSV File" and choose your CSV file. The script will start processing the data for MySQL upload and CS-Cart API submission.
3. **Monitor Progress**: Follow the script's output in the console for progress updates, success messages, or error notifications.
4. **Verify Uploads**: Check your MySQL database and CS-Cart platform to confirm that the data has been uploaded successfully.

## Troubleshooting

- **Database Connection Issues**: Ensure your MySQL server is running and the connection details in the script are correct.
- **API Errors**: Verify your CS-Cart API credentials and ensure the store's API access is configured correctly.
- **Data Mismatch**: Confirm that the CSV file columns, MySQL table fields, and CS-Cart product attributes are correctly mapped in the script.

## Contributing

Contributions to enhance the Integrated CSV to MySQL & CS-Cart API Uploader are welcome. Please fork the repository, make your changes, and submit a pull request for review.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Support

For support, questions, or to report issues, please contact the repository owner or submit an issue on the project's issue tracker.
