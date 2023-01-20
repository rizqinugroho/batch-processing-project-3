import psycopg2
import pandas as pds
import pandas.io.sql as sqlio



#connect to potsgresql
try:
  conn = psycopg2.connect("host=localhosts dbname=postgres user=postgres password=1234")
  print("connnection success")
except:
  print("An exception occurred")


#menggunakan cursor

cur = conn.cursor()
cur.execute("Select * from public.employee")

#menampilkan hasil
all = cur.fetchall()
one = cur.fetchone()
conn.commit()


for record in all:
    print(str(record[0]) +"-"+ record[1])
    
data = sqlio.read_sql_query("Select * from public.employee", conn)
# Now data is a pandas dataframe having the results of above query.
data.head()


#print(one);