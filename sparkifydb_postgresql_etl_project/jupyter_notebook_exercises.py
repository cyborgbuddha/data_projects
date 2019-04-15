import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *

conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
cur = conn.cursor()

def get_files(filepath):
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))
    
    return all_files

song_files = get_files("/home/workspace/data/song_data/")
print(song_files)

filepath = song_files[0]
print(filepath)

df = pd.read_json(filepath, lines=True)
df.head()

song_data = df[["song_id", "title", "artist_id", "year", "duration"]]
song_data = song_data.values[0].tolist()
print(song_data)

cur.execute(song_table_insert, song_data)
conn.commit()

artist_data = df[["artist_id", "artist_name", "artist_location", "artist_latitude", "artist_longitude"]]
artist_data = artist_data.values[0].tolist()
print(artist_data)

cur.execute(artist_table_insert, artist_data)
conn.commit()

log_files = get_files("/home/workspace/data/log_data/")
print(log_files)

filepath = log_files[0]
print(filepath)

df = pd.read_json(filepath, lines=True)
df.head()

df = df[df["page"] == 'NextSong']
df.head()

df['ts'] = pd.to_datetime(df['ts'], unit='ms')
df.head()

time_data_test = pd.DataFrame({ 'A' : df['ts'],
                    'B' : df['ts'].dt.hour,
                    'C' : df['ts'].dt.day,
                    'D' : df['ts'].dt.weekofyear,
                    'E' : df['ts'].dt.month,
                    'F' : df['ts'].dt.year,
                    'G' : df['ts'].dt.weekday})


column_labels = (
'start_time',
'hour',
'day',
'week',
'month',
'year',
'weekday'
)

time_data_test.head()

for i, row in time_data_test.iterrows():
    cur.execute(time_table_insert, list(row))
    conn.commit()



for index, row in df.iterrows():

    # get songid and artistid from song and artist tables
    cur.execute(song_select, (row.song, row.artist, row.length))
    results = cur.fetchone()
    
    if results:
        songid, artistid = results
    else:
        songid, artistid = None, None
    # insert songplay record
    songplay_data = (row.ts, row.userId, row.level, songid, artistid, row.sessionId, row.location, row.userAgent)
    cur.execute(songplay_table_insert, songplay_data)
    conn.commit()