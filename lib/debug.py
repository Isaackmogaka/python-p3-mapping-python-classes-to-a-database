#!/usr/bin/env python3

from config import CONN, CURSOR
from song import Song


if __name__ == '__main__':
   Song.create_table()
   song = Song("Hold On", "Born to Sing")
   song.save()
   
table_info = CURSOR.execute("PRAGMA table_info(songs)").fetchall()
for column in table_info:
        print(column)   
