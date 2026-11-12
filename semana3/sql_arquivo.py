import sqlite3

conexao = sqlite3.connect("alunos.db")
cursor = conexao.cursor()

cursor.execute("drop table if exists alunos")

cursor.execute("create table if not exists alunos (nome text, nota real)")
cursor.execute("insert into alunos values ('ana', 8.5)")
cursor.execute("insert into alunos values ('lucas', 5.0)")

cursor.execute("update alunos set nota = 6.0 where nome = 'lucas'")
cursor.execute("delete from alunos where nome = 'ana'")

conexao.commit()

cursor.execute("select * from alunos")
print(cursor.fetchall())
