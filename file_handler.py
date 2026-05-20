import csv
import json
import os
from utils.logger import log_action

@log_action
def read_csv_rows(file_path):
    rows = []
    try:
        with open(file_path, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                rows.append(row)
    except FileNotFoundError:
        print("Error: CSV file not found:", file_path)
    except OSError as error:
        print("File error:", error)
    return rows


@log_action
def write_csv(file_path, fieldnames, rows):
    """Write a list of dictionaries to CSV."""
    try:
        folder = os.path.dirname(file_path)
        if folder != "" and not os.path.exists(folder):
            os.makedirs(folder)
        with open(file_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
    except OSError as error:
        print("File error:", error)


@log_action
def write_json(file_path, data):
    """Write data to a JSON file."""
    try:
        folder = os.path.dirname(file_path)
        if folder != "" and not os.path.exists(folder):
            os.makedirs(folder)
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
    except OSError as error:
        print("File error:", error)