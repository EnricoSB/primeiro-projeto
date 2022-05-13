import pymysql
conexao = pymysql.connect(host='localhost' ,database='bancoteste',user='root', password='1234', port=3306)
from pydantic import BaseModel
class Item(BaseModel):
     id:int
     name:str
     age:int

class Select:

     def select_all(self):
          return 'select * from minhaprimeiraapi'

     def select_name(self,name):
          query=f'select * from minhaprimeiraapi where nome in ("{name}")'
          return query

     def select_id(self,id):
          query=f'select * from minhaprimeiraapi where id in ({id})'
          return query

     def select_age(self,age):
          query=f'select * from minhaprimeiraapi where idade in ({age})'
          return query


#pesquisar
class Search:
     def search_users(self):
          cursor = conexao.cursor()
          select=Select()
          cursor.execute(select.select_all())
          result=[]
          for i in cursor:
               result.append(i)
          cursor.close()
          return result


     def search_name(self,name):
          cursor = conexao.cursor()
          select = Select()
          cursor.execute(select.select_name(name))
          result = []
          for i in cursor:
               result.append(i)
          cursor.close()
          return result


     def search_id(self, id):
          cursor = conexao.cursor()
          select = Select()
          cursor.execute(select.select_id(id))
          result = []
          for i in cursor:
               result.append(i)
          cursor.close()
          return result

     def search_age(self, age):
          cursor = conexao.cursor()
          select = Select()
          cursor.execute(select.select_age(age))
          result = []
          for i in cursor:
               result.append(i)
          cursor.close()
          return result


#inserir
class Insert:

     def insert_into(self,usuario:Item):
          cursor = conexao.cursor()
          query = f'insert into minhaprimeiraapi(id,nome,idade) values({usuario.id},"{usuario.name}",{usuario.age})'
          cursor.execute(query)
          conexao.commit()
          cursor.close()
          return 'O usuario foi adicionado com sucesso'


















#
#      def deletar(self,id):
#           cursor = conexao.cursor()
#           query = f'delete from minhaprimeiraapi where id={id}'
#           cursor.execute(query)
#           conexao.commit()
#           cursor.close()
#           return "deu certo irmão"
#
#
# #adicionar
# def adicionar_usuario(usuario:Item):
#      cursor=conexao.cursor()
#      query = f'insert into minhaprimeiraapi(id,nome,idade) values({usuario.id},"{usuario.nome}",{usuario.idade})'
#      cursor.execute(query)
#      conexao.commit()
#      cursor.close()
#      return "Dados inseridos com sucesso"







#excluir
#atualizar
#solid