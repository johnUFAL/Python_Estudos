from cassandra.cluster import Cluster
from uuid import uuid4

cluster = Cluster(['localhost'])
session = cluster.connect()

session.set_keyspace('my_keyspace')

# data for inserting
id = uuid4()
name = 'João'
year = 24

# Insert in table
session.execute("INSERT INTO my_table (id, name, year) VALUES (%s, %s, %s)", (id, name, year))

