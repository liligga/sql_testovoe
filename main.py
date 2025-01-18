from database import Database


def main():
    db = Database("db.sqlite3")
    db.create_tables()
    db.insert_data()


if __name__ == "__main__":
    main()
