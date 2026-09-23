# passport ticket

A passport in front of a travel ticket.

Keyshape: SQUARE. Balanced composition; target centerline box (6,6)-(42,42).

Plan: Foreground passport with a globe; tilted notched ticket behind it, with two writing rules.

Construction: ticket: notched perimeter; supplied source owns the overlapping arrangement.

Omissions: Small lower ticket slot omitted; globe meridian retained.

Visual review: Passport and ticket arrangement survives, but the globe is filled in by its crowded equator and meridian. Ticket writing is too close to its boundary. Not visually approved.

```text
status: invalid
  ERROR  mic [ticket-text-0]: parallel straight edges ticket-text-0 and ticket-text-1 are 7.84465 apart on centerlines (ink gap 3.84465); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [passport]: passport and globe are 4 apart on centerlines nearest (6, 29)<->(10, 29); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [passport]: passport and ticket-text-0 are 4.07114 apart on centerlines nearest (25.9675, 20.5598)<->(30, 20); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [ticket]: ticket and ticket-text-1 are 3.53009 apart on centerlines nearest (38.4615, 29.6923)<->(35, 29); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [ticket-text-0]: ticket-text-0 and ticket-text-1 are 7.84465 apart on centerlines nearest (35, 21)<->(33.4615, 28.6923); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```
