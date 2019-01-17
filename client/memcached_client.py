from pymemcache.client import base

try:
    client = base.Client(('localhost', 11211))

    # set does not return the error even if the key already exists
    client.set('name', 'memcached')
    client.set('use', 'to store data in memory')


    print(client.get('name'))
    print(client.get('use'))

    client.delete('name')
    print(client.get('name'))
    print(client.get('use'))


    # add returns error if key already exists
    client.add('what', 'human')
    print(client.get('what'))

except Exception as exception:
    print(str(exception))
