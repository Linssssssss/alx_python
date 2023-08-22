#!/usr/bin/env python3
"""Script that lists all State objects from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <mysql username> <mysql password> <database name>".format(
            sys.argv[0]))
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create an engine to connect to the database
    engine = create_engine(
        f'mysql+mysqldb://{mysql_username}:{mysql_password}@localhost:3306/{database_name}',
        pool_pre_ping=True
    )

    # Bind the engine to the Base class
    Base.metadata.create_all(engine)

    # Create a Session class bound to the engine
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State objects from the database and sort by states.id
    states = session.query(State).order_by(State.id).all()
