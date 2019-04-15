# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS fact_songplay;"
user_table_drop = "DROP TABLE IF EXISTS d_user;"
song_table_drop = "DROP TABLE IF EXISTS d_song;"
artist_table_drop = "DROP TABLE IF EXISTS d_artist;"
time_table_drop = "DROP TABLE IF EXISTS d_time;"

# CREATE TABLES

songplay_table_create = (""" 
    CREATE TABLE IF NOT EXISTS fact_songplay (
        songplay_id SERIAL PRIMARY KEY,
        start_time time,
        user_id int,
        level varchar,
        song_id varchar,
        artist_id varchar,
        session_id int,
        location varchar,
        user_agent varchar
    );
""")

user_table_create = ("""
    CREATE TABLE IF NOT EXISTS d_user (
        user_id int PRIMARY KEY,
        first_name varchar NOT NULL,
        last_name varchar NOT NULL,
        gender varchar NOT NULL,
        level varchar NOT NULL
    );
""")

song_table_create = ("""
    CREATE TABLE IF NOT EXISTS d_song (
        song_id varchar PRIMARY KEY,
        title varchar NOT NULL,
        artist_id varchar NOT NULL,
        year int NOT NULL,
        duration numeric(10,5) NOT NULL
    );
""")

artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS d_artist (
        artist_id varchar PRIMARY KEY,
        name varchar NOT NULL,
        location varchar NOT NULL,
        lattitude float NOT NULL,
        longitude float NOT NULL
    );
""")

time_table_create = ("""
    CREATE TABLE IF NOT EXISTS d_time (
        start_time timestamp PRIMARY KEY, 
        hour int NOT NULL,
        day int NOT NULL,
        week int NOT NULL,
        month int NOT NULL,
        year int NOT NULL,
        weekday int NOT NULL
    );
""")

# INSERT RECORDS

songplay_table_insert = ("""
    INSERT INTO fact_songplay (
        start_time,
        user_id,
        level,
        song_id,
        artist_id,
        session_id,
        location,
        user_agent
    ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
""")

user_table_insert = ("""
    INSERT INTO d_user (
        user_id,
        first_name,
        last_name,
        gender,
        level
    ) VALUES (%s,%s,%s,%s,%s)
    ON CONFLICT (user_id) 
    DO NOTHING;
""")

song_table_insert = ("""
    INSERT INTO d_song (
        song_id,
        title,
        artist_id,
        year,
        duration
    ) VALUES (%s,%s,%s,%s,%s);
""")

artist_table_insert = ("""
    INSERT INTO d_artist (
        artist_id, 
        name, 
        location, 
        lattitude, 
        longitude
    ) VALUES (%s,%s,%s,%s,%s);
""")


time_table_insert = ("""
    INSERT INTO d_time (
        start_time, 
        hour,
        day,
        week,
        month,
        year,
        weekday
    ) VALUES (%s,%s,%s,%s,%s,%s,%s);
""")

song_select = ("""
    SELECT
        d_song.song_id,
        d_artist.artist_id
    FROM d_song JOIN d_artist on d_song.artist_id = d_artist.artist_id
    WHERE d_song.title = (%s) and d_artist.name = (%s) and d_song.duration = (%s);
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]