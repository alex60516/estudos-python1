import sqlite3
import pandas as pd

conexao = sqlite3.connect(":memory:")
cursor = conexao.cursor()

cursor.execute("CREATE TABLE alunos (nome TEXT, nota REAL)")

cursor.execute("INSERT INTO alunos VALUES ('Ana', 8.5)")
cursor.execute("INSERT INTO alunos VALUES ('Lucas', 5.0)")
cursor.execute("INSERT INTO alunos VALUES ('Maria', 9.5)")
cursor.execute("INSERT INTO alunos VALUES ('Pedro', 6.5)")
cursor.execute("INSERT INTO alunos VALUES ('Julia', 4.0)")
cursor.execute("INSERT INTO alunos VALUES ('joao', 3.0)")

cursor.execute("SELECT * FROM alunos")
print(cursor.fetchall())

cursor.execute("SELECT nome FROM alunos WHERE nota >= 6")
print(cursor.fetchall)

cursor.execute("SELECT nome FROM alunos WHERE nota < 6")
print(cursor.fetchall())

cursor.execute("SELECT AVG(nota) FROM alunos")
print(cursor.fetchall)

tabela = pd.read_sql_query("SELECT *FROM alunos", conexao)
print(tabela)
print(tabela["nota"].max)
