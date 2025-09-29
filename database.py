import sqlite3

class Data:
    def __init__(self) -> None:
        self.con = sqlite3.connect("database.db",check_same_thread=False)
        self.cur = self.con.cursor()
        self._init_db()

    def _init_db(self):
        self._query("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY ,name TEXT)")
    
    def _query(self,query):
        return self.cur.execute(query)
        

    def add_user(self,username):
        q = f"INSERT INTO users(name) VALUES('{username}');"
        print(q)
        self._query(q)
        self.con.commit()

    def get_users(self):
        q = f"SELECT * FROM users;"
        users = []
        for id,username in self._query(q).fetchall():
            users.append({'id':id, 'username':username})
        return users

data = Data()
# data.add_user('Fidel')
# data.add_user('Marie')
# data.add_user('Jeanne')
# data.add_user('Paul')
# data.add_user('Marc')
# print(data.get_users())