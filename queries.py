# удаление таблицы
DELETE_POSTGRESQL_OSPS = "DELETE FROM tbl_osps"

# выборка всех записей из таблицы
SELECT_MSSQL_OSPS = 'SELECT * FROM water_supply.dbo.tbl_osp'

# вставка новых записей в таблицу ОСП
INSERT_POSTGRESQL_OSPS = 'INSERT INTO tbl_osps VALUES (%s, %s, %s)'

# выборка данных по сотрудникам
SELECT_MSSQL_EMPLOYEES = "SELECT УИД, Название, Почта, ДоменноеИмя FROM diadoc_test.dbo.tbl_emails_domains_fio WHERE ДоменноеИмя <> ''"

# вставка новых записей в таблицу сотрудников
INSERT_POSTGRESQL_EMPLOYEES = "INSERT INTO tbl_employees VALUES (%s, %s, %s, %s, true)"
