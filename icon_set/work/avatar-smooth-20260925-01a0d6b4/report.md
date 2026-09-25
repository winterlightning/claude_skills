# Smooth avatar corrections

Both matching library originals are updated in place. Both pass strict vector validation and full release QA with zero warnings and no exceptions.

The rounded-cap avatar keeps the source cap, bob hair and V-neck clothing cue. The parted-hair avatar keeps its distinctive fringe and simple bust. Both use VRECT_L, visible ink (6,2)-(42,46), centered circular face arcs, tangent shoulder curves and open bottoms.

Head/body centerline separation is 4 units at x24, so the 4-unit strokes touch with **zero visible gap**. The cap jaw has center (24,16), radius 12; the parted-hair jaw has center (24,18), radius 10. Both reach y28 on centerline; the flat shoulder span is y32, derived from HEAD_BODY_CENTERLINE_GAP.

The extra visor seam, scarf tail and closed tiny hair wedges are removed. Hair ends use one smooth curve per side; the parted fringe has a smooth horizontal tangent at its center. The V collar remains as the cap portrait’s deliberate clothing cue.

Construction references: human_ref/user.svg for circular faces, broad shoulders and open bottoms; Lucide user-round original and atomic-debug geometry for circular arcs and coherent joins. Supplied originals govern headwear and hairstyle. These are standalone head-and-body subjects, not combinations.

[Full reference / before / after comparison](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/avatar-smooth-20260925-01a0d6b4/comparison.png)

- **detective-woman-1-avatar**: [original Python](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/detective_woman_1_avatar_e9337ccf_6e62_4109_8b9f_fb9a7582cfcb.py) · [SVG](/Applications/Workspaces/pictographic/claude_skills/published/solo48/detective-woman-1-avatar.svg) · [QA](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/avatar-smooth-20260925-01a0d6b4/e9337ccf-6e62-4109-8b9f-fb9a7582cfcb/qa.json)

Validation: targeted avatar construction test and profile/keyshape tests pass. The broader avatar suite still fails for unrelated existing avatars; see [full suite log](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/avatar-smooth-20260925-01a0d6b4/full-suite.log). The two revised avatars pass those avatar assertions independently. Targeted build and manifest/hash verification are recorded in completion.json.
- **female-user-profile**: [original Python](/Applications/Workspaces/pictographic/claude_skills/icon_set/model/icons/solo/female_user_profile_b7558322_6681_447e_8b8a_0f4a588a3f0e.py) · [SVG](/Applications/Workspaces/pictographic/claude_skills/published/solo48/female-user-profile.svg) · [QA](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/avatar-smooth-20260925-01a0d6b4/b7558322-6681-447e-8b8a-0f4a588a3f0e/qa.json)

Validation: targeted avatar construction test and profile/keyshape tests pass. The broader avatar suite still fails for unrelated existing avatars; see [full suite log](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/avatar-smooth-20260925-01a0d6b4/full-suite.log). The two revised avatars pass those avatar assertions independently. Targeted build and manifest/hash verification are recorded in completion.json.
