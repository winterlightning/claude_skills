# subtitles-display

Rounded subtitles panel with complete SUB lettering. Rebalanced B remains distinct from the panel and has open bowls; glyph spacing is unresolved.

- Source UUID: `dd1e6365-7d94-41e2-84d6-66c8ad75ede1`
- Reference: `pictographic-primitives/other/rectangle sub text_dd1e6365-7d94-41e2-84d6-66c8ad75ede1.svg`
- Author: `gpt-6`
- Keyshape: `HRECT_L`; visible ink bounds `[2, 6, 46, 42]`. Wide envelope preserves horizontal text and its enclosure.
- Full QA: **fail**.

## Construction and omissions

Lucide rectangle-ellipsis original and atomic-debug: rounded panel; supplied reference governs SUB.

No defining component omitted.

## Visual review

Both themes/native48: full SUB inscription and open B bowls are retained. Narrow gaps among letters and panel remain. No visual approval for release.

## Validation

- mic [b-stem]: parallel straight edges b-stem-2, b-stem-1 and u-2 are 5 apart on centerlines (ink gap 1); requires at least 8 centerline / 4 ink (midpoint-normal)
- mic [u]: parallel straight edges u-2 and u-0 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
- mic [panel]: panel and s are 5.80664 apart on centerlines nearest (4, 18.8867)<->(9.80664, 18.8867); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
- mic [panel]: panel and b-bow are 5 apart on centerlines nearest (44, 20)<->(39, 20); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
- mic [s]: s and u are 5.89846 apart on centerlines nearest (16.1389, 28.813)<->(22.0144, 28.2941); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
- mic [u]: u and b-stem are 5 apart on centerlines nearest (28, 28)<->(33, 28); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
- mic [panel]: panel and u are 8 apart on centerlines nearest (22, 8)<->(22, 16); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
- internal-spacing [u]: u-0 and u-2 have 2 units of ink clearance over 11 units; requires 4; review required
- internal-spacing [b-stem / b-bow]: b-stem-1 and b-bow-1 have 1.5224 units of ink clearance over 4.1881 units; requires 4; review required
- internal-spacing [b-stem / b-bow]: b-stem-2 and b-bow-0 have 1.5224 units of ink clearance over 4.1881 units; requires 4; review required
