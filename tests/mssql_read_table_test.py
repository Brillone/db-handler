import json
from db_handler.mssql.mssql_read import MSSQLTableReader
import time


def read_table_offset(reader):
    start = time.time()
    table = reader.read_table(table_name='TableTest', offset=0, chunk_size=100000, column=None)
    elapsed = time.time() - start

    print('Elapsed time - {}'.format(elapsed))

    print('Table is empty - {}'.format(table.empty))

    print('Table has duplications - {}'.format(table.duplicated().any()))

    return table


def read_table_col(reader):
    start = time.time()
    table = reader.read_table(table_name='TableTest', offset=1, chunk_size=100000, column='ident')
    elapsed = time.time() - start

    print('Elapsed time - {}'.format(elapsed))

    print('Table is empty - {}'.format(table.empty))

    print('Table has duplications - {}'.format(table.duplicated().any()))

    return table


if __name__ == '__main__':
    # config
    config_file_path = 'config/db_conn.json'
    with open(config_file_path, 'r') as fp:
        db_config = json.load(fp)

    # reader
    reader = MSSQLTableReader(**db_config)

    # tests
    table = read_table_offset(reader)
    print(table.shape)
    table = read_table_col(reader)
    print(table.shape)
