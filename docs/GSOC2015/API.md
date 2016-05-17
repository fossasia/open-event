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
      "slogan": "into the wild",
      "id": 3, 
      "latitude": 23.3455, 
      "location_name": "Berlin Station", 
      "longitude": 78.1233, 
      "name": "Re:Publica", 
      "start_time": "2015-05-01T14:00:00",
      "url": "http://14.re-publica.de/"
    }, 
    {
      "end_time": "2015-06-12T05:00:00",
      "slogan": "IN/SIDE/OUT",
      "id": 4, 
      "latitude": 56.8876, 
      "location_name": "Singapore", 
      "longitude": 123.4567, 
      "name": "FOSSASIA", 
      "start_time": "2015-06-10T05:00:00",
      "url": "http://fossasia.org/"
    }
  ]
}
```

` GET /get/v1/event/<event-id>  `  

Example Response (for event-id = 3, ie /get/v1/event/3) - 
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
    }
  ]
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
      "description": "All things to talk about Linux",
      "track_image_url": "http://www.menucool.com/slider/jsImgSlider/images/image-slider-2.jpg"
    },
    {
      "id": 2,
      "name": "Android",
      "description": "All things to talk about Android",
      "track_image_url": "http://www.menucool.com/slider/jsImgSlider/images/image-slider-2.jpg"
    },
    {
      "id": 3,
      "name": "Java",
      "description": "All things to talk about Java",
      "track_image_url": "http://www.menucool.com/slider/jsImgSlider/images/image-slider-2.jpg"
    }
  ]
}
```

### Speakers
` GET /get/v1/event/<event-id>/speakers  ` 

Example response - 
```javascript
{
  "speakers": [
    {
      "id": 4,
      "name": "Arnav Gupta",
      "photo": "http://championswimmer.in/photo.png",
      "bio": "A jolly good fellow",
      "email": "championswimmer@gmail.com",
      "web": "http://championswimmer.in",
      "twitter": "championswimmer",
      "facebook": "championswimmer",
      "linkedin": "http://linkedin.com/in/arnavgupta",
      "github": "championswimmer",
      "organisation": "DTU",
      "position": "Student",
      "country": "India",
      "sessions": [
        {
            "id": 2,
            "title": "Open Event"
        }
      ]
    },
    {
      "id": 2,
      "name": "Manan Wason",
      "photo": "http://manan.in/photo.png",
      "bio": "A jolly good fellow",
      "email": "mananwason@gmail.com",
      "web": "http://mananwason.in",
      "twitter": "mananwason",
      "facebook": "mananwason",
      "linkedin": "http://linkedin.com/in/mananwason",
      "github": "mananwason",
      "organisation": "IIIT-D",
      "position": "Student",
      "country": "India",
      "sessions": [
        {
            "id": 2,
            "title": "Open Event"
        },
        {
            "id": 3,
            "title": "Open-Event-Server"
        }
      ]
    }
  ]
}
```

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

### The latest Version
` GET /get/v1/version `  

Example Response -  
```
{
  "version": 
  [
    {
      "event_id": 2,
      "event_ver": 2,
      "id": 19,
      "microlocations_ver": 0,
      "session_ver": 3,
      "speakers_ver": 1,
      "sponsors_ver": 0,
      "tracks_ver": 0
    }
  ]
}
```
### The latest Version of Event
` GET /get/v1/event/<event_id>/version `  

Example Response -  
`/get/v1/event/1/version ` 
```
{
  "version": 
  [
    {
      "event_id": 1,
      "event_ver": 2,
      "id": 19,
      "microlocations_ver": 0,
      "session_ver": 3,
      "speakers_ver": 1,
      "sponsors_ver": 0,
      "tracks_ver": 0
    }
  ]
}
```
