import os
import redis
from rq import Worker, Queue, Connection
from engine import run_scan

listen = ['default']
redis_host = os.getenv("REDIS_HOST", "redis")
redis_url = os.getenv('REDIS_URL', f'redis://{redis_host}:6379')
# Use redis host env logic similar to engine/main if needed, but REDIS_URL is standard
conn = redis.from_url(redis_url)
q = Queue(connection=conn)

def queue_scan(target: str, category: str, uid: str) -> str:
    """Enqueue a scan job"""
    job = q.enqueue(
        run_scan,
        args=(target, category, uid),
        job_timeout='1h', # Global job timeout
        result_ttl=86400  # Keep result for 24h
    )
    return job.id

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(list(map(Queue, listen)))
        print("Worker starting... listening on 'default' queue.")
        worker.work()
