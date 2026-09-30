"""crested-penguin (redraw of the new-pipeline traced SVG).

Plan: a front-facing crested penguin mirrored about x=24 on VRECT_M
(centerline box (10,4)-(38,44)).
- silhouette (one closed contour): an r10 head dome centred (24,16), split
  at the crest roots (16,10)/(32,10); below the dome's waist (14,16) each
  side swells to the belly (10,32) and rounds into the base (24,44), with a
  knot at (13,40) where the flipper lands. Every join is tangent-continuous.
- crests: from each root one plume leaves the dome along its radius and
  curls out to finish level at the box corner (10,4)/(38,4), 8.4 clear of the dome at the
  tip -- the crested penguin's signature eyebrow plumes.
- flippers: an inner stroke per side, free at the top (19,29)/(29,29) and
  curving out to meet the lower wall at (13,40)/(35,40), as in the image.
- beak: a small closed triangle (22,19)-(26,19)-(24,22) on the axis; it
  paints as a solid wedge at 48 px.
Traced shape and PNG read for proportion only (dome head, pear body, inner
flipper strokes, plumes above the face). No useful Lucide match (Lucide has
no penguin or bird body in this pose).

Metric issues:
- stroke-width (info): redrawn at stroke 4 with every gap budgeted for it.
- stroke-count (warn, 8 vs 6): fixed; 6 parts (silhouette, 2 crests,
  2 flippers, beak).
- keyshape-short-axis (warn): fixed; the crest tips sit on x=10/x=38 and
  y=4, the base on y=44, so VRECT_M is filled on both axes.
- clearance errors between the dome, the traced crest arcs, the side
  flaps and the beak (e0-e5, e0-e7, e1-e2, e1-e3, e1-e4, e1-e5, e1-e7,
  e2-e3, e2-e4, e2-e5, e2-e7 ...): fixed; the four traced crest/flap strokes
  became two plumes rooted on the dome, and the beak moved down to sit
  8+ clear of the dome, the walls and the flipper tops.
- hole 2.55 wide at the top of the head (error): fixed; the traced crest
  loop over the dome is gone, the plumes enclose nothing.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "b013a26e-4b3d-4d2f-a975-ca81de5ad6ce"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1040-crested-penguin/"
    "crested-penguin_raw.svg"
)
AUTHOR = "claude-opus-5-5"

AXIS = 24
HEAD_R = 10
WAIST = (14, 16)        # dome's widest point, where the side wall begins
CREST_ROOT = (16, 10)   # on the dome, radius direction (-4,-3)
CREST_TIP = (10, 4)
BELLY = (10, 32)
FLIPPER_FOOT = (13, 40)
FLIPPER_TOP = (19, 29)
BASE = (24, 44)


def mirror(p):
    return (2 * AXIS - p[0], p[1])


def mirror_segs(segs):
    return tuple(tuple(mirror(q) for q in seg) for seg in segs)


class CrestedPenguinRedraw(Solo48):
    icon_id = "crested-penguin-redraw"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals/birds"
    aliases = ("rockhopper penguin", "macaroni penguin")
    keywords = ("penguin", "crested", "rockhopper", "bird", "antarctic", "animal", "wildlife")

    def build(self) -> None:
        side = ((14, 22), (10, 26), BELLY)
        hip = ((10, 35), (11, 38), FLIPPER_FOOT)
        base = ((15, 42), (19, 44), BASE)

        # Silhouette, walked clockwise from the left waist.
        self.add_arc("dome-l", WAIST, CREST_ROOT, radius_x=HEAD_R, sweep=True)
        self.add_arc("dome-top", CREST_ROOT, mirror(CREST_ROOT), radius_x=HEAD_R, sweep=True)
        self.add_arc("dome-r", mirror(CREST_ROOT), mirror(WAIST), radius_x=HEAD_R, sweep=True)
        self.add_bezier("side-r", mirror(WAIST), mirror_segs((side,))[0])
        self.add_bezier("hip-r", mirror(BELLY), mirror_segs((hip,))[0])
        self.add_bezier("base-r", mirror(FLIPPER_FOOT), mirror_segs((base,))[0])
        # Left half walked backwards from the base to the waist.
        self.add_bezier("base-l", BASE, ((19, 44), (15, 42), FLIPPER_FOOT))
        self.add_bezier("hip-l", FLIPPER_FOOT, ((11, 38), (10, 35), BELLY))
        self.add_bezier("side-l", BELLY, ((10, 26), (14, 22), WAIST))
        self.add_contour(
            "body", "dome-l", "dome-top", "dome-r", "side-r", "hip-r",
            "base-r", "base-l", "hip-l", "side-l", closed=True,
        )

        crest = ((13.6, 8.2), (13, 4), CREST_TIP)
        self.add_bezier("crest-l", CREST_ROOT, crest)
        self.add_bezier("crest-r", mirror(CREST_ROOT), mirror_segs((crest,))[0])

        flipper = ((19, 34), (17, 37), FLIPPER_FOOT)
        self.add_bezier("flipper-l", FLIPPER_TOP, flipper)
        self.add_bezier("flipper-r", mirror(FLIPPER_TOP), mirror_segs((flipper,))[0])

        self.add_polyline("beak", (22, 19), (26, 19), (24, 22), closed=True)

        for part in ("crest-l", "crest-r", "flipper-l", "flipper-r"):
            self.relate("connect", "body", part)
