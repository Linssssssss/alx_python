#!/usr/bin/python3
""" lists all State objects from the database hbtn_0e_6_usa
using SQLAlchemy """
import sys
from sqlalchemy import create_engine
from sqlalchemy.sql import select
from model_state import Base, State


def main():
    """main function """

    dialect = 'mysql'
    driver = 'mysqldb'
    username = sys.argv[1]
    password = sys.argv[2]
    host = 'localhost'
    port = '3306'
    database = sys.argv[3]
    engine = create_engine("{}+{}://{}:{}@{}:{}/{}".format(dialect,
                                                           driver,
                                                           username,
                                                           password,
                                                           host,
                                                           port,
                                                           database))
    with engine.connect() as conn:
        rs = conn.execute('SELECT * FROM states ORDER BY id ASC')
        for r in rs:
            print("{}: {}".format(r[0], r[1]))


if __name__ == "__main__":
    main()
