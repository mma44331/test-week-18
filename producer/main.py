import json
from priority_logic import determining_urgency
from redis_connection import get_redis_conn
from dotenv import load_dotenv

load_dotenv()

with open('../data/border_alerts.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

r = get_redis_conn()


# r.flushdb()

for warning in data:
    alert_analyzed = determining_urgency(warning)

    if alert_analyzed['priority'] == 'NORMAL':
        r.lpush('normal_queue', json.dumps(alert_analyzed))
    else:
        r.lpush('urgent_queue', json.dumps(alert_analyzed))





