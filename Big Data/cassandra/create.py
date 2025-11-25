from cassandra.cluster import Cluster

cluster = Cluster(['localhost'])
session = cluster.connect()

# create a keyspace
session.execute("CREATE KEYSPACE IF NOT EXISTS my_keyspace WITH REPLICATION = {'class':'SimpleStrategy', 'replication_factor':1}")

# Using 
session.set_keyspace('my_kayspace')

# Create a table
session.execute("CREATE TABLE IF NOT EXISTS my_table (id UUID PRIMARY KEY, nome TEXT, idade INT)")
