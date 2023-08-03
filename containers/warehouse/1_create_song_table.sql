DROP TABLE IF EXISTS songs.names;
DROP SCHEMA IF EXISTS songs;
CREATE SCHEMA songs;
CREATE TABLE songs.names (
    song_id varchar,
    name varchar
);
