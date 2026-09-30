"""couple-busts (redraw of the new-pipeline traced SVG).

Subject: two people shown as head-and-shoulders busts side by side, each a
hollow round head floating over an open-bottom shoulder arch.

Plan: HRECT_M (centerline box (4,10)-(44,38)), the suggested keyshape.
The two busts are one repeated definition, placed on the axes x 12 and 36
(mirrored about x 24).
- width budget: two shoulder arches 16 wide plus the 8 gap between them
  fill the 40 of the box exactly (2*16 + 8 = 40), so the outer shoulder ends
  are the x 4 / 44 extremes and the inner ends sit 8 apart (x 20 / 28).
- height budget: head r5 (10 tall, 6 inscribed hole) + 8 head gap + a 10 deep
  shoulder arch = 28, the full HRECT_M height: head tops y 10, shoulder ends
  y 38.
- head: circle r5 about (X,15) from two semicircle arcs.
- shoulders: a flat top on y 28 split at the axis (the neck node), r6
  corners, then short vertical ends down to y 38, like the traced arch but
  with the round Lucide `user` shoulders squared into a stable top so the
  head gap is straight-vs-arc over a level neck.
- each bust is flagged with mark_human_figure; the neck node (X,28) is
  exactly 8 on centerlines under the head bottom (X,20), 4 of visible ink.
References: icon_set/references/human_ref (round head over a shoulder
arch, detached 4-unit ink gap) and Lucide `users` (two busts side by side;
here both at equal size and level since the brief shows two equal busts).

Metric issues (couple-busts_metrics.json) and how they were handled:
- stroke-width (info, trace 2.67): redrawn at stroke 4; every gap budgeted.
- keyshape-short-axis (warn, HRECT_M y fill 67%): fixed; the head tops are
  on y 10 and the shoulder ends on y 38, so all four extremes are exact.
- clearance e0/e2 and e1/e3 (heads 2.3-2.5 above the shoulders) and
  head-gap e0: fixed; each head ends exactly 8 above its level neck node on
  the shared axis.
- clearance e2/e3 (the two shoulder arches 5.85 apart): fixed; the inner
  shoulder ends are parallel verticals exactly 8 apart.
- holes (5.95 / 5.8 inscribed): the heads are r5, inscribed 6.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "a76c7c2d-a4c9-4c4a-8eec-dac04079bf30"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1058-couple-busts/couple-busts_raw.svg"
AUTHOR = "claude-opus-5-5"

AXES = (12, 36)          # bust axes, mirrored about x 24
HEAD_R = 5
HEAD_CY = 15             # head y 10..20
NECK_Y = HEAD_CY + HEAD_R + 8   # 28: exactly 8 under the head outline
HALF_W = 8               # shoulders 16 wide; inner ends 8 apart
CORNER = 6               # shoulder corner radius
BASE_Y = 38              # open shoulder ends on the box bottom


class CoupleBustsRedraw(Solo48):
    icon_id = "couple-busts-redraw"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/couple"
    aliases = ("couple", "two people", "users", "pair", "partners")
    keywords = ("couple", "people", "users", "busts", "two persons", "team", "friends", "partners")

    def _bust(self, name: str, x: int) -> None:
        r, cy = HEAD_R, HEAD_CY
        self.add_arc(f"{name}-head-top", (x - r, cy), (x + r, cy), radius_x=r, sweep=True)
        self.add_arc(f"{name}-head-bottom", (x + r, cy), (x - r, cy), radius_x=r, sweep=True)
        self.add_contour(f"{name}-head", f"{name}-head-top", f"{name}-head-bottom", closed=True)

        w, k, n, b = HALF_W, CORNER, NECK_Y, BASE_Y
        self.add_line(f"{name}-side-l", (x - w, b), (x - w, n + k))
        self.add_arc(f"{name}-corner-l", (x - w, n + k), (x - w + k, n), radius_x=k, sweep=True)
        self.add_line(f"{name}-top-l", (x - w + k, n), (x, n))
        self.add_line(f"{name}-top-r", (x, n), (x + w - k, n))
        self.add_arc(f"{name}-corner-r", (x + w - k, n), (x + w, n + k), radius_x=k, sweep=True)
        self.add_line(f"{name}-side-r", (x + w, n + k), (x + w, b))
        self.add_contour(
            f"{name}-shoulders", f"{name}-side-l", f"{name}-corner-l", f"{name}-top-l",
            f"{name}-top-r", f"{name}-corner-r", f"{name}-side-r",
        )
        self.mark_human_figure(name, head=f"{name}-head", torso=f"{name}-top-r", torso_junction="start")

    def build(self) -> None:
        self._bust("left", AXES[0])
        self._bust("right", AXES[1])
