# Unresolved glyph references

These sources remain TODO; no new original or combination classification was created.

## Email Bomb Attack — f52d2ec1-9555-4994-817d-73a093488f5a
Source: `pictographic-primitives/crime/data attacking e mail_f52d2ec1-9555-4994-817d-73a093488f5a.svg`

Retain the round bomb, upper-left fuse/ignition burst, and exact `@` character centered in the body. Reuse preferred glyph `symbol-at` from `icon_set/typeface/glyphs.json`; do not redraw it. The current catalog glyph has centerline bounds 6 × 20 and fractional endpoints. A compliant integrated 48px layout was not established; glyph geometry/spacing is unresolved. This is not a claim that no layout could ever work.

## Ancient Runic Symbols — 1837ed86-65ba-5a7c-9d4a-bcb9c0b8972e
Source: `pictographic-primitives/culture/batch-01/history caveman symbols_1837ed86-65ba-5a7c-9d4a-bcb9c0b8972e.svg`

The reference has three runic-looking marks: a tall left stave with two rising branches, a central loop/crossing mark, and a right angular arch. Their exact character identities are uncertain. The reusable catalog contains no Runic Unicode glyphs. Identify the characters and supply reusable glyphs before authoring; do not substitute Latin letters or invent runes.

The invoked skill says: “Missing character: report it and leave that part unresolved.” Its typeface rule says: “Any actual letters, words, digits or numbers, alone or inside another icon, reuse existing glyphs. Never draw, trace or redraw letterforms.”

Glyph-fit diagnostics: tested unchanged symbol-at paths at centerline heights 12, 20 and 28 inside a generous 40-unit-diameter circular enclosure. All three returned invalid (25 errors, zero warnings); evidence is in at-glyph-fit-probes.json. These are layout probes, not generated bomb originals.
