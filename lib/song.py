from config import CONN, CURSOR

class Song:
    def __init__(self, name, album):
        self.name = name
        self.album = album
    
    @classmethod
    def create_table(self):
        sql = """
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                album TEXT
            )
        """

        CURSOR.execute(sql)


    def save(self):
        sql = "INSERT INTO songs (name, album) VALUES (?, ?)"
        values = (self.name, self.album)
        CURSOR.execute(sql, values)
        CONN.commit()

    # if __name__ == "__main__":
    #  Song.create_table()
    #  song = Song("Hold On", "Born to Sing")
    #  song.save()    
    