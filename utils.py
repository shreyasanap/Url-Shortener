import validators 
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker
import psycopg2

con=psycopg2.connect(database="urlshortener",
                     user="postgres",
                     password="123",
                     host="localhost",
                     port='5432'
                     )
cursor_obj=con.cursor()

def valid_url(url):
  return validators.url(url) is True

def name_available(name):
  cursor_obj.execute("select short_name from url_info where short_name =%s",(name,))
  result=cursor_obj.fetchone()
  return result

def add_url(name, url):
  cursor_obj.execute("insert into url_info (short_name, url) values(%s, %s)", (name, url))
  con.commit()

def get_url(short_name):
  cursor_obj.execute("select * from url_info where short_name = %s", (short_name,))
  result=cursor_obj.fetchone()
  return result
