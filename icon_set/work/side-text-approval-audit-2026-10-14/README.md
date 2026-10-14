# Side text and wallet review proposals

These are local review artifacts, not production state or an automatic deployment script.
Open `review.html` in a browser to compare the original SVG with each proposed SVG,
including native 64px previews. `proposals.json` records reference IDs and component
revisions; each folder contains its layout and visual verdict.

31 layout fixes are proposed. The crypto USB wallet uses HRECT with the USB main
at preset 44 and its Bitcoin badge unchanged at 32. The plug remains intact and
the cord retains its elbow and horizontal end; only its plain tip is cut.

Four cases remain unchanged: AMEX credit card, CCPA lock, GDPR document and deepfake
person. Their native labels cannot fit cleanly with the existing components.

The text workflow registers the exact native SVG without approving it, preserves
conflicting revisions under separate IDs, requires component approval, and requires
a fresh combination build before final approval. No automatic approval or
production upload is included in these artifacts.

Validation: 31 proposed layouts passed keyshape and contact recording. SFTP and
both INDD cases retain a documented 5-unit clear-space exception. The wallet was
re-reviewed after user feedback. 42 Rust unit tests, 15 UI tests and 4 native-text
regression tests passed; isolated local HTTP checks verified text registration,
revision collisions, approval ordering and invalid keyshape rejection.

The broader baseline still has two browser parity/rounding failures, one Rust
migration integration expectation failure, and three Python workflow expectation
failures. Those broader suites are not reported as passing.

Production deployment and data changes from this task were rolled back at the
user’s request. Deployment requires separate explicit permission after PR review.
