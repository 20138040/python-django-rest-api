import redis
import json

rdis = redis.StrictRedis(port=6379 , db=0)

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

