#!/usr/bin/python3
""" lists all State objects from the database hbtn_0e_6_usa
using SQLAlchemy """
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
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
    Session = sessionmaker(bind=engine)
    session = Session()
    rs = session.query(State).order_by(State.id).first()
    if rs is None:
        print('Nothing')
    else:
        print("{}: {}".format(rs.id, rs.name))


if __name__ == "__main__":
    main()
