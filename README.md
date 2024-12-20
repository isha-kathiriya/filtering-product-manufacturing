# Data Merging and Mismatched Rows Extraction

This repository contains a Python script that merges two Excel files and extracts rows that do not match based on the `Product name` and `Manufacturere` columns. These mismatched rows are saved to a CSV file.

## How to run the script:
1. Install the required Python libraries by running the following command:
    ```
    pip install pandas
    pip install pandas openpyxl
    ```
2. Run the Python script:
    ```
    python process_data.py
    ```
3. The mismatched rows will be saved in the `topic_df.csv` file.

## Example of `topic_df.csv` content:
The CSV file will contain products that either exist only in the first dataset (`left_only`) or only in the second dataset (`right_only`).

## Requirements:
- Python 3.x
- pandas
- openpyxl (for reading Excel files)
