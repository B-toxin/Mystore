import sqlite3
import os


def populate_database(folder_path):
    conn = sqlite3.connect('file_database.db')
    c = conn.cursor()

    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            c.execute('INSERT INTO files (filename) VALUES (?)', (filename,))

    conn.commit()
    conn.close()


if __name__ == "__main__":
    folder_path = "static/files"  # Relative path to the folder
    populate_database(folder_path)
    print("File names added to the database.")
