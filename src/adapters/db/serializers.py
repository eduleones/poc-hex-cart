import decimal
import pickle  # nosec

import freezegun
import orjson


class BaseSerializer:
    DEFAULT_ENCODING = "utf-8"

    def __init__(self):
        self.encoding = self.DEFAULT_ENCODING

    def dumps(self, value):
        raise NotImplementedError("dumps method must be implemented")

    def loads(self, value):
        raise NotImplementedError("loads method must be implemented")


class JsonSerializer(BaseSerializer):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return str(obj)
        elif isinstance(obj, freezegun.api.FakeDatetime):
            return str(obj)

    def dumps(self, value):
        return orjson.dumps(value, default=self.default)

    def loads(self, value):
        if value is None:
            return None
        return orjson.loads(value)


class PickleSerializer(BaseSerializer):  # nosec
    DEFAULT_ENCODING: str = ""

    def dumps(self, value):
        return pickle.dumps(value)

    def loads(self, value):
        if value is None:
            return None
        return pickle.loads(value)
