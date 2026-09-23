# scooter parking shade roof

Scooter under a pitched shelter roof; two wheels, seat, body and steering column.

HRECT_L: Wide object silhouette; visible envelope (2,6)-(46,42).

bike: shared wheel radii and baseline; no useful scooter shelter match.

Omitted tiny seat seam; preserved shelter, seat, scooter body, handle and both wheels.

Shelter roof, wheels and scooter silhouette remain recognizable, but seat/body and front fender are congested. Not approved.

```text
status: invalid
  ERROR  mic [roof]: roof and seat are 5.81378 apart on centerlines nearest (6.4, 16.8)<->(9, 22); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [rear-wheel]: rear-wheel and seat are 7.4018 apart on centerlines nearest (11.9331, 32.1449)<->(10, 25); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [front-wheel]: front-wheel and front-fender are 4.06231 apart on centerlines nearest (32.5197, 34.0284)<->(29, 32); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [body]: body and seat are 2.10474 apart on centerlines nearest (11.0151, 26.8438)<->(10, 25); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```
