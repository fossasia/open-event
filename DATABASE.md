# Open-Event Database Model

This document defines the schema used to store the data in the backend. The data could be stored in SQLite db file or just plain json files. This database will be directly modified only by the [orga-server](https://github.com/fossasia/open-event-orga-server). For the [orga-webclient](https://github.com/fossasia/open-event-orga-webclient), the server will provide access to this data over the defined [API](/API.md), to view/modify.  

## Tables
Following are the various tables, and details about their columns.  

### Event
Basic information about the event.    

| Column      | Data Type      | Notes       |
|:------------|:---------------| ------------|
| name        | string         | 
| logo        | string         | url to logo
| timestart   | timestamp      | 
| timeend     | timestamp      |
| loclat      | float          | latitude of location
| loclang     | float          | longitude of location
| locname     | string         | name of event location



### Sessions  
Information about the sessions.  

### Speakers
Information about the speakers.  

| Column          | Data Type      | Notes       |
|:----------------|:---------------| ------------|
| speakerid       | int [autoincr] | primary key, auto increments, unique for each row
| name            | string         |
| photo           | string         | url to photo 
| email           | email id       |
| web             | string         | https://userswebsite.com
| twitter         | string         | only the handle, without http://twitter/ part
| facebook        | string         | only the handle, without http://facebook/ part
| github          | string         | only the handle, without http://github.com/ part
| linkedin        | string         | full link to linkedin profile
| organisation    | string         | 
| position        | string         | title within organisation
| country         | string         |
| sessions        | int-array      | array of session id's where speaker is speaking

### Sponsors
Information about the sponsors.   

| Column      | Data Type      | Notes       |
|:------------|:---------------| ------------|
| name        | string         |
| url         | string         |
| logo        | string         | url to png of logo


### Microlocation
Information about stalls/auditoriums etc inside the event location, so we can generate a microlocation map from it. 
