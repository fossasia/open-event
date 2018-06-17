## Glossary

#### Terms, acronyms & abbreviations
- **N/A** - Not applicable. This case isn't applicable here. (Eg. either the endpoint itself doesn't/cannot exist or would be illogical to have one)
- **FE** - The Frontend (Eg. `open-event-frontend`, `open-event-orga-app`)
- **BE** - The Backend (The API Server)
- **Gateway** - The API Gateway (Eg. Kong)
- **Microservice** - Microservices such as android app generator, webapp generator etc
- **k8s** - Kubernetes
- **self** - Refers to the currently authenticated user. (The one who is consuming the API)

#### Default roles: 
##### Server level roles
- **Superadmin** - The super admin user of the API Server instance. (There will only be one)
- **Admin** - An admin user of the API Server instance. (There can be multiple.)
- **Sales Admin** - Sales administrator for the Open Event application. Can view/create/delete marketers, event creation discount codes (discount codes applied while creating an event. This will be the discount on the service fee the event organizer pays to eventyay from ticket sales), view sales data.
- **Marketer** - A marketer will go and sell eventyay and try to bring more users into the site using assigned discount codes. View sales info. Will be assigned discount codes and can view them.

##### Event level roles
- **Event admin** - An event's organizer/created (There will be one per event)
- **Event co-organizer** - An event's co-organizer. (There can be multiple) (Also includes all the above event level roles)
- **Event organizer** - Event admin (or) Event co-organizer
- **Event Moderator** - An event's moderator who would review sessions/speakers etc. (There can be multiple) (Also includes all the above event level roles)

##### Visitor roles
- **Registered and verified user** - A user who has logged in and has verified their email.
- **Registered and unverified user** - A user who has logged but hasn't verified their email.
- **Registered user** - A user who has logged in
- **Unauthenticated user** - A visitor who hasn't logged in. (No JWT auth token in request)


##### Microservice roles
- **Mobile app generator** - The Open Event public application
- **Web app generator** - The Open Event web application
