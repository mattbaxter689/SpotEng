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
- [ ] add func to artist class to get artist genres
- [ ] change sql migration for new table with track features
- [ ] add new structure for kmeans algorithm. Will involve data prep

## FUTURE IMPLEMENTATION IDEAS:
- [ ] look into possibly saving data initially to csv in S3 bucket? Then
  pulling, transforming and loading to postgres (S3 would be my data lake)
    - make sure that the data has other variables associated (Acousticness etc)
- [ ] Look to incorporate maybe the recently played tracks? Even suggested ones
  by spotify
- [ ] look to possibly incorporate streaming with kafka. Ie: take data from S3
  data lake as csv or parquet, and stream each row or rows to a consumer that
  saves to postgres
