# Fresh review repairs: pin through SE

All ten completed: eight strict passes and two user-approved dollar-sign spacing exceptions. The prior strict failures remain in their original run folders.

| Subject | Full QA | SVG | Artifacts |
|---|---|---|---|
| pin | PASS | [SVG](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/f442e678-6fbd-570e-923f-8eae8fd127e0/20260925-review-redraw/location-pin-above-baseline.svg) | [Run](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/f442e678-6fbd-570e-923f-8eae8fd127e0/20260925-review-redraw) |
| cart | PASS | [SVG](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/4f97114c-a7e4-4f5d-935d-2b5d4711fb3f/20260925-review-redraw/shopping-cart-rounded-basket.svg) | [Run](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/4f97114c-a7e4-4f5d-935d-2b5d4711fb3f/20260925-review-redraw) |
| plane | PASS | [SVG](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/1a77b164-d1b5-40f6-89b4-9b211524fbb0/20260925-review-redraw/airplane-top-view-swept-wings.svg) | [Run](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/1a77b164-d1b5-40f6-89b4-9b211524fbb0/20260925-review-redraw) |
| man graduate | PASS | [SVG](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/7764a030-9bc6-4b16-aa7c-7ad4e9ca54bc/20260925-review-redraw/man-graduate-avatar.svg) | [Run](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/7764a030-9bc6-4b16-aa7c-7ad4e9ca54bc/20260925-review-redraw) |
| laptop dollar sign | PASS · approved exception | [SVG](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/e6666fd5-a646-4ccf-89c4-7931517ccd22/20260925-dollar-spacing-exception/laptop-dollar-symbol.svg) | [Run](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/e6666fd5-a646-4ccf-89c4-7931517ccd22/20260925-dollar-spacing-exception) |
| mobile phone dollar sign | PASS · approved exception | [SVG](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/31035467-a6b8-4c8d-8d52-52dc236bc2c7/20260925-dollar-spacing-exception/mobile-phone-dollar-sign.svg) | [Run](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/31035467-a6b8-4c8d-8d52-52dc236bc2c7/20260925-dollar-spacing-exception) |
| hand | PASS | [SVG](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/14e0f209-1f73-4be1-9637-df2de37b666b/20260925-review-redraw/open-palm-hand.svg) | [Run](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/14e0f209-1f73-4be1-9637-df2de37b666b/20260925-review-redraw) |
| shopping cart | PASS | [SVG](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/22ba9936-54d3-4de1-815f-e80d16f43ff1/20260925-review-redraw/shopping-cart-right-grip-lower-rail.svg) | [Run](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/22ba9936-54d3-4de1-815f-e80d16f43ff1/20260925-review-redraw) |
| thermometer | PASS | [SVG](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/b9550739-2fcc-4d3f-b1da-62a62d9213f5/20260925-review-redraw/thermometer-mercury.svg) | [Run](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/b9550739-2fcc-4d3f-b1da-62a62d9213f5/20260925-review-redraw) |
| se (text) | PASS | [SVG](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/65ff17d5-d6f4-45f8-9685-b215f34e7ba1/20260925-review-redraw/se-text.svg) | [Run](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/65ff17d5-d6f4-45f8-9685-b215f34e7ba1/20260925-review-redraw) |

## Review notes

### pin

Pin narrowed from VRECT_L to VRECT_M; bigger circular opening and a longer detached baseline restore the source proportions. Point remains symmetric and clear of the baseline.

### cart

Deeper basket, small curved right handle, restored support curl and two equal outlined wheels. Source asymmetry and shopping direction preserved.

### plane

Nose top-to-wing-root height increases from 6 to 8 units (one to three units of straight neck below the round nose). Upright VRECT_L layout preserves swept wings and paired tail planes; both sides derive from x=24. Wing/tail tips remain angular to meet clearance.

### man graduate

Cap now sits on its band and open face instead of floating above a circular head. Left tassel restored. Radius-8 circular jaw ends at y32; symmetric shoulders peak y36, giving the avatar-required zero ink gap. Detailed gown V and tassel droplet omitted because they crowd the 48px geometry.

### laptop dollar sign

Restored dollar top/bottom ticks and the laptop base divider. Earlier strict candidate (superseded by the approved exception) failed: dollar bottom and screen divider have only 4 centerline units; lower tick is only 1 unit from divider. The 2-unit alternative is now approved and saved in a new run.

### mobile phone dollar sign

Restored dollar top/bottom ticks and the phone footer divider. Earlier strict candidate (superseded by the approved exception) failed: lower tick is only 4 centerline units from the footer. The 2-unit alternative is now approved and saved in a new run.

### hand

Longer finger creases restore finger-to-palm proportions. Thumb perimeter no longer crosses itself. Four fingertip widths share radius4 and pitch8. HRECT_L remains broader than the source because four finger widths and a thumb consume the 40-unit horizontal budget; thumb is more upright than the reference.

### shopping cart

Deeper tapered basket, right grip, continuous lower support and attached equal circular wheels restore missing chassis structure.

### thermometer

Taller tube and smaller smoothly joined bulb replace the oversized bowl. Separate mercury line and central dot match the supplied source.

### se (text)

S and E now share cap-height and baseline, correcting the smaller floating S. S curves join coherently, E retains a shortened middle arm.

## Currency exception approved

The user approved both smaller dollar signs as shown in the 2-unit-spacing proposals. Current SVGs are accepted using drawing-bound exceptions; automatic strict validation findings are preserved. [Updated preview](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/20260925-review-batch-pin-se/approved-currency-preview.png).
