```
   ____              __    _ ___     ___  ___ 
  / __/__  ___ _____/ /__ (_) _/_ __/ _ \/ _ )
 _\ \/ _ \/ _ `/ __/  '_// / _/ // / // / _  |
/___/ .__/\_,_/_/ /_/\_\/_/_/ \_, /____/____/ 
   /_/                       /___/            
```

__SparkifyDB__ is a __Relational Database Management System__ designed to convert raw user and event logs from the Sparkify music streaming app into a series of tables optimized for analysts to query.

The raw data is stored in two json dictionary folders. _song_data_ and _log_data_ are the file names sitting in the __data/__ directory.

The logs are converted into a __Star Schema__ using __Python__ and __PostgreSQL__. 

# Table of contents
1. [Star Schema](#starschema)
    1. [Fact Table - songplays](#songplays)
2. [Dimension Tables](#dimtables)
    1. [d_users](#d_users)
    2. [d_songs](#d_songs)
    3. [d_artists](#d_artists)
    4. [d_time](#d_time)


## Star Schema <a name="starschema"></a>

![SparkifyDBStarSchema](https://github.com/cyborgbuddha/data_projects/SparkifyDB%20RDBMS/SparkifyDB.png "SparkifyDBERD")


### Fact Table
## songplays 
_records in log data associated with song plays i.e. records with page "NextSong"_

|Column|Description|Notes|
|------|-----------|-----|
|`songplay_id`| ID assignd to each song played | Primary Key |
|`start_time`| Time that user played song | Surrogate Key |
|`user_id`| Joins on d_user | Surrogate Key |
|`level`| User's subscription status ||
|`song_id`| Joins on d_songs | Surrogate Key |
|`artist_id`| Joins on d_artist | Surrogate Key |
|`session_id`| ID relating to users song play session | Surrogate Key |
|`location`| Location of user during song play record | |
|`user_agent`| User's device information | |

### Dimension Tables <a name="dimtables"></a>
## d_users   <a name="d_users_"></a>
_users in the app_

|Column|Description|Notes|
|------|-----------|-----|
|`user_id`| ID relating to user | Primary Key |
|`first_name`| First name of user | Can be overwritten if user changes in profile |
|`last_name`| Last name of user | Can be overwritten if user changes in profile |
|`gender`| Gender of user | Can be overwritten if user changes in profile |
|`level`| User's subscription status | Can be overwritten if user changes upgrades or downgrades |

## d_songs <a name="d_songs"></a>
_songs in music database_

|Column|Description|Notes|
|------|-----------|-----|
|`song_id`| ID relating to song | Primary Key |
|`title`| Title of song | Immutable |
|`artist_id`| Joinable key on d_artists | Surrogate Key |
|`year`| Year of song release | Immutable |
|`duration`| Duration of song | Immutable |

## d_artists <a name="d_artists"></a>
_artists in music database_

|Column|Description|Notes|
|------|-----------|-----|
|`artist_id`| ID relating to artist | Primary Key |
|`name`| Name of Artist | If artist's changes names, create new row |
|`location`| Country and State/Province of artist | Can be overwritten if artist changes affiliated location |
|`lattitude`| Lattitude of artist's location | Can be overwritten if artist changes affiliated location |
|`longitude`| Longitude of artist's location | Can be overwritten if artist changes affiliated location |

## d_time <a name="d_time"></a>
_timestamps of records in songplays broken down into specific units_

|Column|Description|Notes|
|------|-----------|-----|
|`start_time`| Time that song was played by user|Primary Key|
|`hour`| Hour that song was played||
|`day`| Day that song was played||
|`week`| Year week that song was played||
|`month`| Month that song was played||
|`year`| Year that song was played||
|`weekday`| Day of week song was played||