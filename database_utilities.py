import pymysql


def connect_database_MySQL(database: str):
    # connects to the local MySQL server running in docker
    try:
        return pymysql.connect(host="localhost", port=3308, user="root", password="password", db=database)
        print("Connection to database successfully created")
    except:
        print("Connection to database not possible")


def create_database(database_selection: str, script_file_path: str):
    # generate the database and drops if already created
    conn = connect_database_MySQL(database_selection)
    cursor = conn.cursor()
    ddl = load_sql_script_from_file(script_file_path)
    cursor.execute(ddl)
    # conn.close()


def execute_database_sql_command(sql_command: str):
    conn = connect_database_MySQL("mydb")
    cursor = conn.cursor()
    cursor.execute(sql_command)


def load_sql_script_from_file(file_path: str):
    try:
        f = open(file_path, "r")
        return f.read()

    except FileNotFoundError:
        print("the file " + file_path + " could not be found")
        exit(2)
