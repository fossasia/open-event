## Resources & Permissions

### Understanding the access control matrix

- Each row is inclusive of the permission qualifiers of rows below it. 

	_Example:_
	
	|   | List | View | Create | Update | Delete |
	|---|------|------|--------|--------|--------|
	| **Superadmin/admin** | ✓ | ✓ | ✓ | ✓ |  ✓ |
	| **Event organizer** | ✓ <sup>[1]</sup> | ✓ <sup>[1]</sup> | ✓ <sup>[1]</sup> | ✓ <sup>[1]</sup> | ✓ <sup>[1]</sup> |
	| **Everyone else** | ✓ <sup>[2]</sup> | ✓ <sup>[2]</sup>  |  | |  |
	
	1. Only self-owned events
	2. Only of events with state `published`
	
	
	Here,
	
	- **Event organizer** can list the resources of **self-owned events** and **other events with with state `published`**.
	- **Everyone else** can view resources of **other events with with state `published`**.
	- **Superadmin/admin** can do both of the above.

- Multiple permission qualifiers used together represt an `AND` operation.
	
	_Example:_
	
	Consider the following qualifiers,
	1. Only of sessions with state `approved` or `accepted`
	2. Only to events with state `published`.

	When used together as `[1][2]`, it means, **Only of sessions with state `approved` or `accepted` those belong to events with state `published`**.
	

---

### Resources

#### Users - Eg. `/v1/users`

Users consists of all the regsitered users of Open Event

|   | List | View | Create | Update | Delete |
|---|------|------|--------|--------|--------|
| **Superadmin/admin** | ✓ | ✓ | ✓ | ✓ |  ✓ |
| **Registered user** |  | ✓ <sup>[1]</sup> |  | ✓ <sup>[1][2]</sup> |  |
| **Everyone else** |  |  | ✓ <sup>[3]</sup> |  |  |

1. Only self
2.  Except `is-admin`, `password`, `is-verified`, `is-super-admin` all allowed
3. Only `email`, `first-name`, `last-name`, `twitter-url`, `facebook-url`, `google-plus-url`, `avatar-url` & `password` fields allowed

---

#### Event types - Eg. `/v1/event-types`

|   | List | View | Create | Update | Delete |
|---|------|------|--------|--------|--------|
| **Superadmin/admin** | ✓ | ✓ | ✓ | ✓ |  ✓ |
| **Everyone else** | ✓ | ✓ | |  |  |

---

#### Event topics - Eg. `/v1/event-topics`

|   | List | View | Create | Update | Delete |
|---|------|------|--------|--------|--------|
| **Superadmin/admin** | ✓ | ✓ | ✓ | ✓ |  ✓ |
| **Everyone else** | ✓ | ✓ | |  |  |

---

#### Event sub-topics - Eg. `/v1/event-sub-topics`

|   | List | View | Create | Update | Delete |
|---|------|------|--------|--------|--------|
| **Superadmin/admin** | ✓ | ✓ | ✓ | ✓ |  ✓ |
| **Everyone else** | ✓ | ✓ | |  |  |


---

#### Custom Placeholders - Eg. `/v1/custom-placeholders`

Each sub-topic can have a custom placeholder. The image of site logo, and the placeholder for the user's profile picture are also stored here.

|   | List | View | Create | Update | Delete |
|---|------|------|--------|--------|--------|
| **Superadmin/admin** | ✓ | ✓ | ✓ | ✓ |  ✓ |
| **Everyone else** | ✓ | ✓ | |  |  |

---

#### Events - Eg. `/v1/events`

The events created in Open Event. One of the primary resources of Open Event.

|   | List | View | Create | Update | Delete |
|---|------|------|--------|--------|--------|
| **Superadmin/admin** | ✓ | ✓ | ✓ | ✓ |  ✓ |
| **Event organizer** | ✓ | ✓ | ✓ | ✓ <sup>[1]</sup> | ✓ <sup>[1]</sup> |
| **Registered user** | ✓ | ✓ | ✓ | |  |
| **Everyone else** | ✓ | ✓ |  | |  |

1. Only self-owned events

---

#### Event Copyrights - Eg. `/v1/event-copyright`

Each event will have a copyright information attached to it. (Eg. All rights reserved, Creative commons attribution (or) a custom one)

|   | List | View | Create | Update | Delete |
|---|------|------|--------|--------|--------|
| **Superadmin/admin** | ✓ | ✓ | ✓ | ✓ |  ✓ |
| **Event organizer** | ✓ | ✓ | ✓ | ✓ <sup>[1]</sup> | ✓ <sup>[1][2]</sup> |
| **Everyone else** | ✓ | ✓ |  | |  |

1. Only self-owned events
2. Cannot delete a copyright relationship with an event. Can only update relationship. 

---

#### Event Invoices - Eg. `/v1/event-invoice`

At the end of the billing period (one month), each event organizer who is selling the tickets to their events via Open Event would get an invoice. (The event invoice). This invoice is for the Open Event fee collected for each ticket sale using the service. _(Not to be confused with `Orders` or `Attendees`)_

|   | List | View | Create | Update | Delete |
|---|------|------|--------|--------|--------|
| **Superadmin/admin** | ✓ | ✓ | | ✓ |  ✓ |
| **Event organizer** | ✓ <sup>[1]</sup> | ✓ <sup>[1]</sup> | | | |
| **Everyone else** | | |  | |  |

1. Only self-owned events

---

#### Microlocations - Eg. `/v1/microlocations`

Each session can happen in a microlocation. (Eg. a room or a hall). A microlocation will have multiple sessions. But a session can have only one microlocation.

|   | List | View | Create | Update | Delete |
|---|------|------|--------|--------|--------|
| **Superadmin/admin** | ✓ | ✓ | ✓ | ✓ |  ✓ |
| **Event organizer** | ✓ <sup>[1] / [2]</sup> | ✓ <sup>[1] / [2]</sup> | ✓ <sup>[1]</sup> | ✓ <sup>[1]</sup> | ✓ <sup>[1]</sup> |
| **Everyone else** | ✓ <sup>[2]</sup> | ✓ <sup>[2]</sup>  |  | |  |

1. Only self-owned events
2. Only of events with state `published`

---

#### Sessions - Eg. `/v1/sessions`

Sessions are distinct micro-events that occur within an event. (They can consist of talks, breaks, lunch, performance, etc). A session can also have speakers. A session can have multiple speakers. A speaker can have multiple sessions.

|   | List | View | Create | Update | Delete |
|---|------|------|--------|--------|--------|
| **Superadmin/admin** | ✓ | ✓ | ✓ | ✓ |  ✓ |
| **Event organizer** | ✓ <sup>[1]</sup> | ✓ <sup>[1]</sup> | ✓ <sup>[1]</sup> | ✓ <sup>[1]</sup> | ✓ <sup>[1]</sup> |
| **Registered User** | ✓ <sup>[3]</sup> | ✓ <sup>[3]</sup> | ✓ <sup>[4]</sup> | ✓ <sup>[3]</sup> | ✓ <sup>[3]</sup> |
| **Everyone else** | ✓ <sup>[2][4]</sup> | ✓ <sup>[2][4]</sup> |  | |  |

1. Only self-owned events
2. Only sessions with state `approved` or `accepted`
3. Only self-submitted sessions
4. Only to events with state `published`.

---

#### Session type - Eg. `/v1/session-types`

Sessions can be categorized into distinct types. Each session  type would also have a duration that represets how long each session within that type could last. A session type will have multiple sessions. But a session can have only one session type.


|   | List | View | Create | Update | Delete |
|---|------|------|--------|--------|--------|
| **Superadmin/admin** | ✓ | ✓ | ✓ | ✓ |  ✓ |
| **Event organizer** | ✓ <sup>[1]</sup> | ✓ <sup>[1]</sup> | ✓ <sup>[1]</sup> | ✓ <sup>[1]</sup> | ✓ <sup>[1]</sup> |
| **Everyone else** | ✓ <sup>[2]</sup> | ✓ <sup>[2]</sup>  |  | |  |

1. Only self-owned events
2. Only of events with state `published`

---

#### Speakers - Eg. `/v1/speakers`

Speakers (aka speaker profiles) are the human element of each session. Each speakers instance could be linked to one user instance. But one user can have multiple speaker profiles. A speaker can also have multiple sessions under him/her. 

|   | List | View | Create | Update | Delete |
|---|------|------|--------|--------|--------|
| **Superadmin/admin** | ✓ | ✓ | ✓ | ✓ |  ✓ |
| **Event organizer** | ✓ <sup>[1]</sup> | ✓ <sup>[1]</sup> | ✓ <sup>[1]</sup> | ✓ <sup>[1]</sup> | ✓ <sup>[1]</sup> |
| **Registered User** | ✓ <sup>[3]</sup> | ✓ <sup>[3]</sup> | ✓ <sup>[4]</sup> | ✓ <sup>[3]</sup> | ✓ <sup>[3]</sup> |
| **Everyone else** | ✓ <sup>[2][4]</sup> | ✓ <sup>[2][4]</sup> |  | |  |

1. Only self-owned events
2. Only of sessions with state `approved` or `accepted`
3. Only of self-submitted sessions
4. Only to events with state `published`.

---

#### Social Links - Eg. `/v1/social-links`

Social links represent social network links of each event. An event can have multiple social links.

|   | List | View | Create | Update | Delete |
|---|------|------|--------|--------|--------|
| **Superadmin/admin** | ✓ | ✓ | ✓ | ✓ |  ✓ |
| **Event organizer** | ✓ <sup>[1]</sup> | ✓ <sup>[1]</sup> | ✓ <sup>[1]</sup> | ✓ <sup>[1]</sup> | ✓ <sup>[1]</sup> |
| **Everyone else** | ✓ <sup>[2]</sup> | ✓ <sup>[2]</sup>  |  | |  |

1. Only self-owned events
2. Only of events with state `published`


---

#### Speaker Calls - Eg. `/v1/speaker-calls`

Speaker Calls (usually known as Call for speakers) is an invitation sent out people asking them to submit their talk for an event (usually a conference). An event can have only one speaker call record. 

|   | List | View | Create | Update | Delete |
|---|------|------|--------|--------|--------|
| **Superadmin/admin** | | ✓ | ✓ | ✓ |  ✓ |
| **Event organizer** | | ✓ <sup>[1]</sup> | ✓ <sup>[1]</sup> | ✓ <sup>[1]</sup> | ✓ <sup>[1]</sup> |
| **Everyone else** | | ✓ <sup>[2]</sup>  |  | |  |

1. Only self-owned events
2. Only of events with state `published`

---

#### Sponsors - Eg. `/v1/sponsors`

An event would usually be sponsored by companies in-turn for advertisement oppurtunities.  An event can have multiple sponsors. But a sponsor would be linked to only one event.

|   | List | View | Create | Update | Delete |
|---|------|------|--------|--------|--------|
| **Superadmin/admin** | ✓ | ✓ | ✓ | ✓ |  ✓ |
| **Event organizer** | ✓ <sup>[1]</sup> | ✓ <sup>[1]</sup> | ✓ <sup>[1]</sup> | ✓ <sup>[1]</sup> | ✓ <sup>[1]</sup> |
| **Everyone else** | ✓ <sup>[2]</sup> | ✓ <sup>[2]</sup>  |  | |  |

1. Only self-owned events
2. Only of events with state `published`

---

#### Tax - Eg. `/v1/taxes`

If the event is organized by a commercial company that has a tax account, they would want to pass on the taxes to the ticket amount payed by the user. They will also want the tax account number specified on the invoice sent to them. That is collected here. An event can have only one tax record. And a tax record will have only one event.

|   | List | View | Create | Update | Delete |
|---|------|------|--------|--------|--------|
| **Superadmin/admin** | | ✓ | ✓ | ✓ |  ✓ |
| **Event organizer** | | ✓ <sup>[1]</sup> | ✓ <sup>[1]</sup> | ✓ <sup>[1]</sup> | ✓ <sup>[1]</sup> |
| **Everyone else** | | ✓ <sup>[2]</sup> |  | |  |

1. Only self-owned events
2. Only `rate` and `is_tax_included` fields

---

#### Tickets - Eg. `/v1/tickets`

The primary revenue source in the Open Event project. Organizers of events can sell tickets to their events. An event can have multiple tickets. Each ticket has a sales period and a fixed quantity.

|   | List | View | Create | Update | Delete |
|---|------|------|--------|--------|--------|
| **Superadmin/admin** | ✓ | ✓ | ✓ | ✓ |  ✓ |
| **Event organizer** | ✓ <sup>[1]</sup> | ✓ <sup>[1]</sup> | ✓ <sup>[1]</sup> | ✓ <sup>[1]</sup> | ✓ <sup>[1]</sup> |
| **Everyone else** | ✓ <sup>[2]</sup> | ✓ <sup>[2]</sup>  |  | |  |

1. Only self-owned events
2. Only of events with state `published`, and tickets with tickets sale active and quantity not exhausted.

---

#### Ticket tags - Eg. `/v1/ticket-tags`

Each ticket could be assigned to a tag. (Eg. premium tickets, free tickets etc). And later the tickets can be displayed/queried/grouped by tags. One ticket can have multiple tags. One tag can have multiple tickets.

|   | List | View | Create | Update | Delete |
|---|------|------|--------|--------|--------|
| **Superadmin/admin** | ✓ | ✓ | ✓ | ✓ |  ✓ |
| **Event organizer** | ✓ <sup>[1]</sup> | ✓ <sup>[1]</sup> | ✓ <sup>[1]</sup> | ✓ <sup>[1]</sup> | ✓ <sup>[1]</sup> |
| **Everyone else** | ✓ <sup>[2]</sup> | ✓ <sup>[2]</sup>  |  | |  |

1. Only self-owned events
2. Only of events with state `published`

---

#### Orders - Eg. `/v1/orders`

Each purchase request starts with the creation of an order resource. It holds the status of their payment, payment token, confirmation, payment mode, price etc. Order is used while calculating the invoice and service-fee. A pdf containing all tickets would be available here on successful order completion.

|   | List | View | Create | Update | Delete |
|---|------|------|--------|--------|--------|
| **Superadmin/admin** | ✓ | ✓ | ✓ | ✓ |  ✓ |
| **Event organizer** | ✓ <sup>[1]</sup> | ✓ <sup>[1]</sup> | ✓ <sup>[1]</sup> | ✓ <sup>[1][2]</sup> | ✓ <sup>[1][3]</sup> |
| **Registered user** | | ✓ <sup>[4]</sup> |  | |  |
| **Everyone else** | | |  | |  |

1. Only self-owned events
2. Can only change order status
3. A refund will also be initiated if paid ticket
2. Only if order placed by self

---

#### Attendees - Eg. `/v1/attendees`

Attendee (aka Ticket Holder) is part of every order. An order would have atleast one attendee attached to it. An attendee can be linked to only one ticket. A pdf with a single ticket will be available here on successful order completion. 

|   | List | View | Create | Update | Delete |
|---|------|------|--------|--------|--------|
| **Superadmin/admin** | ✓ | ✓ | ✓ | ✓ |  ✓ |
| **Event organizer** | ✓ <sup>[1]</sup> | ✓ <sup>[1]</sup> | ✓ <sup>[1]</sup> | ✓ <sup>[1]</sup> | ✓ <sup>[1]</sup> |
| **Registered user** | | ✓ <sup>[2]</sup> |  | |  |
| **Everyone else** | | |  | |  |

1. Only self-owned events
2. Only of tickets purchased by self or tickets with self as one of the ticket holders

---

#### Tracks - Eg. `/v1/tracks`

Tracks represent a set of similar sessions grouped together. (Eg. Android track would contail all sessions related to the Android OS or android apps). A track will have multiple sessions. But a session can have only one track.

|   | List | View | Create | Update | Delete |
|---|------|------|--------|--------|--------|
| **Superadmin/admin** | ✓ | ✓ | ✓ | ✓ |  ✓ |
| **Event organizer** | ✓ <sup>[1]</sup> | ✓ <sup>[1]</sup> | ✓ <sup>[1]</sup> | ✓ <sup>[1]</sup> | ✓ <sup>[1]</sup> |
| **Everyone else** | ✓ <sup>[2]</sup> | ✓ <sup>[2]</sup>  |  | |  |

1. Only self-owned events
2. Only of events with state `published`

---

#### Ticket Fees - Eg. `/v1/ticket-fees`

We collect service fees for each ticket sold through Open Event. This allows the admins to specify what percentage/value of fee to collect for each currency type.

|   | List | View | Create | Update | Delete |
|---|------|------|--------|--------|--------|
| **Superadmin/admin** | ✓ | ✓ | ✓ | ✓ |  ✓ |
| **Everyone else** | ✓ | ✓ | |  |  |


---

#### Notifications - Eg. `/v1/notifications`

The users can recieve notifications (email, push or in-app notification) from the system. Microservices such as the app generators can also send notifications to users. A user can also mark his/her notifications as read.

|   | List | View | Create | Update | Delete |
|---|------|------|--------|--------|--------|
| **Superadmin/admin** | ✓ | ✓ | | | ✓ |
| **Registered user** | ✓ <sup>[1]</sup> | ✓ <sup>[1]</sup> | | ✓ <sup>[1][2]</sup> |  |
| **Mobile app generator** | | ✓ | |  |  |
| **Webapp app generator** | | ✓ | |  |  |
| **Everyone else** | | | |  |  |

1. Only notifications to self
2. Only `is-read` field.

---

#### Email Notifications - Eg. `/v1/email-notifications`

Ever user has the ability to control the types of notifications they recieve from the Open Event system. Notifications for specific events can be turned on/off on an event level basis.

|   | List | View | Create | Update | Delete |
|---|------|------|--------|--------|--------|
| **Superadmin/admin** | ✓ | ✓ | ✓ | ✓  | |
| **Registered user** |  | ✓ <sup>[1]</sup> | ✓ <sup>[1]</sup> | ✓ <sup>[1]</sup> |  |
| **Everyone else** | | | |  |  |

1. Only self

---

#### Discount Codes - Eg. `/v1/discount-codes`

 Two different forms of discount code can exist. (Both use the same model/resource/api)
 
1. Created by the super admin and can be applied to whole events when creating an event. (this discount is on the total ticket sales service fee that goes to Open Event) - `used-for=event`
2. Created by an event's organizer to be used on a specific event's tickets - `used-for=ticket`


|   | List | View | Create | Update | Delete |
|---|------|------|--------|--------|--------|
| **Superadmin/admin** | ✓ | ✓ | ✓ | ✓  | |
| **Sales admin** | ✓ <sup>[1]</sup> | ✓ <sup>[1]</sup> | ✓ <sup>[1]</sup> | ✓ <sup>[1]</sup>  | |
| **Marketer** | ✓ <sup>[1][2]</sup> | ✓ <sup>[1][2]</sup> | |  | |
| **Event organizer** | ✓ <sup>[3]</sup> | ✓ <sup>[3]</sup> | ✓ <sup>[3]</sup> | ✓ <sup>[3]</sup> |  ✓ <sup>[3]</sup>|
| **Registered user** | | ✓ <sup>[4]</sup> | |  |  |
| **Everyone else** | | | |  |  |


1. Only those with `used-for` as `event`
2. Only those assigned to self
3. Only those of self-owned events
4. Only valid and non-exhausted ones and accessed via the discount code itself (not ID).

---

#### Access Codes - Eg. `/v1/access-codes`

Some tickets are hidden by default and can be accessed only via a special access code. Each access code can be linked to multiple tickets.

|   | List | View | Create | Update | Delete |
|---|------|------|--------|--------|--------|
| **Superadmin/admin** | ✓ | ✓ | ✓ | ✓  | |
| **Event organizer** | ✓ <sup>[1]</sup> | ✓ <sup>[1]</sup> | ✓ <sup>[1]</sup> | ✓ <sup>[1]</sup> |  ✓ <sup>[1]</sup>|
| **Registered user** | | ✓ <sup>[2]</sup> | |  |  |
| **Everyone else** | | | |  |  |


1. Only those of self-owned events
2. Only valid and non-exhausted ones and accessed via the access code itself (not ID).

---

#### Role Invites - Eg. `/v1/role-invites`

A user can be given additional roles on an event. The role invite is sent as a notification to the user via this.

|   | List | View | Create | Update | Delete |
|---|------|------|--------|--------|--------|
| **Superadmin/admin** | ✓ | ✓ | ✓ | ✓ | ✓ |
| **Event organizer** | ✓ <sup>[1]</sup> | ✓ <sup>[1]</sup> | ✓ <sup>[1]</sup> | ✓ <sup>[1]</sup> |  ✓ <sup>[1]</sup>|
| **Registered user** | | ✓ <sup>[2]</sup> | | ✓ <sup>[2][3]</sup> |  |
| **Everyone else** | | | |  |  |


1. Only those of self-owned events
2. Only invites sent to self. (ie. `invite.email === self.email`).
3. Only change `status` field.

---

#### Image Sizes - Eg. `/v1/image-sizes`

The size of the images used throughout the site, (event background image, profile pic image) etc can be adjusted here. The images are resized while saving depending on the values here.

|   | List | View | Create | Update | Delete |
|---|------|------|--------|--------|--------|
| **Superadmin/admin** | ✓ | ✓ | ✓ | ✓ | ✓ |
| **Everyone else** | | | |  |  |

---

#### Roles - Eg. `/v1/roles`

Each user can have multiple roles. Each roles has different permissions. 

|   | List | View | Create | Update | Delete |
|---|------|------|--------|--------|--------|
| **Superadmin/admin** | ✓ | ✓ | ✓ | ✓ | ✓ |
| **Registered user** | ✓ | ✓ | |  |  |
| **Everyone else** | | | |  |  |

---

#### Activities - Eg. `/v1/activites`

Every operation made on Open Event, is logged as an activity in the database. Admins can view these activities if and when needed.

|   | List | View | Create | Update | Delete |
|---|------|------|--------|--------|--------|
| **Superadmin/admin** | ✓ | ✓ | | | |
| **Everyone else** | | | |  |  |

---

#### Pages - Eg. `/v1/pages`

The public facing pages of Open Event are customizable. (About us page, contact us page etc). The pages can be added or removed. Each page can have multiple language content.

|   | List | View | Create | Update | Delete |
|---|------|------|--------|--------|--------|
| **Superadmin/admin** | ✓ | ✓ | ✓ | ✓ | ✓ |
| **Everyone else** | ✓ | ✓ | |  |  |

---

#### Settings - Eg. `/v1/settings`

The administrative settings of Open Event.

|   | List | View | Create | Update | Delete |
|---|------|------|--------|--------|--------|
| **Superadmin/admin** | | ✓ | | ✓ |  |
| **Everyone else** | | ✓ <sup>[1]</sup> |  | |  |

1. Only `app_name`, `tagline`, `analytics_key`, `stripe_publishable_key`, `google_url`, `github_url`, `twitter_url`, `support_url`, `facebook_url`, `youtube_url`, `android_app_url`, `web_app_url` fields .

---

#### Modules - Eg. `/v1/modules`

Open Event allows users to turn on/off specific modules of the system (eg. ticketing). That can be controlled here. 

|   | List | View | Create | Update | Delete |
|---|------|------|--------|--------|--------|
| **Superadmin/admin** | | ✓ | | ✓ |  |
| **Everyone else** | | ✓ |  | |  |

---

#### Upload - Eg. `/v1/upload/*`

Images and files can be uploaded to a temporary location via these. 

|   | List | View | Create | Update | Delete |
|---|------|------|--------|--------|--------|
| **Superadmin/admin** | ✓ | ✓ | ✓ | ✓ | ✓ |
| **Registered user** | | ✓ | ✓ | | |
| **Everyone else** | | | | | |
