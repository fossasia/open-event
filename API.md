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

### Speakers
` GET /get/v1/speakers.json ` 

### Sponsors
` GET /get/v1/sponsors.json ` 

Example response  - 
```javascript
{
  "sponsors": [
    {
      "0": {
        "name": "Google",
        "url": "http://google.com",
        "logo": "http://google.com/logo.png"
      },
      "1": {
        "name": "RedHat",
        "url": "http://redhat.org",
        "logo": "http://redhat.org/logo.png"
      }
    }
  ]
}
```

### Microlocation
` GET /get/v1/microlocations.json ` 
