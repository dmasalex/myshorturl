import redis


class RedisTools:
    __redis_connect = redis.Redis(host="redis", port=6379)

    @classmethod
    def set_pair(cls, short_url: str, long_url: str):
        cls.__redis_connect.set(short_url, long_url)

    @classmethod
    def get_pair(cls, short_url):
        return cls.__redis_connect.get(short_url)

    @classmethod
    def get_keys(cls):
        return cls.__redis_connect.keys(pattern="*")
