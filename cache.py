import redis
import json

# create  a new redis client
redis_client = redis.Redis(host="localhost", port=6379, db=0)

username = redis_client.get("username")
print(username)

redis_client.set("microsoft_fundamental_data", json.dumps({"pe": 33}))
print(redis_client.get("microsoft_fundamental_data"))
