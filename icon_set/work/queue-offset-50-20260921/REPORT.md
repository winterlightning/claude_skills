# Generation queue, offset 50

Processed the fixed 10-item batch captured in [queue.json](queue.json), using `$icon-solo-distilled`. All references were rechecked as TODO in the local gallery database before authoring, rendered, and visually inspected. All ten are standalone subjects or natural scenes; no container or side combinations were found. No component briefs required saving.

The requested `python icon_set/scripts/generation_queue.py --offset 50` failed because `python` resolves to an older interpreter. Python 3 was blocked from localhost by the sandbox, and no browser was available. The same repository `generation_queue` function was called read-only against the local gallery catalog and current database, with family=solo, offset=50, limit=10. The captured queue had 266 TODO references.

Original source UUIDs, source paths and saved editorial briefs were retained. The bread and collision originals already existed as excluded drafts; these were revised and promoted instead of duplicated. Author: `gpt-6` (already used in the repository).

## Icons

| Icon | Keyshape and subject | Simplification | References and visual findings |
| --- | --- | --- | --- |
| [knife-buttering-bread](../../../icon_set/model/icons/solo/knife_buttering_bread_f9a5cfd4_e289_4257_90a9_77f15fa702fa.py) | SQUARE: Toast and diagonal butter knife | Wide rounded blade replaces the narrow blade; separate butter dab omitted after trial placements crowded the blade or bread. | Source defines bread and spreading gesture; no useful direct Lucide match. Readable bread and broad spreading knife; simplified buttering cue. |
| [paired-grain-stalks](../../../icon_set/model/icons/solo/paired_grain_stalks_8a02fc5d_81a6_4f72_8628_2ea73f78a5b6.py) | SQUARE: Two staggered wheat stalks | Open paired grain strokes replace dense overlapping closed leaves. | Source defines paired stagger; Lucide wheat informs axial repetition. Two balanced stalks; clear separated branches. |
| [oval-brooch-with-extended-pin](../../../icon_set/model/icons/solo/oval_brooch_with_extended_pin_da8e4b4b_2941_4694_9449_49cdee922e25.py) | HRECT_M: Oval brooch and extended pin | Plain gem and clasp retained without extra ornament. | Source defines oval face and fastening; Lucide pin informs simple shaft. Clear oval ornament, central gem and attached clasp. |
| [two-level-bus-in-profile](../../../icon_set/model/icons/solo/two_level_bus_in_profile_c3f4b56e_b7d9_4000_bb93_f157d62f206a.py) | HRECT_L: Double-decker bus in profile | One mullion per tier; wheel centres moved inward for clearance from body sides. | Source defines two storeys; Lucide bus informs wheel joins and sparse glazing. Two window tiers and paired wheels remain legible. |
| [tall-bus-front](../../../icon_set/model/icons/solo/tall_bus_front_3c79c18d_55d6_4dfc_9ecf_737c14cf9a32.py) | VRECT_L: Tall bus front | Roof slot becomes upper glazing; short tyre stubs and lamps retained. | Source defines tall face; Lucide bus-front informs glazing and attached tyres. Symmetrical front; separated lamps and two glazing bands. |
| [two-door-rounded-cabinet](../../../icon_set/model/icons/solo/two_door_rounded_cabinet_051c846c_5b40_442b_9abd_c400bc170236.py) | SQUARE: Double-door cabinet | Wider proportion provides room for seam and two handles. | Source defines doors and handles; Lucide bus-front informs rounded shell construction; no direct cabinet match. Matching doors and handles, clear negative space. |
| [rounded-digital-camera-body](../../../icon_set/model/icons/solo/rounded_digital_camera_body_616d422f_12d3_43a6_93e6_1f80b251ffe7.py) | HRECT_L: Rounded digital camera | Plain shell and one lens; no added buttons. | Source defines body and lens; Lucide camera informs continuous shell and simple lens. Recognizable camera; clear lens opening. |
| [raised-top-photo-camera](../../../icon_set/model/icons/solo/raised_top_photo_camera_c489d854_1f8e_43c0_9352_5f289afbebf9.py) | HRECT_L: Raised-top photo camera | Broader shoulders and larger lens distinguish this source. | Source defines raised housing; Lucide camera informs shell and lens. Recognizable camera with balanced larger lens. |
| [backward-cap-above-sunglasses](../../../icon_set/model/icons/solo/backward_cap_above_sunglasses_264814f3_8ffa_45e9_be4e_00194dae68c2.py) | SQUARE: Backward cap above sunglasses | Tiny top button omitted; rear opening and joined lenses retained. | Source defines accessory arrangement; Lucide hat-glasses and glasses inform spacing and bridge. Cap opening and both lenses remain open at native size. |
| [car-broken-beneath-impact-burst](../../../icon_set/model/icons/solo/car_broken_beneath_impact_burst_757187c1_fd16_4577_8bb6_b25ad4df2330.py) | HRECT_L: Broken car beneath impact burst | Reduced burst points; wheels integrated as semicircular lower contours to avoid crowded overlapping wheel loops. | Source defines physical crash scene; Lucide bus informs sparse wheel construction. Two separated vehicle halves and impact burst remain identifiable. |

## Verification

Every final original passes `validate_icon()` with status `valid` and zero warnings. Every final original also passes `inspect_icon()` with no errors or warnings, including holes/pinches and internal-spacing review. See [validation.json](validation.json).

The first targeted build exported eight icons and exposed wheel-to-body internal-spacing findings in the bus profile and collision scene. Moving the bus wheels inward and integrating the crash wheels into the outlines resolved those checks. A subsequent targeted build covers only these two repaired originals. No profile rules, validation tolerances or exported SVG geometry were patched.

Model renders were inspected at 48 pixels in both themes using the repository contact-sheet renderer: [light](contact-light.png), [dark](contact-dark.png). Source evidence: [enlarged references](references.png), [native references](references-native.png), [Lucide references](lucide.png).

Final result: **10 generated icons, 0 prepared combinations, 0 unresolved failures.** The repaired targeted build exited successfully. All ten exports were verified in `published/solo48/manifest.json` with zero errors and warnings; each SVG exactly matches its Python original. All ten source UUIDs are now linked as `generated` in the gallery catalog and none remains in the failed manifest. See [export-verification.json](export-verification.json).

Actual exported SVGs were rendered and visually inspected at 48 pixels and enlarged in both themes: [light exports](exports-light.png), [dark exports](exports-dark.png). The wheel repairs retain the bus and collision subjects while clearing the flagged tight joins.

The initial interpreter/network errors and build-lock contention were recovered. No component saves were attempted or required, and there are no unsaved component fields. Saved editorial records and reference artwork remain unchanged. No commit or full-library validation was performed; the targeted build reused all unrelated outputs.
