import psycopg2

from configparser import ConfigParser
from psycopg2.extensions import connection


def config_db():
    global db_host, db_port, db_username, db_password, db_name

    parser = ConfigParser()
    parser.read("pipeline.conf")

    db_host = parser.get("db_config", "host")
    db_port = parser.get("db_config", "port")
    db_username = parser.get("db_config", "username")
    db_password = parser.get("db_config", "password")
    db_name = parser.get("db_config", "database")


def get_db_conn() -> connection:
    db_conn = psycopg2.connect(
        host=db_host,
        port=db_port,
        user=db_username,
        password=db_password,
        database=db_name,
    )

    if db_conn is None:
        print("Failed to connect to db")
        exit(1)

    return db_conn
