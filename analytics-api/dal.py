import json

from redis_connection import get_redis_conn
from mongo_connection import get_mongo_conn



r = get_redis_conn()
conn = get_mongo_conn()

def get_alerts_by_border_and_priority():
    cache_key = "analytics:alerts_by_border"

    cached_data = r.get(cache_key)
    if cached_data:
        print("Returning data from Redis Cache")
        return json.loads(cached_data)

    pipeline = [
        {
            "$group": {
                "_id": {
                    "border": "$border",
                    "priority": "$priority"
                },
                "count": {"$sum": 1}
            }
        },
        {
            "$project": {
                "_id": 0,
                "border": "$_id.border",
                "priority": "$_id.priority",
                "count": 1
            }
        }
    ]

    results = list(conn.aggregate(pipeline))

    r.set(cache_key, json.dumps(results), ex=600)

    return results



def get_top_urgent_zones():
    cache_key = "analytics:top_urgent_zones"
    cached_data = r.get(cache_key)

    if cached_data:
        return json.loads(cached_data)

    r.set(cache_key, json.dumps(data, default=str), ex=300)


def get_distance_distribution():
    cache_key = "analytics:distance_distribution"
    cached_data = r.get(cache_key)

    if cached_data:
        return json.loads(cached_data)

    r.set(cache_key, json.dumps(data, default=str), ex=300)


def get_low_visibility_high_activity():
    cache_key = "analytics:low_visibility_high_activity"
    cached_data = r.get(cache_key)

    if cached_data:
        return json.loads(cached_data)

    r.set(cache_key, json.dumps(data, default=str), ex=300)


def get_hot_zones():
    cache_key = "analytics:hot_zones"
    cached_data = r.get(cache_key)

    if cached_data:
        return json.loads(cached_data)

    r.set(cache_key, json.dumps(data, default=str), ex=300)
