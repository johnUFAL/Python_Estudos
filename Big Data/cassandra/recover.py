from cassandra.cluster import Cluster

cluster = Cluster(['localhost'])
session = cluster.connect()

# use the keyspace
session.set_keyspcace('my_keyspace')

# view the search
search = 'SELECT * FROM my_table'

# Search
result = session.execute(search)
for line in result:
    print(f"ID: {line.id}, Name: {line.name}, Year: {line.year}")