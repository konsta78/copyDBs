import psycopg2
import pyodbc


def db_connect(type_db, server, database, user=None, password=None):
    """
    Подключение к БД
    :param type_db: тип БД ('mssql' или 'postgresql')
    :param server: сервер
    :param database: база данных
    :param user: логин
    :param password: пароль
    :return: коннект
    """
    try:
        if type_db == 'mssql':
            conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; '
                                    'SERVER=' + server + ';'
                                    'DATBASE=' + database + ';'
                                    'Trusted_Connection=yes')
        elif type_db == 'postgresql':
            conn = psycopg2.connect(host=server, dbname=database, user=user, password=password)
        else:
            raise
        return conn
    except Exception as e:
        print(e)


def query_execute(connect, query, type_query, data=None):
    """
    Выполнение запросов к БД
    :param connect: соединение с БД
    :param query: текст запроса
    :param type_query: тип запроса ('select', 'delete', 'insert')
    :param data: данные для записи в БД
    :return: данные из БД (при 'select')
    """
    cursor = connect.cursor()
    if type_query == 'insert':
        cursor.executemany(query, data)
        connect.commit()
    elif type_query == 'delete':
        cursor.execute(query)
    elif type_query == 'select':
        cursor.execute(query)
        return cursor.fetchall()