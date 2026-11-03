import sqlite3

conexao = sqlite3.connect(":memory:")
cursor = conexao.cursor()

cursor.execute("create table alunos (nome text, nota real)")

cursor.execute("insert into alunos values ('ana', 8.5)")
cursor.execute("insert into alunos values ('lucas', 5.0)")
cursor.execute("insert into alunos values ('maria', 9.5)")
cursor.execute("insert into alunos values ('pedro', 6.5)")

cursor.execute("select * from alunos")
print(cursor.fetchall())

cursor.execute("select nome from alunos where nota < 6")
print(cursor.fetchall())

cursor.execute("select avg(nota) from alunos")
print(cursor.fetchall())

cursor.execute("select nome, nota from alunos order by nota desc")
print(cursor.fetchall())