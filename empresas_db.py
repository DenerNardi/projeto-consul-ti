import sqlite3 as sql




connection = sql.connect('empresas_db.db')
cursor = connection.cursor()
cursor.execute('DROP TABLE IF EXISTS empresas')

sql = '''CREATE TABLE "empresas" (
    "idempresas" INTEGER PRIMARY KEY AUTOINCREMENT,
    "razao_social" TEXT,
    "nome_fantasia" TEXT,
    "cnpj" TEXT
    )'''

cursor.execute(sql)
connection.commit()
connection.close()