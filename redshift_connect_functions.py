def do_sql(sql):
  import psycopg2

  #Obtaining the connection to RedShift
  con=psycopg2.connect(dbname= '<dbname>', host= '<get from RedShift>', port= '5439', user= 'user name', password= 'password')

  #Opening a cursor and running a query 
  cur = con.cursor()
  cur.execute(sql)
  #Printing the output
  print(cur.fetchall())
  cur.close()
  con.close()
  
def do_sp(storedproc):
  import psycopg2

  #Obtaining the connection to RedShift
  con=psycopg2.connect(dbname= '<dbname>', host= '<get from RedShift>', port= '5439', user= 'user name', password= 'password')

  #Opening a cursor and running a query 
  cur = con.cursor()
  cur.execute(storedproc)
  cur.close()
  #Committing the stored proc
  con.commit()
  con.close()
