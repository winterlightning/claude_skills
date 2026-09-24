# crypto currency megacoin

A Megacoin badge containing three equal domed arches.

**CIRCLE**: The reference is defined by a circular enclosure; centerline radius20 about (24,24). The module obtains its exact visible bounds from the profile.

Construction references: No useful exact currency logo match; parameterized identical arches within a circle.

Reduction: None; all three arches retained.

Validation: **invalid**, 6 errors, 0 warnings.

Visual review at48px and240px in light and dark: **not approved**. All three arches and the coin enclosure remain. The arches crowd each other and the circle; the original logo cannot be approved in this attempted fit.

Exact unresolved checks, elements and coordinates:

```text
status: invalid
  ERROR  mic [arch-2-left]: parallel straight edges arch-2-left and arch-1-rest-1 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [arch-1-left]: parallel straight edges arch-1-left and arch-0-rest-1 are 4 apart on centerlines (ink gap 0); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [coin]: coin and arch-0-left are 3.50747 apart on centerlines nearest (4.59248, 28.8314)<->(8, 28); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [coin]: coin and arch-2-rest are 3.50747 apart on centerlines nearest (43.4075, 28.8314)<->(40, 28); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [arch-0-top]: arch-0-top and arch-1-left are 4 apart on centerlines nearest (16, 23)<->(20, 23); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
  ERROR  mic [arch-1-top]: arch-1-top and arch-2-left are 4 apart on centerlines nearest (28, 23)<->(32, 23); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```

[SVG](crypto-currency-megacoin.svg) · [Python](crypto_currency_megacoin_13d0089e_f330_48ba_93f8_58b6b6f1f9e2.py) · [Light](light-240.png) · [Dark](dark-240.png)
