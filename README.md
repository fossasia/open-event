# Open-Event
The FOSSASIA Open Event Project aims to make it easier for events, conferences, tech summits (maybe more types in future) to easily create Web and Mobile (only Android right now) micro Apps. The project comprises of a data schema for easily storing event details, a server and web frontend that are used to view, modify, update this data easily by the event organisers, a mobile-friendly webapp client to show the event data to attendees, an Android app template which will be used to generate specific apps for each event.   

Each specific component's source code has it's own Github Repo, links provided in the subsections below . This repository is for tracking milestones and issues, and maintaining a wiki about the project. Also, documentation about the JSON Schema, and how to use the template will be hosted on this repo.   

### Open-Event Organiser Server
[Github Repo](https://github.com/fossasia/open-event-orga-server)   
The server which will manage all the data of the event. Backed by a database, it provides API endpoints to fetch the data, and also to modify/update it.    

### Open-Event WebApp
[Github Repo](https://github.com/fossasia/open-event-webapp)   
A mobile-friendly webapp, which shows all information about the event like Sessions, Speakers, Map of location, Sponsors etc. The idea is to make a ready-to-port webapp, that can be wrapped into iOS, Windows, Chrome etc apps - ie. those platforms we are not immediately supporting natively.    

### Open-Event Android App
[Github Repo](https://github.com/fossasia/open-event-android)   
A native Android app template which shows all information about the event like Sessions, Speakers, Map of location, Sponsors etc. Each event needs to make a copy of this template, change only a handful of basic stuff like icon, package name, backend URL, and generate a unique app for their own event. The idea is the create a template from which anyone can generate an app in 10 minutes, without having any knowledge of Android development.    


#### Maintainers
 * Abhishek Batra  
 * Arnav Gupta   
 * Manan Wason     
 * Rafal Kowalski   
This project initially started as part of a GSoC 2015 initiative, under the mentorship of Mario Behling, Duke Leto and others.    
