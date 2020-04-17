from impala.dbapi import connect
from impala util import as_pandas

conn = connect(host='<local host>' port = '10000', use_ssl=True, ca_cert=None, user=None, password=None, kerberos_servie_name='impala')

curs = conn.cursor()

curs.execute('show databases')
curs.fetchall()

curs.execute("""select *
                from tbl_name
                limit 10""")
                              
df
