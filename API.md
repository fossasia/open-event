# Open-Event API Endpoint Documentation

## Endpoints
All the GET endpoints are suffix to the domain where we will set up the [organiser server](https://github.com/fossasia/open-event-orga-server)   

### Event
` GET /get/v1/event.json `  


Example response - 
```javascript
{
  "event": {
    "name": "OpenEvent",
    "logo": "http://openevent.org/logo.png",
    "timestart": "2015-05-08T16:44:36.150Z",
    "timeend": "2015-05-08T16:44:36.150Z",
    "loclat": "75.12315",
    "loclang": "123.22312",
    "locname": "Eventsarena Auditorium"
  }
}
```


### Sessions
` GET /get/v1/sessions.json ` 

Example response -    
```javascript
{
  "sessions": [
    {
      "id": 2,
      "title": "Open-Event",
      "subtitle": "Creating a generic event app template",
      "abstract": "Some random abstract goes here",
      "description": "Some random desc goes here",
      "timestart": "2015-05-11T22:12:41.201Z",
      "timeend": "2015-05-11T22:12:41.201Z",
      "type": "talk",
      "track": {
        "id": 1,
        "name": "Android"
      },
      "speakers": [
        {
          "id": 3,
          "name": "John Smith"
        },
        {
          "id": 5,
          "name": "Jane Doe"
        }
      ],
      "level": "advanced",
      "microlocation": {
        "id": 4,
        "name": "Hall 4"
      }
    },
    {
      "id": 3,
      "title": "Open-Event-Server",
      "subtitle": "Creating an event management Dashboard",
      "abstract": "Some random abstract goes here",
      "description": "Some random desc goes here",
      "timestart": "2015-05-11T22:12:41.205Z",
      "timeend": "2015-05-11T22:12:41.206Z",
      "type": "discussion",
      "track": {
        "id": 1,
        "name": "Python"
      },
      "speakers": [
        {
          "id": 3,
          "name": "Harry Potter"
        },
        {
          "id": 5,
          "name": "Jack Daniels"
        }
      ],
      "level": "intermediate",
      "microlocation": {
        "id": 2,
        "name": "Stage 2"
      }
    }
  ]
}
```

### Tracks 
` GET /get/v1/tracks.json `

Example response -   
```javascript
{
  "tracks": [
    {
      "id": 1,
      "name": "Linux",
      "description": "All things to talk about Linux"
    },
    {
      "id": 2,
      "name": "Android",
      "description": "All things to talk about Android"
    },
    {
      "id": 3,
      "name": "Java",
      "description": "All things to talk about Java"
    }
  ]
}
```

### Speakers
` GET /get/v1/speakers.json ` 

### Sponsors
` GET /get/v1/sponsors.json ` 

Example response  - 
```javascript
{
  "sponsors": [
    {
      "name": "Google",
      "url": "http://google.com",
      "logo": "http://google.com/logo.png"
    },
    {
      "name": "RedHat",
      "url": "http://redhat.org",
      "logo": "http://redhat.org/logo.png"
    }
  ]
}
```

### Microlocation
` GET /get/v1/microlocations.json `  

Example Response -  
```javascript
{
  "microlocations": [
    {
      "id": 0,
      "name": "Stage 7",
      "latitude": "75.12312",
      "longitude": "123.11212",
      "floor": 2
    },
    {
      "id": 1,
      "name": "Hall 3",
      "latitude": "75.12312",
      "longitude": "123.11212",
      "floor": 1
    },
    {
      "id": 2,
      "name": "Stage 2",
      "latitude": "75.12212",
      "longitude": "123.14512",
      "floor": 1
    }
  ]
}
```
