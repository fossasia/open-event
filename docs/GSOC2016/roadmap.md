GSOC 2016 is about to start. And a lot of coding activity will take place on the open-event repos in the coming months. It is good to have a roadmap of broad features we intend to add to these projects.

Tagging all parties involved on this to give their opinion -
@leto @mariobehling @creativepsyco  @batraabhishek @mananwason @rafalkowalski @hpdang

## Open Event Org Server

- [ ] Access control (event creators, event admins, event speakers - with different editing permissions)
- [ ] Support for Oauth tokens and API keys, so 3rd party app can register and use data
- [ ] Add support for voting talks
- [ ] Support for more information about the event like nearby airport/station, bus routes.

## Open Event Android App

- [ ] Automated scripts to generate apk (organisers can build apk without editing/writing any code)
- [ ] Extract API data fetching code into a separate module, and be able to turn that portion into a jar/aar library
- [ ] Support for more information about the event like nearby airport/station, bus routes.
- [ ] Add support for Android Wear, to give reminders about bookmarked events
- [ ] Add support for deeklinks to open in the app (http://event.com/speaker/1)

## Open Event Webapp
- [ ] Move to Angular2 (or possible some framework like React/Ember) - with the objective of improving performance.
- [ ] Have theming support. Not only for colors, but more components as well.
- [ ] Possibly extract api functionality into a separate js lib
- [ ] Implement lazy loaders or paginators for speakers and sessions when lists are long
- [ ] Support for more information about the event like nearby airport/station, bus routes.
