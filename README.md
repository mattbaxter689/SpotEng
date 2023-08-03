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

## TO FIX
There seems to be a weird error with spotipy in the docker container. Need to
change this with just using the requests library instead and seeing if that
makes it any better, since I'm getting auth errors. Will need to generate
access token for this

## TODO:
- [ ] implement a class to allow download of data from spotify
- [ ] Add schema for postgres in docker container
- [ ] add docker compose file and set up services
    - add service for db
    - add service for db eng app
- [ ] add commands to makefile
- [ ] add logging to application

## FUTURE WORK:
This is an iterative project that I am looking to expand upon and build more as
time goes on. This is something that I want to put onto a resume and show that
it is being updated when it can

- [ ] build a recommendation engine with python and scikitlearn
- [ ] create a playlist from my recommnded songs based on model
- [ ] starting with something like pandas, look to move to dbt or the like for
  other tools
- [ ] look to expand the project to include other useful tools in industry
