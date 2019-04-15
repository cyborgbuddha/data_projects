```
   ____              __    _ ___     ___  ___ 
  / __/__  ___ _____/ /__ (_) _/_ __/ _ \/ _ )
 _\ \/ _ \/ _ `/ __/  '_// / _/ // / // / _  |
/___/ .__/\_,_/_/ /_/\_\/_/_/ \_, /____/____/ 
   /_/                       /___/            
```

__SparkifyDB__ is a __Relational Database Management System__ designed to convert raw user and event logs from the Sparkify music streaming app into a series of tables optimized for analysts to query. 

The raw data is outputted in json dictionaries 



## Star Schema

### Fact Table
#### songplays 
- records in log data associated with song plays i.e. records with page "NextSong"
    songplay_id, 
    start_time, 
    user_id, 
    level, 
    song_id, 
    artist_id, 
    session_id, 
    location, 
    user_agent

### Dimension Tables
#### d_users  
- users in the app
    user_id, 
    first_name, 
    last_name, 
    gender, 
    level

#### d_songs 
- songs in music database
    song_id, 
    title, 
    artist_id, 
    year, 
    duration

#### d_artists 
- artists in music database
    artist_id, 
    name, 
    location, 
    lattitude, 
    longitude

#### d_time 
- timestamps of records in songplays broken down into specific units
    start_time, 
    hour, 
    day, 
    week, 
    month, 
    year, 
    weekday

