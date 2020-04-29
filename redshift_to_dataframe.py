import psycopg2
import pandas as pd

redshift_endpoint = "<get this from redshift cluster>"
redshift_user = "<username>"
redshift_pass = "<password>"
port = 5439
dbname = 'dev'

from sqlalchemy import create_engine
engine_string = "postgresql+psycopg2://%s:%s@%s:%d/%s" % (redshift_user, redshift_pass, redshift_endpoint, port, dbname)
engine = create_engine(engine_string)

sql = ("SELECT * FROM business_event")

df = pd.read_sql(sql, engine)

df.head() 
