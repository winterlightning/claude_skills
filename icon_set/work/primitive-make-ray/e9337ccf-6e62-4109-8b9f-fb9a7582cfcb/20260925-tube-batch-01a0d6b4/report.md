# woman-in-rounded-cap

The rounded cap, curved visor, flipped hair and V neckline follow the source instead of the previous fedora and scarf. Exact detached head/body spacing is analytically four ink units; automated curved-distance certification remains review.

- Concept: detective woman
- Source UUID: `e9337ccf-6e62-4109-8b9f-fb9a7582cfcb`
- Source: `pictographic-primitives/avatars/detective woman_e9337ccf-6e62-4109-8b9f-fb9a7582cfcb.svg`
- Author: gpt-6
- Keyshape: VRECT_L; visible ink [6, 2, 42, 46]. Upright rectangle contains the cap, lower face, hair and V-neck bust.
- Validation: **review**. Full QA: **review**. Acceptance: **user-approved-exception**.

Construction references: Lucide hat-glasses: separate crown and brim construction; human_ref/user.svg owns round jaw and shoulder vocabulary. Relevant local Lucide originals and atomic-debug geometry were inspected before authoring.

Simplifications: Upper visor seam omitted; small closed hair wedges reduced to open curved flips.

Human review: {"reference": "icon_set/references/human_ref/user.svg", "jaw_center": [24, 18], "jaw_radius": 12, "body_nearest_points": [[12, 34], [36, 34]], "head_to_body_ink_gap": 4, "proof": "sqrt(12^2+16^2)-12-4=4. Nearest jaw points are (16.8,27.6) and (31.2,27.6). Shoulder curves approach these endpoints from outside the offset circle; each collar line moves away from it. The checker reports review for the curved pair, not a strict pass."}

Exception: The exact four-unit head/body ink gap is proved analytically, but the checker cannot certify the diagonal arc/shoulder minimum. jaw/left-shoulder curved-distance review; reported 8.00043 centerline distance. Raw validation remains unchanged.

[SVG](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/e9337ccf-6e62-4109-8b9f-fb9a7582cfcb/20260925-tube-batch-01a0d6b4/woman-in-rounded-cap.svg) · [Python](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/e9337ccf-6e62-4109-8b9f-fb9a7582cfcb/20260925-tube-batch-01a0d6b4/woman_in_rounded_cap_e9337ccf_6e62_4109_8b9f_fb9a7582cfcb.py) · [Full QA](/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-make-ray/e9337ccf-6e62-4109-8b9f-fb9a7582cfcb/20260925-tube-batch-01a0d6b4/qa.json)
