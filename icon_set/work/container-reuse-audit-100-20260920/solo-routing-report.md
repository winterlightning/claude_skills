# Solo rerouting — 76 empty frames/devices

All **76** source reference briefs now route to **solo** in the local gallery database.

- reuse_existing_solo: **42** sources
- adapt_existing_solo: **3** sources
- convert_existing_artwork_to_solo: **31** sources

**0** fresh-generation jobs were created. The 24 sources with inner content are unchanged.

These are source-routing changes, not completed geometry/family migrations. Existing solo assets can be reused. Other existing artwork is explicitly held for adaptation or SOLO48 conversion. Matching uses the standard-library subject, not pixel identity; meaningful differences are noted below. All candidates were visually inspected and their SVG files verified.

To prevent duplicate generation, these sources remain SKIP with reason `other` and a reuse explanation, instead of being returned to TODO. Their saved reference brief family is `solo`. Obsolete container component fields were cleared; complete previous values are retained in `before-solo-routing.json`.

The original 100-source audit is historical; this routing supersedes its treatment of these 76 sources. Existing model families, artwork, and the production gallery were not changed.

| # | Source | Action | Existing icon | Note |
|---|---|---|---|---|
| 4 | Layout with Left Sidebar | reuse_existing_solo | layout-with-left-sidebar-batch-001-r3 | Use the earlier batch-001-r3 version: its dashed divider is correctly on the left; the newer solo-b001-04 version incorrectly centers two dots. |
| 5 | Left Sidebar Navigation Layout | reuse_existing_solo | left-sidebar-navigation-layout-solo-b001-05 | Existing solo uses two navigation marks rather than three; reuse the standard layout. |
| 6 | Right Sidebar Interface Panel | reuse_existing_solo | right-sidebar-interface-panel-solo-b001-06 | Existing solo uses two navigation marks rather than three; reuse the standard layout. |
| 12 | Closed Left Hand Sliding Door | reuse_existing_solo | closed-left-hand-sliding-door-solo-b002-01 | Existing solo artwork matches this standalone subject; reuse it. |
| 13 | Closed Right Sliding Door | reuse_existing_solo | closed-right-sliding-door-solo-b002-02 | Existing solo artwork matches this standalone subject; reuse it. |
| 16 | Simple Entrance Door | reuse_existing_solo | simple-entrance-door-solo-b002-04 | Existing solo artwork matches this standalone subject; reuse it. |
| 23 | Stacked Data Tables | adapt_existing_solo | stacked-data-tables-solo-b002-14 | Existing solo has a reduced table grid; restore the source three-column, two-row grid. |
| 24 | Standard Payment Credit Card | reuse_existing_solo | standard-payment-credit-card-solo-b002-15 | Existing solo artwork matches this standalone subject; reuse it. |
| 25 | Broken Speech Bubble | reuse_existing_solo | broken-speech-bubble-solo-b003-03 | Existing solo artwork matches this standalone subject; reuse it. |
| 27 | Document with Folded Corner | reuse_existing_solo | blank-folded-corner-page | Existing solo artwork matches this standalone subject; reuse it. |
| 32 | Desktop Computer Monitor | reuse_existing_solo | desktop-monitor-centre-post-stand | Existing solo artwork matches this standalone subject; reuse it. |
| 33 | Computer Monitor Screen | reuse_existing_solo | desktop-monitor-bezel-splayed-stand | Existing solo artwork matches this standalone subject; reuse it. |
| 34 | Desktop Computer Monitor | reuse_existing_solo | desktop-monitor-bezel-splayed-stand | Existing solo artwork matches this standalone subject; reuse it. |
| 35 | Desktop Computer Monitor | adapt_existing_solo | desktop-monitor-curved-pedestal | Add the lower bezel divider to the existing curved-pedestal solo monitor. |
| 36 | Desktop Computer Monitor | adapt_existing_solo | desktop-monitor-curved-pedestal | Same bezel addition as source 35; share one adapted solo asset. |
| 37 | Computer Monitor Screen | reuse_existing_solo | desktop-monitor-splayed-stand | Existing solo artwork matches this standalone subject; reuse it. |
| 38 | Desktop Computer Monitor Screen | reuse_existing_solo | desktop-monitor-bezel-splayed-stand | Existing solo artwork matches this standalone subject; reuse it. |
| 40 | Cinema Movie Film Frame | reuse_existing_solo | film-strip-frame | Existing solo uses connected perforation boxes rather than small separated slots; same film-frame concept. |
| 41 | Classroom Presentation Board | convert_existing_artwork_to_solo | presentation-board | Existing artwork is currently CONTAINER64. Reuse its geometry for a SOLO48 conversion; do not generate an independent duplicate. |
| 42 | Cloud Shaped Speech Bubble | convert_existing_artwork_to_solo | cloud-speech-bubble | Existing artwork is currently CONTAINER64. Reuse its geometry for a SOLO48 conversion; do not generate an independent duplicate. |
| 43 | Computer Monitor and Keyboard | reuse_existing_solo | monitor-with-desk-keyboard | Existing solo adds a monitor stem; same blank monitor-and-keyboard subject. |
| 44 | Computer Monitor with Webcam | convert_existing_artwork_to_solo | monitor-webcam | Existing artwork is currently CONTAINER64. Reuse its geometry for a SOLO48 conversion; do not generate an independent duplicate. |
| 45 | Desktop Computer Monitor | reuse_existing_solo | desktop-monitor-centre-post-stand | Existing solo artwork matches this standalone subject; reuse it. |
| 46 | Desktop Computer Monitor | reuse_existing_solo | desktop-monitor-centre-post-stand | Existing solo artwork matches this standalone subject; reuse it. |
| 47 | Desktop Computer Monitor | reuse_existing_solo | desktop-monitor-curved-pedestal | Existing solo artwork matches this standalone subject; reuse it. |
| 48 | Double Speech Bubbles | convert_existing_artwork_to_solo | double-speech-bubbles | Existing artwork is currently CONTAINER64. Reuse its geometry for a SOLO48 conversion; do not generate an independent duplicate. |
| 49 | Eight Pointed Star Badge | convert_existing_artwork_to_solo | eight-pointed-star-badge | Existing artwork is currently CONTAINER64. Reuse its geometry for a SOLO48 conversion; do not generate an independent duplicate. |
| 50 | Empty Battery Level Indicator | reuse_existing_solo | battery-1 | Existing solo artwork matches this standalone subject; reuse it. |
| 51 | Framed Achievement Certificate | convert_existing_artwork_to_solo | framed-achievement-certificate | Existing artwork is currently CONTAINER64. Reuse its geometry for a SOLO48 conversion; do not generate an independent duplicate. |
| 52 | Hanging Pennant Banner | convert_existing_artwork_to_solo | hanging-pennant-banner | Existing artwork is currently CONTAINER64. Reuse its geometry for a SOLO48 conversion; do not generate an independent duplicate. |
| 53 | Hanging Store Sign | reuse_existing_solo | hanging-shop-sign-solo | Existing solo artwork matches this standalone subject; reuse it. |
| 54 | Horizontal Coupon Voucher | convert_existing_artwork_to_solo | horizontal-ticket-voucher | Existing artwork is currently CONTAINER64. Reuse its geometry for a SOLO48 conversion; do not generate an independent duplicate. |
| 55 | Horizontal Mobile Phone | convert_existing_artwork_to_solo | horizontal-mobile-phone | Existing artwork is currently CONTAINER64. Reuse its geometry for a SOLO48 conversion; do not generate an independent duplicate. |
| 56 | Horizontal Ticket Voucher | convert_existing_artwork_to_solo | horizontal-ticket-voucher | Existing artwork is currently CONTAINER64. Reuse its geometry for a SOLO48 conversion; do not generate an independent duplicate. |
| 57 | Landscape Mobile Phone | convert_existing_artwork_to_solo | landscape-mobile-phone | Existing artwork is currently CONTAINER64. Reuse its geometry for a SOLO48 conversion; do not generate an independent duplicate. |
| 58 | Landscape Mobile Phone | convert_existing_artwork_to_solo | landscape-mobile-phone | Existing artwork is currently CONTAINER64. Reuse its geometry for a SOLO48 conversion; do not generate an independent duplicate. |
| 59 | Landscape Smartphone | convert_existing_artwork_to_solo | horizontal-mobile-phone | Existing artwork is currently CONTAINER64. Reuse its geometry for a SOLO48 conversion; do not generate an independent duplicate. |
| 60 | Mail Envelope Icon | convert_existing_artwork_to_solo | mail-envelope | Existing artwork is currently CONTAINER64. Reuse its geometry for a SOLO48 conversion; do not generate an independent duplicate. |
| 61 | Mobile Phone Device | reuse_existing_solo | smartphone-bottom-bezel-solo-08a24aa4 | Existing solo artwork matches this standalone subject; reuse it. |
| 62 | Movie Film Frame | convert_existing_artwork_to_solo | movie-film-frame | Existing artwork is currently CONTAINER64. Reuse its geometry for a SOLO48 conversion; do not generate an independent duplicate. |
| 63 | Movie Film Frame | convert_existing_artwork_to_solo | movie-film-frame | Existing artwork is currently CONTAINER64. Reuse its geometry for a SOLO48 conversion; do not generate an independent duplicate. |
| 64 | Movie Film Strip Frame | convert_existing_artwork_to_solo | movie-film-frame | Existing artwork is currently CONTAINER64. Reuse its geometry for a SOLO48 conversion; do not generate an independent duplicate. |
| 65 | Open Envelope with Letter | reuse_existing_solo | open-envelope-with-letter-solo | Existing solo artwork matches this standalone subject; reuse it. |
| 66 | Oval Speech Bubble | convert_existing_artwork_to_solo | oval-speech-bubble | Existing artwork is currently CONTAINER64. Reuse its geometry for a SOLO48 conversion; do not generate an independent duplicate. |
| 67 | Pair of Square Brackets | reuse_existing_solo | square-brackets | Existing solo artwork matches this standalone subject; reuse it. |
| 68 | Pair of Square Brackets | reuse_existing_solo | square-brackets | Existing solo artwork matches this standalone subject; reuse it. |
| 69 | Rectangular Picture Frame | reuse_existing_solo | double-bordered-rectangle | Existing solo differs in proportions but preserves the double-bordered empty frame. |
| 70 | Retro Television with Antenna | reuse_existing_solo | retro-television-antenna | Existing solo has an extra inset screen border; same empty retro television subject. |
| 71 | Retro Television with Antennas | reuse_existing_solo | retro-television-antenna | Reuse the same retro television as source 70. |
| 72 | Right Pointing Label Symbol | convert_existing_artwork_to_solo | right-pointing-label-tag | Existing artwork is currently CONTAINER64. Reuse its geometry for a SOLO48 conversion; do not generate an independent duplicate. |
| 73 | Right Pointing Label Tag | convert_existing_artwork_to_solo | right-pointing-label-tag | Existing artwork is currently CONTAINER64. Reuse its geometry for a SOLO48 conversion; do not generate an independent duplicate. |
| 74 | Right Pointing Tag | convert_existing_artwork_to_solo | right-pointing-label-tag | Existing artwork is currently CONTAINER64. Reuse its geometry for a SOLO48 conversion; do not generate an independent duplicate. |
| 75 | Round Smartwatch | convert_existing_artwork_to_solo | round-smartwatch | Existing artwork is currently CONTAINER64. Reuse its geometry for a SOLO48 conversion; do not generate an independent duplicate. |
| 76 | Round Smartwatch | convert_existing_artwork_to_solo | round-smartwatch | Existing artwork is currently CONTAINER64. Reuse its geometry for a SOLO48 conversion; do not generate an independent duplicate. |
| 77 | Rounded Rectangular Frame | reuse_existing_solo | rectangle-frame | Existing solo artwork matches this standalone subject; reuse it. |
| 78 | Rounded Square Brackets | reuse_existing_solo | square-brackets | Existing solo artwork matches this standalone subject; reuse it. |
| 79 | Simple House Icon | reuse_existing_solo | plain-house-outline-102d245d-463e-51ca-9972-ba1befe53f32 | Existing solo artwork matches this standalone subject; reuse it. |
| 80 | Simple House Shape | reuse_existing_solo | plain-house-outline-102d245d-463e-51ca-9972-ba1befe53f32 | Existing solo artwork matches this standalone subject; reuse it. |
| 81 | Square Alignment Measurement Frame | convert_existing_artwork_to_solo | square-alignment-measurement-frame | Existing artwork is currently CONTAINER64. Reuse its geometry for a SOLO48 conversion; do not generate an independent duplicate. |
| 82 | Square Artboard with Corner Indicators | convert_existing_artwork_to_solo | square-artboard-with-corner-indicators | Existing artwork is currently CONTAINER64. Reuse its geometry for a SOLO48 conversion; do not generate an independent duplicate. |
| 83 | Square Grid Layout | convert_existing_artwork_to_solo | square-alignment-measurement-frame | Existing artwork is currently CONTAINER64. Reuse its geometry for a SOLO48 conversion; do not generate an independent duplicate. |
| 84 | Square Measuring Viewfinder Frame | convert_existing_artwork_to_solo | square-alignment-measurement-frame | Existing artwork is currently CONTAINER64. Reuse its geometry for a SOLO48 conversion; do not generate an independent duplicate. |
| 85 | Square Note with Top Hole | convert_existing_artwork_to_solo | square-note-with-top-hole | Existing artwork is currently CONTAINER64. Reuse its geometry for a SOLO48 conversion; do not generate an independent duplicate. |
| 86 | Square Selection Box | reuse_existing_solo | square-selection-corner-handles | Existing solo artwork matches this standalone subject; reuse it. |
| 87 | Square Selection Box | reuse_existing_solo | square-selection-corner-handles | Existing solo artwork matches this standalone subject; reuse it. |
| 88 | Square Smartwatch Device | reuse_existing_solo | square-face-smartwatch | Reuse the existing square smartwatch with open curved wrist strap. |
| 89 | Stacked Browser Windows | convert_existing_artwork_to_solo | stacked-browser-windows | Existing artwork is currently CONTAINER64. Reuse its geometry for a SOLO48 conversion; do not generate an independent duplicate. |
| 90 | Stacked Web Browser Windows | convert_existing_artwork_to_solo | stacked-browser-windows | Existing artwork is currently CONTAINER64. Reuse its geometry for a SOLO48 conversion; do not generate an independent duplicate. |
| 91 | Stacked Web Browser Windows | convert_existing_artwork_to_solo | stacked-browser-windows | Existing artwork is currently CONTAINER64. Reuse its geometry for a SOLO48 conversion; do not generate an independent duplicate. Add the other two header controls; the existing stacked-browser container has one. |
| 92 | Upper Part of Smartphone | reuse_existing_solo | mobile-phone-with-speaker-slot | Use the complete phone with speaker slot for the cropped upper-phone reference. |
| 93 | Upward Pointing Tag | reuse_existing_solo | plain-house-outline-102d245d-463e-51ca-9972-ba1befe53f32 | Same pointed-top empty silhouette as the existing plain house outline; reuse the geometry with tag terminology rather than draw a duplicate. |
| 94 | Vertical Admission Ticket | reuse_existing_solo | ticket-1 | Rotate the existing ticket 90 degrees to place notches at top and bottom. |
| 95 | Vertical Admission Ticket | reuse_existing_solo | ticket-1 | Same rotated ticket asset as source 94. |
| 96 | Vertical Admission Ticket | reuse_existing_solo | ticket-1 | Same rotated ticket asset as source 94. |
| 97 | Web Browser Window | reuse_existing_solo | browser-header-window-solo-dd2e4d0c | Existing solo artwork matches this standalone subject; reuse it. |
| 98 | Web Browser Window Interface | reuse_existing_solo | browser-header-window-solo-dd2e4d0c | Existing solo artwork matches this standalone subject; reuse it. |
