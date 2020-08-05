from smartninja_sql.sqlite import SQLiteDatabase

db = SQLiteDatabase("hiking.sqlite")

db.execute("""CREATE TABLE IF NOT EXISTS User(
                id integer primary key autoincrement, 
                name text, 
                age integer);
            """)

#db.execute("INSERT INTO User(name, age) VALUES ('Matt', 31);")

db.print_tables(verbose=True)

result = db.execute("SELECT * FROM User;")
print(result)

db.pretty_print("SELECT * FROM User;")

db.execute("""
            UPDATE User 
            SET age=22 
            WHERE id=1;
            """)




