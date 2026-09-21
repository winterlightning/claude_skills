# Humans

Before drawing any person, render and inspect `icon_set/references/human_ref/user.svg` (bust: circular outlined head, broad smooth shoulders, short rounded sides, open bottom) and/or `full_body_ref.png` (full body: circular head, round-ended limbs, minimal anatomy; pick the nearest pose). These override Lucide and older generated humans. Reuse shared head radii and body parameters across the set at the same scale. Never copy fractional coordinates or scale between families.

**Stick-figure head placement.** Find the torso axis from hip through shoulder/neck (for a bent torso, the upper torso's direction at the neck). Put the head centre on that axis beyond the shoulder. Never use an arm, hand or the canvas vertical as the axis. Keep the head close to its own shoulders at the exact gap below, measured at the torso/neck junction; an arm passing nearer does not count, and raising an arm to manufacture the gap is wrong. Solve alignment and clearance together; do not slide the head away to clear an arm or fit the keyshape. A slightly larger head and smoother upper torso often fix a floating-head look. Depart from the axis only for a reference-supported neck bend.

After each stick figure:
```python
self.mark_human_figure("person", head="head", torso="torso", torso_junction="start")
```
Unique figure id per person. `head` = head outline primitive or contour. `torso` = the actual upper torso primitive (segment nearest the neck), never an arm or whole body. `torso_junction` = which end is the neck. Targets recorded: centerline gap 8, ink gap 4, measured from the head outline (e.g. head contour bottom y=14, torso start y=22). Flags do not move geometry, waive MIC or create a connection. Not for avatars with touching ink.

**Detached head, all non-avatar humans:** exactly 4 units visible ink gap to its own body = 8 between centerlines. Frontal bust: `body_top = head_cy + head_radius + 4 + 4`. Tilted poses: shortest gap. For a circular head of radius r, `distance(head_center, torso_junction) = r + 8` when that junction is the nearest body point; verify nothing else is closer. Never add a neck or a false `connect` to bypass it. Do not widen to 5+ to silence a curved-distance warning; use certifiable geometry or report the unresolved `review`. A diagonal gap may stay `review` even when analytically exact (approved example: `football-player-approaching-ball`, head (29,11) r5, junction (24,23), distance 13 = 5 + 8). Report visual approval, the analytical calculation and the checker status separately.

**Avatars (icon-avatar, solo family):** head ink touches body ink, zero gap, 4 between centerlines, declared with a scoped `connect` on the touching paths. Face and jaw are circular arcs with equal radii, never ovals. A bust in another category may set `human_construction = "bust"` for the same rule. Curved shoulder contact is accepted only when jaw and shoulder arcs have aligned vertical extrema exactly 4 apart and a direct `connect`.

**Review.** Record reference paths and shared head/body parameters in the module. Confirm the emitted gap, not a named constant. Compare with the reference at native size both themes. Check head shape, relative size, limb construction, and torso-axis alignment.
