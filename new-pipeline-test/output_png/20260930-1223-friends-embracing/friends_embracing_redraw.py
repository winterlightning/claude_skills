"""friends-embracing (redraw of the new-pipeline traced SVG).

Plan: two stick-figure friends side by side on HRECT_L (centerline box
(4,8)-(44,40)), each with its outer arm hanging out and its inner arm reaching
across towards the other, the left arm above and the right arm below so the
two arms pass each other like a shoulder hug.
- heads: 4-cardinal-arc circles r5 at y=13 (top extreme 8), centres x=14/34
  mirrored about x=24; outlines 10 apart.
- torsos: vertical, split at the shoulder into a short neck (flagged torso,
  start junction 8 below the head outline) and a body down to y=40.
- shoulders: left at y=28, right at y=30 (the lower arm belongs to the right
  friend); outer arms fall to the left/right extremes x=4 / x=44.
- inner arms: parallel 3:1 slopes; left rises to (26,24), right falls to
  (22,34); each tip stops 8 short of the partner's torso and >8 from the
  partner's head, and the two arms stay 8.2 apart.
Reference: icon_set/references/human_ref/full_body_ref.png (circular heads,
round-ended single-stroke limbs, detached head 4 ink units above the body);
Lucide `users` / `user` for the circle-head vocabulary.

Metric issues fixed:
- stroke-width: redrawn at stroke 4, every gap re-budgeted at 8 centerline.
- keyshape-short-axis: outer hands now reach x=4 and x=44, heads y=8,
  torsos y=40, so HRECT_L fits exactly.
- clearance e0/e1 (heads 6.4): heads now 10 apart.
- clearance heads vs arms/torsos (e0-e2, e0-e4, e1-e2, e1-e3, e1-e5 ...):
  arms start at a shoulder below an 8-unit neck gap and slope away from
  both heads; every head/limb pair is >= 8.
- clearance e2/e3 (arms overlapping): arm tips pass each other 8.2 apart.
- t-junction e5/e3 gap 1.02 and the loose torso tops: torsos and arms now
  share an exact shoulder node and are declared connected.
- holes 4.3 inscribed: head radius 5 gives a 6-unit inner hole.
- human head gap (e1 at 2.67): both heads flagged, exactly 8 on centerlines.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "9879b825-1a99-4cc8-b5d3-ebca82cb7300"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1223-friends-embracing/"
    "friends-embracing_raw.svg"
)
AUTHOR = "claude-opus-5-5"

HEAD_R = 5
HEAD_Y = 13
NECK_Y = HEAD_Y + HEAD_R + 8          # 26: 8 on centerlines, 4 ink
BOTTOM = 40
# (x, shoulder_y, inner-arm tip, outer hand)
FIGURES = {
    "left": (14, 28, (26, 24), (4, 36)),
    "right": (34, 30, (22, 34), (44, 38)),
}


class FriendsEmbracingRedraw(Solo48):
    icon_id = "friends-embracing-redraw"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people"
    aliases = ("friends hugging", "shoulder hug", "friendship")
    keywords = ("friends", "embrace", "hug", "people", "friendship", "together", "buddies")

    def _head(self, name: str, cx: int, cy: int, r: int) -> None:
        pts = [(cx, cy - r), (cx + r, cy), (cx, cy + r), (cx - r, cy)]
        ids = []
        for i in range(4):
            aid = f"{name}-{i + 1}"
            self.add_arc(aid, pts[i], pts[(i + 1) % 4], radius_x=r, sweep=True)
            ids.append(aid)
        self.add_contour(name, *ids, closed=True)

    def build(self) -> None:
        for side, (x, sy, tip, hand) in FIGURES.items():
            head, neck, body = f"{side}-head", f"{side}-neck", f"{side}-body"
            inner, outer = f"{side}-inner-arm", f"{side}-outer-arm"
            shoulder = (x, sy)
            self._head(head, x, HEAD_Y, HEAD_R)
            self.add_line(neck, (x, NECK_Y), shoulder)
            self.add_line(body, shoulder, (x, BOTTOM))
            self.add_line(inner, shoulder, tip)
            self.add_line(outer, shoulder, hand)
            for a, b in ((neck, body), (neck, inner), (neck, outer),
                         (body, inner), (body, outer), (inner, outer)):
                self.relate("connect", a, b)
            self.mark_human_figure(side, head=head, torso=neck, torso_junction="start")
