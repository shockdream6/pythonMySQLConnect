import argparse
import database_utilities
import os

if __name__ == "__main__":
    # database code
    # database directory closs plattform of sql create database script
    os.chdir(os.path.dirname(__file__))
    path = os.path.join(os.getcwd(), "sql_script")
    # commandline function
    parser = argparse.ArgumentParser(description="Enter SQL command:")
    parser.add_argument("--create", action="call_create_database")
    parser.add_argument("sqlQuery1", type=str, help="SQL statement to execute")
    args = parser.parse_args()
    print(args.sqlQuery1)
    database_utilities.execute_database_sql_command(args.sqlQuery1)
    print("Command executed")


def call_create_database():
    database_utilities.create_database(database_selection="mydb", script_file_path=path)
    # print(database_utilities.load_sql_script_from_file(path))
