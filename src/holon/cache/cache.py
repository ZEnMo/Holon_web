from django.core.cache.backends.db import DatabaseCache
from django.db import connections, router
import pickle
import base64
from django.utils.encoding import force_bytes


class DatabaseCacheExtended(DatabaseCache):
    def get_where(self, query, default=None, version="%") -> dict:
        db = router.db_for_read(self.cache_model_class)
        table = connections[db].ops.quote_name(self._table)

        with connections[db].cursor() as cursor:
            cursor.execute(
                f"SELECT cache_key, value, expires FROM {table} WHERE cache_key LIKE ':{version}:{query}'"
            )
            rows = cursor.fetchall()
        if len(rows) < 1:
            return {}
        return_d = {}
        for row in rows:
            value = connections[db].ops.process_clob(row[1])
            key = self.__get_key_without_version(row[0])
            return_d[key] = pickle.loads(base64.b64decode(force_bytes(value)))
        return return_d

    def get_all(self, default=None, version=None) -> dict:
        db = router.db_for_read(self.cache_model_class)
        table = connections[db].ops.quote_name(self._table)

        with connections[db].cursor() as cursor:
            cursor.execute(f"SELECT cache_key, value, expires FROM {table}")
            rows = cursor.fetchall()
        if len(rows) < 1:
            return {}
        return_d = {}
        for row in rows:
            value = connections[db].ops.process_clob(row[1])
            key = self.__get_key_without_version(row[0])
            return_d[key] = pickle.loads(base64.b64decode(force_bytes(value)))
        return return_d

    def clear_scenario(self, scenario_id, default=None, version="%") -> None:
        db = router.db_for_read(self.cache_model_class)
        table = connections[db].ops.quote_name(self._table)

        with connections[db].cursor() as cursor:
            cursor.execute(f"delete FROM {table} WHERE cache_key LIKE ':{version}:{scenario_id}_%'")

    def __get_key_without_version(self, key):
        second_colon = key.find(":", key.find(":") + 1)
        return key[second_colon + 1 :]
