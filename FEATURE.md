#Feature List and Technologies

##Open-Event Organiser Server/Web Client
- Database sqlite/postgresql
- Provides Api for WebApp and Android App (Configuration, Session, Speakers, Sponsors etc.)
- Possibility changes configuration(Gui colors, conference logo, timezone, event title, event email) 
- CRUD methods for (Session, Events, etc) in admin panel

## Open-Event WebApp
- Responsible Web Design(RWD)
- Shows information about Session, Speakers, Map of location, Sponsors

## Open-Event Android App
- SQLite Database with an efficient schema, so that no extra data is stored
- Navigation drawer with fragments using generics
- Recycler view wherever lists are required, cardview in about us fragment, all in api v21 onwards
- Data retrieval through json api using volley library
- versioning check from the api on start of data download
- Offline support for the app
