import sqlite3


class Database:
    def __init__(self):
        self.connection = sqlite3.connect("user")
        self.cursor = self.connection.cursor()
        self.create_user()

    def create_user(self):
        self.cursor.execute("""
            create table if not exists user(
                id integer primary key,
                name varchar ,
                age integer ,
                phone_number varchar ,
                address varchar,
                 latitude FLOAT,
                longitude FLOAT)
        """)
        self.connection.commit()

    def add_user(self, name, age, phone_number, address, location):
        self.cursor.execute("""
            insert into user (name, age, phone_number, address, location) values (?, ?, ?, ?, ?)
        """, (name, age, phone_number, address, location))
        self.connection.commit()

    def all_user(self):
        self.cursor.execute(f"""
            SELECT * from user
        """)
        return self.cursor.fetchall()


    def get_user(self, id):
        self.cursor.execute("""
            select * from user where id=?
        """, (id,))
        return self.cursor.fetchone()

    def delete_user(self, id):
        self.cursor.execute("""
            delete from user where id=?
        """, (id,))
        self.connection.commit()




