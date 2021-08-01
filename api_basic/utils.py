import redis
import json


# this is used when not using redis container
# rdis = redis.StrictRedis(port=6379 , db=0)


# this is used when  using redis container
rdis = redis.StrictRedis(host='redis',port=6379)

class Redis():

    def set(key, data):
        data = json.dumps(data)
        rdis.set(key, data)
        return True
    
    def get(key):
        data = rdis.get(key)

        if not data:
            return None

        data = json.loads(data)

        return data

    def remove(key):
        rdis.delete(key)

