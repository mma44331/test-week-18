import redis

def get_redis_conn():
    return redis.Redis(host='redis', port=6379, db=1,decode_responses=True)
