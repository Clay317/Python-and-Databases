import jaydebeapi
import pandas as pd
import json

%matplotlib inline

def read_jdbc(sql, jclassname, driver_args, jars=None, libs=None):
  try:
    conn = jaydebeapi.connect(jclassname=jclassname, url=driver_args, jars=jars, libs=libs)
    
  except jaybeapi.DatabaseError as de:
    raise
    
  try:
    curs = conn.cursor()
    curs.execute(sql)
    
    columns = [desc[0] for desc in curs.description] #getting column headers
    
    return pd.DataFrame(curs.fetchall(), columns=columns)
    
  except jaybeapi.DatabaseError as de:
    raise
    
  finally:
    curs.close()
    conn.close()
    
connection_string = "jdbc:<type and server>:user=<username>; password=" + open('<path to private folder>', "r").readline().strip + ";;"
class_name = "<driver name>"
jars = "<path to jar file>"

sql_query = (select * from tbl_name")

df = read_jdbc(sql=sql_query, jclassname=class_name, driver_args=connection_string, jars=jars)
