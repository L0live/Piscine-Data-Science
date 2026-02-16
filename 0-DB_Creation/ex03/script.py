from sys import argv
import os.path as osp
from os import listdir

def main():
    assert len(argv) == 2, "Usage: python script.py <csv_directory>"

    csv_directory = argv[1]
    assert osp.isdir(csv_directory), f"Directory '{csv_directory}' does not exist"

    print(f"Generating SQL script for CSV files in directory '{csv_directory}'...")

    csv_files = [f for f in listdir(csv_directory) if f.endswith('.csv')]
    assert csv_files, f"No CSV files found in directory '{csv_directory}'"

    table_template = "(event_time TIMESTAMPTZ, event_type VARCHAR(50), product_id SERIAL, price REAL, user_id BIGINT, user_session UUID);"

    sql_script = ""

    for csv_file in csv_files:
        print(f"Processing file: {csv_file}")
        table_name = osp.splitext(csv_file)[0]
        sql_script += f"CREATE TABLE {table_name}{table_template}\n"
        sql_script += f"\copy {table_name}(event_time, event_type, product_id, price, user_id, user_session)"
        sql_script += f" FROM '{osp.join(csv_directory, csv_file)}' WITH (FORMAT csv, HEADER true, DELIMITER ',');\n\n"
        print(f"Added SQL commands for table '{table_name}' to the script.")
    
    with open("import_data.sql", "w") as f:
        f.write(sql_script)
    
    print(f"SQL script 'import_data.sql' has been generated successfully for all CSV files in directory '{csv_directory}'.")

if __name__ == "__main__":
    main()