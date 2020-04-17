import pyodbc
import pandas as pd

#connect to database
con = pyodbc.connect("DSN=<database>",UID='<username>', pwd='password'>)

sql = """select * from tbl_name"""

#load query results into a dataframe
data = pd.read_sql_query(sql, con)

#write output to folder
data.to_csv('<output path and file name>', index=False, header=False)
