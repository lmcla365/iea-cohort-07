import os


def get_database_host():
    host = os.getenv("DATABASE_HOST")
    if host is None or host == "":
        return None
    return "mysql://" + host



if __name__ == "__main__":
    print(get_database_host())

