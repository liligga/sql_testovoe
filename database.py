import sqlite3


class Database:
    def __init__(self, db_file):
        self.db_file = db_file

    def create_tables(self):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute("DROP TABLE IF EXISTS brandList;")
            cursor.execute("DROP TABLE IF EXISTS categoryList;")
            cursor.execute("DROP TABLE IF EXISTS goodsList;")
            cursor.execute("DROP TABLE IF EXISTS storeList;")
            cursor.execute("DROP TABLE IF EXISTS contractorList;")
            cursor.execute("DROP TABLE IF EXISTS actionTable;")
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS brandList (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(255)
            );
            """)
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS categoryList (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(255)
            );
            """)
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS goodsList (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(255),
                category_id INTEGER, 
                brand_id INTEGER, 
                FOREIGN KEY (category_id) REFERENCES categoryList(id),
                FOREIGN KEY (brand_id) REFERENCES brandList(id)
            );
            """)
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS storeList (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(255)
            );
            """)
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS contractorList (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(255)
            );
            """)
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS actionTable (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                store_from_id INTEGER, 
                store_to_id INTEGER, 
                contractor_from_id INTEGER, 
                contractor_to_id INTEGER, 
                good_id INTEGER,
                qty INTEGER NOT NULL CHECK (qty > 0),
                action_date DATE,
                FOREIGN KEY (store_from_id) REFERENCES categoryList(id),
                FOREIGN KEY (store_to_id) REFERENCES brandList(id),
                FOREIGN KEY (contractor_from_id) REFERENCES categoryList(id),
                FOREIGN KEY (contractor_to_id) REFERENCES brandList(id)
                FOREIGN KEY (good_id) REFERENCES goodsList(id)
            );
            """)
            conn.commit()

    def insert_data(self):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute("""
            INSERT INTO brandList (name) VALUES ('Бренд 1'), ('Бренд 2'), ('Бренд 3'), ('Бренд 4'), ('Бренд 5');
            """)
            cursor.execute("""
            INSERT INTO categoryList (name) VALUES ('кросы'), ('Футболки'), ('Шорты'), ('Поло'), ('Джинсы');
            """)
            cursor.execute("""
            INSERT INTO goodsList (name, category_id, brand_id) VALUES 
            ('Удобные кроссы', 1, 1), 
            ('Оранжевые кроссы', 1, 2), 
            ('Пёстрая футболка', 2, 2), 
            ('Белая футболка', 2, 3),
            ('Футболка хаки', 2, 4), 
            ('Обтягивающая футболка', 2, 2), 
            ('Юнисекс футболка', 2, 3), 
            ('Обтягивающие джинсы', 5, 5),
            ('Белые джинсы', 5, 1), 
            ('Голубые джинсы', 5, 2),
            ('Женские шорты', 3, 1), 
            ('Мужские шорты', 3, 2), 
            ('Женские поло', 4, 4), 
            ('Мужские поло', 4, 5);
            """)
            cursor.execute("""
            INSERT INTO storeList (name) VALUES ('Магазин 1'), ('Магазин 2'), ('Магазин 3');
            """)
            cursor.execute("""
            INSERT INTO contractorList (name) VALUES ('Поставщик 1'), ('Поставщик 2'), ('Поставщик 3'), ('Поставщик 4');
            """)
            cursor.execute("""
            INSERT INTO actionTable (store_from_id, store_to_id, contractor_from_id, contractor_to_id, good_id, qty, action_date) VALUES
            (1, 2, NULL, NULL, 1, 10, '2023-01-01'),
            (3, 1, NULL, NULL, 1, 17, '2023-01-05'),
            (2, 3, NULL, NULL, 2, 13, '2023-01-12'),
            (1, 2, NULL, NULL, 2, 23, '2023-02-12'),
            (3, 1, NULL, NULL, 2, 5, '2023-02-14'),
            (3, 1, NULL, NULL, 3, 5, '2023-01-06'),
            (3, 2, NULL, NULL, 3, 33, '2023-03-19'),
            (1, 2, NULL, NULL, 4, 8, '2023-01-23'),
            (1, 3, NULL, NULL, 4, 18, '2023-05-09'),
            (1, 2, NULL, NULL, 4, 21, '2023-03-16'),
            (2, 1, NULL, NULL, 5, 42, '2023-02-01'),
            (2, 1, NULL, NULL, 5, 12, '2023-01-11'),
            (2, 3, NULL, NULL, 5, 10, '2023-02-23'),
            (3, 1, NULL, NULL, 6, 7, '2023-02-05'),
            (3, 1, NULL, NULL, 6, 23, '2023-01-12'),
            (3, 2, NULL, NULL, 6, 29, '2023-03-22'),
            (1, 2, NULL, NULL, 7, 9, '2023-02-10'),
            (2, 3, NULL, NULL, 8, 11, '2023-02-11'),
            (3, 1, NULL, NULL, 9, 6, '2023-02-13'),
            (1, 2, NULL, NULL, 10, 14, '2023-03-21'),
            (2, 3, NULL, NULL, 11, 15, '2023-03-27'),
            (2, 1, NULL, NULL, 11, 1, '2023-01-27'),
            (2, 1, NULL, NULL, 11, 33, '2023-04-27'),
            (3, 1, NULL, NULL, 12, 16, '2023-04-06'),
            (3, 2, NULL, NULL, 12, 22, '2023-01-12'),
            (3, 1, NULL, NULL, 12, 44, '2023-02-13'),
            (1, 3, NULL, NULL, 13, 17, '2023-04-18'),
            (1, 3, NULL, NULL, 13, 22, '2023-02-28'),
            (1, 2, NULL, NULL, 13, 14, '2023-03-03'),
            (1, 3, NULL, NULL, 13, 5, '2023-05-11'),
            (2, 3, NULL, NULL, 14, 18, '2023-05-04'),
            (NULL, 1, 1, NULL, 1, 12, '2023-02-10'),
            (NULL, 4, 1, NULL, 2, 5, '2023-02-10'),
            (NULL, 2, 3, NULL, 2, 4, '2023-02-13'),
            (NULL, 1, 1, NULL, 3, 19, '2023-02-21'),
            (NULL, 2, 3, NULL, 3, 7, '2023-04-01'),
            (NULL, 1, 4, NULL, 4, 11, '2023-04-02'),
            (NULL, 1, 3, NULL, 4, 22, '2023-04-11'),
            (NULL, 2, 1, NULL, 5, 9, '2023-04-14'),
            (NULL, 1, 1, NULL, 6, 15, '2023-04-24'),
            (NULL, 4, 3, NULL, 6, 12, '2023-02-13'),
            (NULL, 1, 4, NULL, 7, 8, '2023-05-02'),
            (NULL, 1, 1, NULL, 8, 13, '2023-05-11'),
            (NULL, 2, 3, NULL, 9, 14, '2023-05-13'),
            (NULL, 1, 4, NULL, 10, 17, '2023-05-14'),
            (NULL, 2, 1, NULL, 11, 18, '2023-05-18');
            """)
