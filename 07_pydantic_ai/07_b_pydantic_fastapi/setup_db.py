from utils import querry_duckdb

querry_duckdb(""" 

    CREATE TABLE IF NOT EXISTS movies (
              title STRING,
              year INT,
              genre STRING,
              rating TINYINT
    );
""")

if __name__ == "__main__":
    print(querry_duckdb("DESC;"))