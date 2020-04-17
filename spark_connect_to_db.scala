#Note: JDBC loading and saving can be achieved via either the load/save or jdbc methods
#Loading data from a JDBC source
jdbcDF = spark.read \ 
  .fprmat("jdbc") \
  .option("url", "jdbc:postgressql:dbserver") \
  .option("dbtable", "schema.tablename") \
  .option("user", "username") \
  .option("password"), "password") \
  .load()
  
jdbcDF2 = spark.read \
  .jdbc("jdbc:postgresql:dbserver", "schema.tablename",
    properties={"user": "username", "password": "password"})
