###########################################
# Копирование данных из MSSQL в PostgreSQL
# Создано: 12.08.2022
###########################################

import functions as f
import queries as q

MSSQL_SERVER = 'M1-CTX-1001'
MSSQL_DB = 'water_supply'

PG_SERVER = '10.214.37.55'
PG_DB = 'water_supply_dev'
PG_USER = 'developer'
PG_PASSWORD = 'DDP1Md40yQ'


if __name__ == '__main__':
    connect_mssql = f.db_connect('mssql', MSSQL_SERVER, MSSQL_DB)
    # data = f.query_execute(connect_mssql, q.SELECT_MSSQL_OSPS, 'select')
    data = f.query_execute(connect_mssql, q.SELECT_MSSQL_EMPLOYEES, 'select')
    connect_mssql.close()

    connect_posgresql = f.db_connect('postgresql', PG_SERVER, PG_DB, PG_USER, PG_PASSWORD)
    # f.query_execute(connect_posgresql, q.DELETE_POSTGRESQL_OSPS, 'delete')
    # f.query_execute(connect_posgresql, q.INSERT_POSTGRESQL_OSPS, 'insert', data=data)
    f.query_execute(connect_posgresql, q.INSERT_POSTGRESQL_EMPLOYEES, 'insert', data=data)
    connect_posgresql.close()