from src.core.db.postgres_connector import get_postgres_connector


def create_parts_table():
    """Создаёт таблицу parts, если она не существует"""
    connector = get_postgres_connector()
    with connector:  # Используем контекстный менеджер для подключения
        with connector.cursor() as cursor:
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS parts (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(255) NOT NULL UNIQUE,
                    description TEXT,
                    price DECIMAL(10, 2) NOT NULL,
                    in_stock INTEGER
                );
                """
            )


def create_suppliers_table():
    """Создаёт таблицу Suppliers, если она не существует"""
    connector = get_postgres_connector()
    with connector:
        with connector.cursor() as cur:
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS suppliers (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(255) NOT NULL UNIQUE,
                    contact TEXT
                );
            """
            )


def create_supplies_table():
    """Создаёт таблицу Supplies, если она не существует"""
    connector = get_postgres_connector()
    with connector:
        with connector.cursor() as cur:
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS supplies (
                    id SERIAL PRIMARY KEY,
                    part_id INTEGER NOT NULL,
                    supplier_id INTEGER NOT NULL,
                    quantity INTEGER NOT NULL,
                    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    CONSTRAINT fk_part FOREIGN KEY (part_id) REFERENCES parts (id),
                    CONSTRAINT fk_supplier FOREIGN KEY (supplier_id) REFERENCES suppliers (id)
                );
            """
            )
