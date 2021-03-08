# Open Event
[![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/fossasia/open-event?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge) [![Mailing List](https://img.shields.io/badge/Mailing%20List-FOSSASIA-blue.svg)](https://groups.google.com/forum/#!forum/open-event)

The Open Event Project offers event managers a platform to help users organize events including concerts, conferences, summits and regular meetups . The components support organizers through all stages from event planning to publishing, marketing and ticket sales. Automated web and mobile apps help attendees to get information easily. The Open Event Project was originally started to support the organization of the [FOSSASIA OpenTechSummit](http://fossasia.org) and is maintained by the **FOSSASIA** community.The Open Event boasts a diverse ecosystem and is composed of several components:

## Components of Open Event Ecosystem

### The Open Event Format Definition
[![Repository](https://img.shields.io/badge/Repository-Visit-blue.svg)](https://github.com/fossasia/open-even) [![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/fossasia/open-event)
The **Open Event** format enables the exchange of data between all components as well as with other services through a standardized Format. This *open-event* repository provides a sample implementation of the format. It includes `JSON` files for all relevant event information and binary data for images and audio files. The repository holds the **JSON Schema** sample implementation in the [/sample](/sample/) folder, that is used across all projects for testing. We keep:
- Zip files that include all `JSON` files with binary media data, **And**
- The uncompressed files that can act as APIs substitutes to test applications.

### The Open Event Server
[![Repository](https://img.shields.io/badge/Repository-Visit-blue.svg)](https://github.com/fossasia/open-event-server) [![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/fossasia/open-event-server)
The **Open Event Server** is the centralised backend powering most of the components of the open event ecosystem. The open event server exposes a well documented JSON:API Spec Compliant REST API that can be used by external services (like the Open Event Organiser App and the Open Event Frontend) to access & manipulate the data. Using the APIs of the open event server, it is possible for the other components of open event like the open event organiser app, and the open event frontend to enable organizers to manage events from concerts to conferences and meetups. The APIs offer features for events with several tracks and venues. Event managers can create invitation forms for speakers and build schedules in a Drag & Drop interface. The system provides API endpoints to fetch the data, and to modify and update it. Organizers can import and export event data in a standard compressed file format that includes the event data in `JSON` and binary media files like images and audio.

### The Open Event Frontend
[![Repository](https://img.shields.io/badge/Repository-Visit-blue.svg)](https://github.com/fossasia/open-event-frontend) [![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/fossasia/open-event-frontend)
The **Open Event Frontend** as the name suggests, is a web app written in Ember.js which consumes the Open Event Server API to give the users a medium to interact with the several functionalities and features which the open event server offers, in an intuitive manner, with a moder UI/UX. It's responsive design allows effecient browsing on mobile web browswers along with large screen devices. While the open event server serves as the backend, all the users including administrators need to interact only with the frontend.

### The Open Event Android App
[![Repository](https://img.shields.io/badge/Repository-Visit-blue.svg)](https://github.com/fossasia/open-event-android) [![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/fossasia/open-event-android)
The **Open Event Android App** is an android app which allows users to discover events happening around the world using the Open Event Platform. It consumes the APIs of the open event server to get a list of available events, and can get detailed information about them. It is possible to  buy event tickets.
The app also offers other modern features such as easy check-in using QR codes. This app is meant for the users who intend to browse events and purchase tickets for them as an attendee.

### The Open Event iOS App
[![Repository](https://img.shields.io/badge/Repository-Visit-blue.svg)](https://github.com/fossasia/open-event-ios) [![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/fossasia/open-event-ios)
The **Open Event iOS App** is the iOS counterpart of the Open Event Android app, currently in development. The app will eventually achieve the same functionalities as the Open Event Android app, and alloww users to discover event, book tickets, and will use the Open Event Server as the backend.

### The Open Event Organiser Android App
[![Repository](https://img.shields.io/badge/Repository-Visit-blue.svg)](https://github.com/fossasia/open-event-orga-app) [![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/fossasia/open-event-orga-app)
The Open Event Organiser app is intended for the organizers and entry managers who intend for their event to be available in the Open Event Ecosystem. While the Open Event Android and iOS apps allow the users to browse the events happening around them, the organiser app allows creation and management of those events from an organzer's perspective with intuitive features like push notifications, ticket management, and check in using QR codes.

### The Open Event Organiser iOS App
[![Repository](https://img.shields.io/badge/Repository-Visit-blue.svg)](https://github.com/fossasia/open-event-orga-iOS) [![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/fossasia/open-event-ios)
The **Open Event Organiser iOS App** is the iOS counterpart of the Open Event Organiser Android app, currently in development. The app will eventually achieve the same functionalities as the Open Event Organiser Android app, and allow the users to browse the events happening around them, the organiser app allows creation and management of those events from an organzer's perspective with intuitive features like push notifications, ticket management, and check in using QR codes.

### Open Event Web App Generator
[![Repository](https://img.shields.io/badge/Repository-Visit-blue.svg)](https://github.com/fossasia/open-event-webapp) [![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/fossasia/open-event-web-app)
The **Open Event Web App** generator is an event website generator.  The web generator application can generate event websites by getting data from event `JSON` files and binary media files, that are stored in a compressed zip file with an Open Event Format Specification. You can also access the application through a Rest API. Websites that are generated by the web app generator can be uploaded to any web location, e.g. on Github pages or any server.

### The Open Event Android App Generator
[![Repository](https://img.shields.io/badge/Repository-Visit-blue.svg)](https://github.com/fossasia/open-event-droidgen) [![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/fossasia/open-event-droidgen)
The **open-event-droidgen** is a web application that is hosted on a server and generates an event Android app from a zip file in an Open Event Format Specification containing JSON and binary files.You can also access the application through a Rest API. Apps that are generated by the android app generator can be uploaded to the play store and be readily made available, which is of great convenience to the orgazers, as an organizer can generate a ready to publish app for his/her event.

## License
This repository is licensed under the [GNU General Public License v3](LICENSE.md).
To obtain the software under a different license, Please contact **FOSSASIA**.
