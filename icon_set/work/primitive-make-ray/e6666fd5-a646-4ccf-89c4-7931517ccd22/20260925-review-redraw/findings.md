# laptop dollar sign

Reviewed at native 48px and 144px in both themes. Restored dollar top/bottom ticks and the laptop base divider. Complete strict candidate remains blocked: dollar bottom and screen divider have only 4 centerline units; lower tick is only 1 unit from divider. Separate 2-unit-spacing proposal saved without approval or validator exception.

Construction references: laptop + dollar-sign. Lucide originals and atomic geometry were inspected.

status: invalid
  ERROR  mic [dollar]: parallel straight edges dollar-6, dollar-5 and screen-5 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [screen]: screen and currency-bottom are 1 apart on centerlines nearest (24, 34)<->(24, 33); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
Full QA: fail
mic [dollar]: parallel straight edges dollar-6, dollar-5 and screen-5 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal)
mic [screen]: screen and currency-bottom are 1 apart on centerlines nearest (24, 34)<->(24, 33); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship