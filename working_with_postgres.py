"""
Python scripts to work with postgres db, can be used to add and read the data from the tables
pre-requisites: we need to have postgres db and the data base

Manual commands to create a table in postgres
db_endpoint = postgresql://postgres:changeit@localhost:5432/aws_actions
CREATE TABLE accounts (
	execution_id serial PRIMARY KEY,
	user_id VARCHAR ( 50 )  NOT NULL,
	status_code VARCHAR ( 255 )  NOT NULL,
	created_on TIMESTAMP NOT NULL,
    action_type VARCHAR ( 255 )  NOT NULL
);

'INSERT INTO accounts(execution_id, user_id, status_code, created_on, action_type)
VALUES(1,'ramguthula','200','2022-03-31','GET'),(2, 'ramguthula', '500', '2022-03-31 9:30:22', 'PUT'),
(3, "ramguthula", "200", "2022-03-31 9:30:22", "GET")'


"""

from sqlalchemy import create_engine, Integer, Date, Table, Column, String, MetaData, inspect


def table_info(table_name: str) -> tuple:
    """
    this method used to supply data to other methods
    :param table_name: name of the table
    :return: tuple
    """
    db_string = "postgresql://postgres:changeit@localhost:5432/aws_actions"
    db = create_engine(db_string)
    meta = MetaData(db)
    return (Table(table_name, meta,
                  Column('execution_id', Integer, primary_key=True, nullable=False),
                  Column('user_id', String),
                  Column('status_code', Integer),
                  Column('created_on', Date),
                  Column('action_type', String),
                  ), db)


def create_table(table_name: str) -> None:
    """
    Method used to create a table in existing database 'aws_actions'
    :param table_name: name of the table
    :return: none
    """
    try:
        accounts_table = table_info(table_name)[0]

        inspector = inspect(table_info(table_name)[1])
        if inspector.has_table(table_name) is True:
            print("Table exists already")
        else:
            print("Table doesn't exist, Creating new table....")
            return accounts_table.create()

    except Exception as error:
        return error


def add_data(table_name: str) -> None:
    """
    this method adds data to the table supplied, make sure table exists already
    :param table_name: name of the table to read the data
    :return: dic
    """
    try:
        table_params = table_info(table_name)[0]
        db = table_info(table_name)[1]
        insert_statement = table_params.insert().values(user_id="ramguthula",
                                                        status_code=500,
                                                        created_on='2022-06-08 9:30:22',
                                                        action_type='PUT')
        return db.execute(insert_statement)
    except Exception as error:
        return error


def read_data(table_name: str) -> list:
    try:
        db = table_info(table_name)[1]
        result_set = db.execute(f"SELECT * FROM {table_name}")
        return [print(r) for r in result_set]

    except Exception as error:
        return error


if __name__ == "__main__":
    db_add_data = add_data('dummy_table')
    db_read_data = read_data('dummy_table')
