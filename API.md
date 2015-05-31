# Open-Event API Endpoint Documentation

## Endpoints
All the GET endpoints are suffix to the domain where we will set up the [organiser server](https://github.com/fossasia/open-event-orga-server)   

### Event
` GET /get/v1/event  `  


Example response - 
```javascript
{
  "events": [
    {
      "end_time": "2015-05-08T16:00:00", 
      "id": 3, 
      "latitude": 23.3455, 
      "location_name": "Berlin Station", 
      "longitude": 78.1233, 
      "name": "Re:Publica", 
      "start_time": "2015-05-01T14:00:00"
    }, 
    {
      "end_time": "2015-06-12T05:00:00", 
      "id": 4, 
      "latitude": 56.8876, 
      "location_name": "Singapore", 
      "longitude": 123.4567, 
      "name": "FOSSASIA", 
      "start_time": "2015-06-10T05:00:00"
    }
  ]
}
```

` GET /get/v1/event/<event-id>  `  

Example Response (for event-id = 3, ie /get/v1/event/3) - 
```javascript

{
  "end_time": "2015-05-08T16:00:00", 
  "id": 3, 
  "latitude": 23.3455, 
  "location_name": "Berlin Station", 
  "longitude": 78.1233, 
  "name": "Re:Publica", 
  "start_time": "2015-05-01T14:00:00"
}
```

### Sessions
` GET /get/v1/event/<event-id>/sessions  ` 

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
` GET /get/v1/event/<event-id>/tracks  `

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
` GET /get/v1/event/<event-id>/speakers  ` 

### Sponsors
` GET /get/v1/event/<event-id>/sponsors  ` 

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
` GET /get/v1/event/<event-id>/microlocations  `  

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
