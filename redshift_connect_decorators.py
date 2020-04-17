def redshiftconnect(func):
  import psycopg2

  #Obtaining the connection to RedShift
  con=psycopg2.connect(dbname= '<dbname>', host= '<get from RedShift>', port= '5439', user= 'user name', password= 'password')

  #Opening a cursor and running a query 
  cur = con.cursor()
  
  #Running associated function's specific action
  func()
  
  cur.close()
  con.close()
  
@redshiftconnect
def do_sql(sql):
  cur.execute(sql)
  print(cur.fetchall())
  
@redshiftconnect
def do_sp(sp)
  cur.execute(sp)
  con.commit()
