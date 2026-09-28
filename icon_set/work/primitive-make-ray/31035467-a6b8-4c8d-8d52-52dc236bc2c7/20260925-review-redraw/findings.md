# mobile phone dollar sign

Reviewed at native 48px and 144px in both themes. Restored dollar top/bottom ticks and the phone footer divider. Complete strict candidate remains blocked: lower tick is only 4 centerline units from the footer. Separate 2-unit-spacing proposal saved without approval or validator exception.

Construction references: smartphone + dollar-sign. Lucide originals and atomic geometry were inspected.

status: invalid
  ERROR  mic [dollar]: parallel straight edges dollar-6, dollar-5 and footer are 7 apart on centerlines (ink gap 3); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [footer]: footer and currency-bottom are 4 apart on centerlines nearest (24, 36)<->(24, 32); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
Full QA: fail
mic [dollar]: parallel straight edges dollar-6, dollar-5 and footer are 7 apart on centerlines (ink gap 3); requires at least 8 centerline / 4 ink (midpoint-normal)
mic [footer]: footer and currency-bottom are 4 apart on centerlines nearest (24, 36)<->(24, 32); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship