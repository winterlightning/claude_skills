"""astronomy-telescope-stars (redraw of the new-pipeline traced SVG).

Plan: refracting telescope on a tripod aimed at one star, SQUARE
(centerline box (6,6)-(42,42)).
- tube: one closed parallelogram along D=(2,-1) with thickness N=(4,8)
  (8.9 on centerlines); the upper-left corner is the left extreme. The lower
  wall is split at the pivot node so the tripod shares it.
- tripod: three straight legs from the pivot node on the tube's lower wall,
  feet on the bottom extreme spaced 8 apart; the centre leg is vertical.
- star: hollow four-point star, four concave integer-radius arcs between the
  tips; its top and right tips are the top and right extremes.
Reference: Lucide `telescope` (tilted tube with the stand hung from one
shared node on its lower wall); the generated PNG for the tube angle and star
placement.

Metric issues:
- clearance e0/e2, e0/e7 (star vs tube and its end ellipse): fixed, the star
  sits 8+ from the tube corner and the eye-end ellipses are dropped.
- clearance e2/e3/e4/e5/e6 vs e1 and the 1.71 hole (the tiny pivot ring):
  fixed, the ring is dropped and the legs share one node on the tube wall.
- e3/e8 (lens-end ellipse slivers): dropped, the tube is one closed outline.
- stroke-count (9 vs 6): fixed, 3 outlines/parts (tube, tripod, star).
- keyshape-short-axis (x fill 99%): fixed, extremes sit exactly on 6 and 42.
- stroke-width info: redrawn at stroke 4 with gaps budgeted at 8.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "4a8d494e-32cc-4073-96a3-0c1ca2d67952"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260928-1658-astronomy-telescope-stars/"
    "astronomy-telescope-stars_raw.svg"
)
AUTHOR = "claude-opus-5-5"

D = (2, -1)              # tube axis (up to the right)
N = (4, 8)               # tube thickness, perpendicular to D
TUBE_T = 8               # tube length in D steps
PIVOT_T = 6              # pivot node position along the lower wall
LOWER_LEFT = (10, 35)
FOOT_Y = 42
FOOT_DX = 8              # feet spacing
STAR_C = (35, 13)
STAR_R = 7               # tip distance from the star centre
STAR_ARC = 15            # concave arc radius between tips


def _along(p, t):
    return (p[0] + D[0] * t, p[1] + D[1] * t)


class AstronomyTelescopeStarsRedraw(Solo48):
    icon_id = "astronomy-telescope-stars-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "science"
    aliases = ("telescope", "stargazing", "astronomy")
    keywords = ("astronomy", "telescope", "star", "stargazing", "space", "tripod", "observatory")

    def build(self) -> None:
        ll = LOWER_LEFT
        lr = _along(ll, TUBE_T)
        pivot = _along(ll, PIVOT_T)
        ul = (ll[0] - N[0], ll[1] - N[1])
        ur = (lr[0] - N[0], lr[1] - N[1])
        self.add_line("tube-bottom-left", ll, pivot)
        self.add_line("tube-bottom-right", pivot, lr)
        self.add_line("tube-front", lr, ur)
        self.add_line("tube-top", ur, ul)
        self.add_line("tube-back", ul, ll)
        self.add_contour("tube", "tube-bottom-left", "tube-bottom-right",
                         "tube-front", "tube-top", "tube-back", closed=True)

        px = pivot[0]
        for name, fx in (("leg-left", px - FOOT_DX), ("leg-centre", px), ("leg-right", px + FOOT_DX)):
            self.add_line(name, pivot, (fx, FOOT_Y))
            self.relate("connect", name, "tube-bottom-left")
            self.relate("connect", name, "tube-bottom-right")
        self.relate("connect", "leg-left", "leg-centre")
        self.relate("connect", "leg-centre", "leg-right")
        self.relate("connect", "leg-left", "leg-right")

        cx, cy, r = STAR_C[0], STAR_C[1], STAR_R
        tips = [(cx, cy - r), (cx + r, cy), (cx, cy + r), (cx - r, cy)]
        members = []
        for i, (a, b) in enumerate(zip(tips, tips[1:] + tips[:1])):
            self.add_arc(f"star-{i + 1}", a, b, radius_x=STAR_ARC, sweep=False)
            members.append(f"star-{i + 1}")
        self.add_contour("star", *members, closed=True)
