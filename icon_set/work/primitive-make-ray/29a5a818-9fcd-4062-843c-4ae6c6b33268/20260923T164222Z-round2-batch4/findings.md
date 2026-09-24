# credit card payment

A payment terminal with receipt beside a card and insertion arrow.

**HRECT_L**: The wide composition uses the 40 by32 centerline envelope. The module obtains its exact visible bounds from the profile.

Construction references: credit-card: outlined card and stripe; source supplies terminal and receipt.

Reduction: Six keypad marks reduced to two; receipt serrations reduced to one broad notch.

Validation: **invalid**, 4 errors, 2 warnings.

Visual review at48px and240px in light and dark: **not approved**. Receipt and terminal remain identifiable; the detached card stripe fills its narrow card and cannot read cleanly. Receipt-to-terminal clearances also fail. Not approved.

Exact unresolved checks, elements and coordinates:

```text
status: invalid
  ERROR  mic [card]: parallel straight edges card-2-0 and stripe are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [stripe]: parallel straight edges stripe and card-6-0 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [terminal]: parallel straight edges terminal-2-0, terminal-2-1 and receipt-5, receipt-6 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (overlap-fallback)
  ERROR  mic [receipt]: parallel straight edges receipt-2, receipt-1 and terminal-6-1, terminal-6-0 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (overlap-fallback)
  WARN   mic [terminal]: terminal and key-0 are 8 apart on centerlines nearest (12, 40)<->(12, 32); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  WARN   mic [terminal]: terminal and key-1 are 8 apart on centerlines nearest (20, 40)<->(20, 32); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```

[SVG](credit-card-payment.svg) · [Python](credit_card_payment_29a5a818_9fcd_4062_843c_4ae6c6b33268.py) · [Light](light-240.png) · [Dark](dark-240.png)
