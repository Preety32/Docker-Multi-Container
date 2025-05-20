from flask import Flask
import redis
import os

app = Flask(__name__)
cache = redis.Redis(host=os.environ.get('REDIS_HOST', 'redis'), port=6379)

def get_hit_count():
 retries = 5
 while True:
     try:
         return cache.incr('hits')
     except redis.exceptions.ConnectionError:
         if retries == 0:
             return "Cannot connect to Redis"
         retries -= 1

@app.route('/')
def hello():
 count = get_hit_count()
 return f'Hello Preeti! I have been seen {count} times.\n'

if __name__ == '__main__':
 app.run(host='0.0.0.0')
