# Nine icon redraws after visual review

All nine requested originals were redrawn in place. Existing icon IDs, source IDs and module filenames are preserved; no v2 icons were created. Only these nine icon models were edited in this follow-up.

## Validation and visual evidence

- Fresh model and full build QA: 9/9 pass, no errors or warnings.
- Targeted gallery build: exit 0; all nine exported SVGs match the models and QA hashes.
- Focused primitive, profile/keyshape, parallel-spacing, internal-spacing and symmetry tests: 68 passed.
- Native 48 px and enlarged views checked in both light and dark themes.
- `changes.json` preserves before/after SVG hashes; every before hash was verified against the drawing captured in the preceding nine-icon review.
- `comparison-light-1.png`, `comparison-dark-1.png` and `index.html` show the actual reviewed drawing beside this redraw.
- `before/` preserves the nine previous Python models. `before-svg/` and `after-svg/` preserve the compared artwork.
- `final-qa.json`, `build.log` and `tests.log` retain the validation evidence.

The original source SVGs informed subject identity. Previously inspected Lucide bird and paw-print geometry informed sparse curves and repeated pads; the shared human reference informed circular face construction. The human icon depicts a head and hand, not a detached full-body figure.

The user's authorization to resize beyond standard keyshapes remains applied through documented custom envelopes. The 48 px canvas, 4-unit stroke, integer nodes, round joins/caps and clearance rules remain unchanged. Production artwork and approval statuses were not changed by this local redraw.

## Visual decisions

| Icon | Change | Symmetry / intent |
|---|---|---|
| cough | Open mouth in profile with three expelled cough strokes; rounded cranium and chin. | Left-facing profile and forceful, outward breath marks; intentional asymmetry. |
| paw-print | Four rounded toes in a compact arch above a smooth mirrored three-lobed pad; matching oval toes. | Mirrored about x=24; matching oval toes and tangent-continuous pad curves. |
| paw-print-small-outer-toes | Four rounded toes in a compact arch above a smooth mirrored three-lobed pad; smaller outlined outer toes. | Mirrored about x=24; smaller outer toes retain visible openings instead of becoming solid dots. |
| peacock-with-spread-tail | Circular spread fan with radial feather divisions behind a tapered bird body, curved head profile and two feet. | Fan, feather divisions, lower body and feet mirror about x=24; head faces right. A small crest reinforces the bird identity. |
| pelican-on-water | Long bill and shallow pouch, visible eye, continuous neck and floating belly, and a shallow water ripple. | Left-facing bill and pouch, curved neck, eye and closed floating body. Water is a shallow wave. |
| perching-bird | Rounded songbird body and back, a distinct short tail and folded wing, standing on two legs on a branch. | Left-facing curved body, shortened tail and two legs with real branch contacts. |
| person-receiving-cheek-massage | Relaxed circular face with gently closed eyes and a curved palm, thumb and wrist pressing the cheek. | Closed eyes mirror about x=24; diagonal palm and wrist press the right cheek, with the hidden face edge omitted. |
| oval-stadium-with-two-flags | Wide open arena with a low curved stadium wall and two complete repeated pennants, anchored on the rear rim. | Rim and wall mirror about x=24; two repeated pennants point right and attach to the rear rim. |
| oval-stadium-with-three-flags | Wide open arena with a low curved stadium wall and three complete repeated pennants, anchored on the rear rim. | Same arena construction with three identical pennants at a constant horizontal spacing. |

These are revised candidates for visual review. Passing geometry checks is reported separately from the design assessment.
