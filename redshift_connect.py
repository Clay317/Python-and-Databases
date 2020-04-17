import psycopg2

#Obtaining the connection to RedShift
con=psycopg2.connect(dbname= '<dbname>', host= '<get from RedShift>', port= '5439', user= 'user name', password= 'password')

#Opening a cursor and running a query 
cur = con.cursor()
cur.execute("select * from tbl_name")

#Printing the output
print(cur.fetchall())

cur.close()

#commit stored proc
#con.commit()
con.close()
