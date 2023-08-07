# The Purpose
This project is meant to serve as a data engineering project using some of the
relevant tools found in industry. For now it is something simple, however, as
time progresses, I will try and expand on this project as much as I can with the
limited time I have with my thesis

# What is the project?
This project makes use of the spotify API to extract various data from my
personal listenings. As I said, this will start of simply as is, with future
plans to implement further and incorporate other things as I see fit. For now,
this extracts spotify data, and stores the necessary items in a postgres
database running in a docker container. 

From there I can add the necessary transformations to data that I choose to.

## TODO:
- [ ] Make sure data is uploading properly to postgres
- [ ] look into possibly saving data initially to csv in S3 bucket? Then
  pulling, transforming and loading to postgres (this would be my data lake)
- [ ] Look to incorporate maybe the recently played tracks
    - can extend this further by streaming with kafka?

## COMPLETED:
- [x] implement a class to allow download of data from spotify
- [x] Add schema for postgres in docker container
- [x] add docker compose file and set up services
    - add service for db
    - add service for db eng app
- [x] add commands to makefile
