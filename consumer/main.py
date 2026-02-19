import json
from mongo_connection import get_mongo_conn
from datetime import datetime, time
from redis_connection import get_redis_conn

r = get_redis_conn()
conn = get_mongo_conn()

while True:
    result = r.brpop(['urgent_queue', 'normal_queue'], timeout=0)
    if result:
        queue_name, raw_data = result

        try:
            message = json.loads(raw_data)
            message['insertion_time'] = datetime.now()
            print(message)
            conn.insert_one(message)
        except Exception as e:
            print(f"Error processing message: {e}")

