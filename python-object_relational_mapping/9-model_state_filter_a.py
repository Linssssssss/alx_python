#!/usr/bin/env python3
"""
Script to list all State objects that contain the letter 'a'
from the database hbtn_0e_6_usa using SQLAlchemy.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>".format(
            sys.argv[0]))
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Creating an engine to connect to the MySQL server
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            mysql_username, mysql_password, database_name
        )
    )

    # Creating a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Querying the database for State objects containing the letter 'a'
    states_with_a = (
        session.query(State)
        .filter(State.name.contains("a"))
        .order_by(State.id)
        .all()
    )

    # Displaying the results
    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))

    # Closing the session
    session.close()
