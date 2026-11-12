import sqlite3

conexao = sqlite3.connect(":memory:")
cursor = conexao.cursor()

cursor.execute("create table alunos (nome text, turma text, nota real)")
cursor.execute("insert into alunos values ('ana', 'A', 8.5)")
cursor.execute("insert into alunos values ('lucas', 'A', 5.0)")
cursor.execute("insert into alunos values ('maria', 'B', 9.5)")
cursor.execute("insert into alunos values ('pedro', 'B', 6.5)")
cursor.execute("insert into alunos values ('julia', 'B', 4.0)")

cursor.execute("select turma, count(*) from alunos group by turma")
print(cursor.fetchall())

cursor.execute("select turma, avg(nota) from alunos group by turma")
print(cursor.fetchall())

cursor.execute("select turma, max(nota) from alunos group by turma")
print(cursor.fetchall())
