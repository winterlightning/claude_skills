# face awesome

Status: `exception` — user-authorized rule violations. Full circle retained; smaller eye symbols stay separate from the head.

User instruction:
> for those emoji, i want you to remain the circle, just draw the heart, start, @ smaller, even if broke the rule, im good with it

Automatic model validation: invalid.

```text
BUILD GATE FAIL (fail, 7 errors, 8 warnings)
  error: mic [star-1]: parallel straight edges star-1-4 and star-1-7 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
  error: mic [star-0]: parallel straight edges star-0-4 and star-0-7 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
  error: mic [head]: head and star-0 are 5.23487 apart on centerlines nearest (6.39849, 14.504)<->(11, 17); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  error: mic [head]: head and star-1 are 5.23487 apart on centerlines nearest (41.6015, 14.504)<->(37, 17); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  error: mic [head]: head and open-grin are 6.99987 apart on centerlines nearest (23.957, 43.9997)<->(24, 37); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  error: mic [star-0]: star-0 and star-1 are 6 apart on centerlines nearest (21, 17)<->(27, 17); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  error: holes/pinches: 2 undersized holes; 0 pinches
  warning: mic [star-0]: star-0 and open-grin are 8 apart on centerlines nearest (19, 23)<->(19, 31); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  warning: mic [star-1]: star-1 and open-grin are 8 apart on centerlines nearest (29, 23)<->(29, 31); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  warning: internal-spacing [star-0]: star-0-1 and star-0-8 have 1.9322 units of ink clearance over 2.733 units; requires 4; review required
  warning: internal-spacing [star-0]: star-0-3 and star-0-10 have 1.9322 units of ink clearance over 2.733 units; requires 4; review required
  warning: internal-spacing [star-0]: star-0-4 and star-0-7 have 2 units of ink clearance over 2 units; requires 4; review required
  warning: internal-spacing [star-1]: star-1-1 and star-1-8 have 1.9322 units of ink clearance over 2.733 units; requires 4; review required
  warning: internal-spacing [star-1]: star-1-3 and star-1-10 have 1.9322 units of ink clearance over 2.733 units; requires 4; review required
  warning: internal-spacing [star-1]: star-1-4 and star-1-7 have 2 units of ink clearance over 2 units; requires 4; review required
```
