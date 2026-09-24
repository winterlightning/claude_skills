# monitoring-heart-beat-hand

Subject: monitoring heart beat hand.

Keyshape: SQUARE. Square composition balances heart above a lower-right grip.

Omissions/reductions: Reduced secondary heartbeat peak.

Construction references: Lucide heart-pulse and hand; rounded lobes and fingertip.

Visual review at 48px and enlarged in both themes: Blocked: pulse crowds hand; lower heart pocket remains undersized. Grip is deliberately asymmetric.

Validation: invalid.

BUILD GATE FAIL (fail, 2 errors, 2 warnings)
  error: mic [pulse]: pulse and hand are 3.41424 apart on centerlines nearest (31.4333, 18)<->(31.4333, 21.4142); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  error: holes/pinches: 1 undersized holes; 0 pinches
  warning: mic [heart]: heart and pulse are 0 apart on centerlines nearest (6.73535, 18)<->(6.73535, 18); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  warning: mic [heart]: heart and hand are 0 apart on centerlines nearest (34.489, 22.489)<->(34.489, 22.489); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship

