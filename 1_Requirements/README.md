# Requirements

## Introduction

During the 1990's, Music piracy was a big issue and a lot of people were sued heavily because of it. With the introduction of music streaming platforms, Regulating the piracy have been achieved. Record label companies can distribute the music albums without any worry of their revenue. Also, the consumer can hear the songs for free with ads or get a premium account for lesser price. Streaming works by sending information from a server to an individual player. The actual song exists on the server as a raw file. They are then compressed in order to travel over the internet instantaneously.

## Research

### Cost and Features:-

| Time | Features                                                                                                                                                                                                                                 | Cost                                                                                                                           |
| ---- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| 1993 | Internet Underground Music Archive launched as the first free online music archive of MP3 downloadable songs. Unsigned singers can use this platform to communicate with audience and distrbute their songs while avoiding record labels | Music distribution was free of cost                                                                                            |
| 1999 | A peer-to-peer music sharing website called Napster was introduced among American college students. They were able to download albums as well as hear to rare live version and laternative cuts                                          | Downloading music was free of cost and was considered illegal                                                                  |
| 2003 | Apple launched the iTunes Store, an online music library to be used with their flagship MP3 player (IPod),                                                                                                                               | Users were able to download a full catalogue of music for the mere price of $0.99 per song                                     |
| 2005 | Introduction to Pandora,, Pandora created an online service which recommended new music based on a user’s listening history, allowing users to bookmark artists and discover new acts.                                                   | Pandora introduced "freemium model" where users can listen for free with ads or pay $10 per month for uninterrupted streaming. |
| 2007 | Soundcloud launched as an online audio distribution platform that allows musicians to distribute their tracks for free.                                                                                                                  | Music distribution was free of cost                                                                                            |
| 2008 | Spotify was launched to tackle the issues of music piracy, offering a seemingly infinite, catalog of music for audiences to listen to.                                                                                                   | Driving revenue was from advertisements played of free version and Spotify premium subscription fees                           |

## SWOT Analysis

![Swot Analysis](/1_Requirements/SWOTanalysis.png)

## 4W&#39;s and 1&#39;H

### Who:-

- Users of any age group can use this program.

### What:-

- A music streaming platform were users can login and hear to their favourite tracks.

### When:-

- People use music streaming platforms every day like Spotify, Saavn etc.

### Where:-

- Anyone can access these platforms anywhere in the world.

### How:-

- Users are asked to login or signup. After they have logged in, they can stream to their favourite tracks by browsing or searching through the platform

## Detail requirements

### High Level Requirements:-

| ID   | Description                             | Category  | Status |
| ---- | --------------------------------------- | --------- | ------ |
| HR01 | User shall view the menu screen         | Technical |        |
| HR02 | User shall navigate using choices       | Scenario  |        |
| HR03 | User shall hear the song                | Scenario  |        |
| HR04 | User shall search for the song          | Technical |        |
| HR05 | User shall login/signup                 | Technical |        |
| HR06 | User shall browse through the song list | Technical |        |
| HR07 | Data should be stored in the database   | Scenario  |        |
| HR08 | User shall see last played song         | Technical |        |

### Low level Requirements:-

| ID   | Description                                                                            | HLR ID | Status (Implemented/Future) |
| ---- | -------------------------------------------------------------------------------------- | ------ | --------------------------- |
| LR01 | In the sign up , username and password can be entered to create account                | HR05   |                             |
| LR02 | The password is processed using hashing technique and returned                         | HR05   |                             |
| LR03 | The username and password are stored in the database for further use                   | HR05   |                             |
| LR04 | In login page, username and password are entered and authenticated using database      | HR05   |                             |
| LR05 | If the user is invalid, expection is thrown                                            | HR05   |                             |
| LR06 | The streaming menu screen is displayed with search browse and last played option       | HR01   |                             |
| LR07 | In search, keyword is entered and checked for valid results                            | HR04   |                             |
| LR08 | If the program can't find the song, expection is thrown                                | HR04   |                             |
| LR09 | If the program finds the song, valid results is displayed and user can select the song | HR04   |                             |
| LR10 | In browse, the list of music tracks is displayed                                       | HR06   |                             |
| LR12 | The user can choose the song from the browse list                                      | HR06   |                             |
| LR13 | In last played option, the user is able to see what sing was last played by the user   | HR08   |                             |
| LR14 | Database is updated with last played song everytime the user listens to the song       | HR08   |                             |
