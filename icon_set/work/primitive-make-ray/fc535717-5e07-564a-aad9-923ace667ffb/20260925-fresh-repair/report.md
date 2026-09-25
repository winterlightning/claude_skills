# star-award-badge-ribbon

Round award medal with a crisp five-point star and symmetric notched ribbon. Star arms and ribbon now pass internal spacing; inset star-to-medal clearance remains unresolved.

- Source UUID: `fc535717-5e07-564a-aad9-923ace667ffb`
- Reference: `pictographic-primitives/holidays/star_fc535717-5e07-564a-aad9-923ace667ffb.svg`
- Author: `gpt-6`
- Keyshape: `VRECT_L`; visible ink bounds `[6, 2, 42, 46]`. Tall envelope preserves the lock shackle or medal-and-ribbon stack.
- Full QA: **fail**.

## Construction and omissions

Lucide star original and atomic-debug: alternating points and valleys with a common vertical axis.

No defining component omitted.

## Visual review

Both themes/native48: crisp star retained after rejecting a rounded attempt that resembled a flower. Star arm and ribbon-spacing notes are resolved, but the larger star crowds the medal. Bilateral geometry preserved; no visual approval for release.

## Validation

- mic [medal]: medal and star are 5.69814 apart on centerlines nearest (16.5218, 32.131)<->(19, 27); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
