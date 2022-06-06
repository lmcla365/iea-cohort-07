import os


def get_database_host():
    host = os.getenv("DATABASE_HOST")
    if not host:
        return None
    return f"mysql://{host}"



if __name__ == "__main__":
    print(get_database_host())

