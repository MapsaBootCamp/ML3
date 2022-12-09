from typing import Dict, List, Any, Tuple, Union
import psycopg2


# CREATE TABLE table_name()
# DROP TABLE, TRUNCATE TABLE
# INSERT INTO table_name(col1, col2, ....) VALUES (val1, val2)
# ALTER TABLE      <------- change schema


class DBManipulation:

    def __init__(self) -> None:
        self._connect_db()

    def _connect_db(self):
        # Connect to your postgres DB
        self.conn = psycopg2.connect(
            host="localhost",
            database="ml",
            user="mapsa",
            password="mapsa1234")

        self.cur = self.conn.cursor()

    def create_table(self, table_name, schema):
        self.cur.execute(f"DROP TABLE IF EXISTS {table_name} cascade")
        self.cur.execute(f"CREATE TABLE {table_name}({schema})")
        self.conn.commit()

    def bulk_insert_data(self, table_name, values: List[Dict]):
        if not isinstance(values, list):
            raise Exception("data should be list")
        self._insert_data(table_name, values)

    def insert_data(self, table_name, data):
        self._insert_data(table_name, [data])

    def _insert_data(self, table_name, data_list: List[Dict]):
        keys = []
        values = []
        query_values = "("
        for key, val in data_list[0].items():
            keys.append(key)
            query_values += "%s, "

        for data in data_list:
            values.append(tuple(data.values()))

        keys = ", ".join(keys)
        query_values = query_values[:-2]
        query_values += ")"
        print(query_values)
        print(values)
        self.cur.executemany(f"""
                INSERT INTO {table_name}(
                    {keys}
                )VALUES {query_values}
            """, values)
        self.conn.commit()

    def get_all_data(self, table_name):
        pass

    def __del__(self):
        if self.conn:
            self.conn.close()
