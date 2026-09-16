---
name: icon-propose
description: Propose new standalone icon concepts for a category, audit existing names and coverage, and write drawing briefs for the Pictographic concept dictionary. Use for expanding icon ideas or asking what to draw next; this skill plans concepts rather than generating artwork.
---

# Icon Propose

Expand a category with distinct, useful **solo primitives**: independently recognizable subjects that can read at 48 × 48. Deliver concepts another agent can draw, grounded in the current library rather than only in the category name.

## Establish scope

Use the requested category, quantity, exclusions, and output destination. Infer a category from the active dictionary or supplied gallery URL when clear. If the user asks for “more,” extend the existing proposals without repeating them. When no quantity is given, aim for about 20 worthwhile additions; prefer a smaller strong set to padding the list.

Find the Pictographic repository in the current workspace or supplied path. It contains `icon_set/` and usually `pictographic-primitives/`. Do not hard-code one machine's absolute path. If no library is available, still propose concepts but clearly say that existing coverage could not be checked.

## Inspect coverage before choosing ideas

Relevant repository data:

- `icon_set/dist/gallery/primitives.json`: source `rows`, including category, concept, original label, UUID, path, and generated model links.
- `icon_set/dist/gallery/icons.json`: published and failed models. A published model is not necessarily approved or suitable for the solo family.
- `icon_set/model/icons/`: unbuilt models may exist here too.
- `icon_set/scripts/templates/concept-dictionary.json`: existing curated concepts and aliases. Read this before adding any proposal.

Use the read-only helper from this skill folder:

```bash
python3 scripts/audit_concepts.py --repo /path/to/repository --category websites
python3 scripts/audit_concepts.py --repo /path/to/repository --category websites --terms "security token" "passkey" "USB key"
```

Resolve `scripts/audit_concepts.py` against the skill's actual directory. The helper summarizes category names and searches **all categories**, proposals, aliases, model names, and model filenames. Search synonyms, spelling variants, and broader nouns as well as exact proposed names. Missing catalogs are reported as unavailable, not as proof of a gap. Name searches are candidates for inspection, not proof of visual identity or absence.

Inspect source SVGs visually when deciding to reuse a drawing, extract a subject, or identify a combination. Use the actual reference path or source URL; do not infer its geometry from a label. Existing names can describe intended use incorrectly: the Websites source labeled “performance metrics,” for example, depicts a browser frame.

## Find meaningful expansion

Think through several useful themes within the chosen category before listing objects. For Websites these could include discovery, privacy, accessibility, publishing, performance, archives, and infrastructure. For another category, choose themes that fit it rather than reusing the Websites themes.

For each candidate, ask:

- What single subject will be drawn, and what makes its silhouette recognizable?
- What category need does it serve? Prefer direct relevance and familiar metaphors. Label exploratory metaphors explicitly; do not fill a quota with obscure hardware or strained associations.
- Is this a new subject, an existing reusable concept, or only an alias/style/state variation?
- Will the defining features survive at 48 pixels without text, labels, or a scene?

Count **new drawing proposals** separately from reuse candidates. An existing Cookie can supply a tracking alias, but it is not a new drawing. A distinct complete subject extracted from a larger reference can be proposed, with the related source and extraction rationale recorded. A no-match name search means “no match found in the checked names,” not “this icon does not exist.”

## One icon, multiple categories

**One canonical icon may belong to multiple categories for reuse.** Category membership is many-to-many: a category can contain many icons, and an icon can serve many categories while keeping one identity and one drawing.

- Assign a **primary category** based on the subject itself, plus **related categories** where it has a useful direct application or established metaphor. Primary category is an organizational home, not a restriction on reuse.
- Search existing icons and ungenerated proposals globally before adding a subject. Reuse the canonical name, identity, and drawing brief when the visual subject is the same; add category associations and context-specific aliases instead of another drawing task.
- For example, Hair claw can belong to Accessories and Beauty; Cookie to Food and Websites. Ring mandrel belongs primarily to Tools and can also be discoverable in Accessories for jewelry fitting.
- Count a new canonical subject once across the library. Adding another category to an existing icon is **category reuse**, and adding a category to an existing ungenerated proposal is **a reference to that pending proposal**. Neither increases the new-drawing count.
- Report new drawing proposals and category-reuse opportunities separately. An item need not be exclusive to the requested category to be useful there, but explain its relevance and avoid weak associations.
- Keep the icon's family unchanged when adding categories. Shared use alone does not require a new variant, model file, source UUID, or generation task.

When presenting proposals, include the primary and related categories. Follow the dictionary's current storage capabilities in the linked reference; do not imply the page implements category associations it does not yet support.

## Keep the solo boundary

A solo primitive is one natural subject: object, animal, person, tool, device, or other independently recognizable noun. Attached functional parts belong to their object; a head and its own body are one subject.

Keep these out of a solo proposal list:

- Empty browser windows, cards, screens, bubbles, and other enclosures intended to hold independent content: container candidates.
- Operators, arrows, state marks, and small accessory glyphs: sub candidates.
- A noun plus an independently meaningful badge, arrow, checkmark, lock, or other modifier: a composition, not a new solo subject.
- Multiple independently meaningful objects arranged as a scene.
- A shape that relies on lettering or numbers to communicate its identity.

Do not turn a browser-plus-checkmark into a solo proposal by calling it “Verified website.” Propose the standalone subject if useful and leave the composition out. When a boundary is uncertain, describe the uncertainty and choose a clearer subject rather than silently changing family.

## Write a useful entry

Use a short canonical noun phrase, normally 1–4 words. Add a qualifier when it distinguishes the subject. Keep category prefixes, UUIDs, versions, and generic suffixes such as “icon” out of display names.

Separate:

- **Name:** what is drawn, such as “Tally counter.”
- **Meaning:** its intended category use; identify a metaphor where applicable.
- **Aliases:** likely searches, synonyms, and use contexts.
- **Categories:** one primary category and any useful related categories; identify an existing canonical icon or pending proposal when reusing it.
- **Drawing brief:** one complete subject, its silhouette, orientation when important, and the few defining integrated details. Mention exclusions only when they prevent a likely composition mistake.
- **Rationale:** the coverage gap, distinction from related artwork, and any visual uncertainty.
- **Priority:** start with broadly useful, recognizable subjects; place niche or exploratory ones later.

Avoid arbitrary geometry, new construction rules, or claims that a proposal is already generated or validated. Do not produce SVGs or start generation unless the user also asks for artwork; then use the repository's appropriate authoring skill if available.

## Deliver and preserve the draft boundary

For a normal brainstorming request, return the requested format or a concise concept list with drawing briefs. If the user is extending the existing dictionary, append the entries using [references/dictionary.md](references/dictionary.md). Do not rebuild the website just to add concepts.

The current Pictographic dictionary is an **unlisted local draft**. Preserve that state: no main-app navigation links, normal gallery-build inclusion, deployment, or generation queue writes unless the user explicitly requests that additional step. An unlisted URL is not access control; do not call it a private page.

Before finishing, check that additions have distinct subjects and IDs, counts reflect newly added proposals, known reuse is not mislabeled as a gap, and any dictionary preview matches the source data. Summarize how many new proposals were added, highlight a few strongest ones, and link the requested output.
