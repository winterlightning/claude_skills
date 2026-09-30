"""home-cog (redraw of the new-pipeline traced SVG).

Plan: a gabled house with a six-tooth cog inside it, on SQUARE
(centerline box (6,6)-(42,42)), mirrored about x=24.
- house: one closed polyline, apex (24,6), eave corners (6,18) / (42,18),
  walls straight down to the floor at y=42. The walls are the keyshape's
  left/right extremes, the apex the top and the floor the bottom.
- cog: Lucide file-cog construction scaled to this grid: a ring of r5
  about (24,26) split at six integer roots on the 3-4-5 circle
  ((+-5,0), (+-3,+-4)), each root carrying a short knob tooth that ends on
  an integer point ((+-7,0), (+-4,+-6)). The (+-4,+-6) tips lean 3 deg off
  radial so the tips sit 56/67 deg apart instead of the roots' 53/74; the
  open ring is the cog's circular hole. Longer (+-9,0)/(+-5,+-7) stubs also
  validated but read as insect legs at 48 px, so the short knobs won.
Traced shape: home-cog_raw.svg / home-cog_fitted.svg (the house proportions
and the cog-in-house layout; no trace coordinates were reused).
Lucide: house (gable + straight walls) and file-cog / cog (ring with short
radial tooth stubs instead of an outlined tooth polygon).

Metric issues:
- keyshape-short-axis (SQUARE y fill 87%): fixed; the apex is at y=6 and the
  floor at y=42, so all four extremes sit on the box.
- clearance e0/e2 (walls+floor vs cog, 3.31): fixed; floor is 10 below the
  lowest tooth tips, walls are 11 from the side teeth.
- clearance e1/e2 (roof vs cog, 5.13): fixed; nearest upper tooth tips
  (20,20) / (28,20) are 9.4 from the roof lines.
- clearance e2/e3 (cog outline vs hole, 3.8): fixed by construction; the
  outlined-tooth cog and its separate hole circle are replaced by one ring
  whose interior is the hole, so there is no second part to crowd.
- holes 1.6-2.2 wide inside the cog (tooth slivers, hub gap): fixed; teeth
  are open stubs, and the only hole left is the ring interior, 6 inscribed.
- hole 4.12 at the roof apex (eave overhang pockets): fixed; the eave
  overhang stubs were dropped (the walls must sit on x=6/42 so the cog's
  side teeth keep 8 from them; stubs of 1 unit would not read).
- stroke-width 2.4 -> 4: info only; every gap above is measured at stroke 4.
Deliberate change: the source's separate hole circle inside an outlined
cog cannot fit at stroke 4 (hole r>=3.5 + 8 + teeth needs a ~28 wide cog,
leaving no 8-unit band to the walls), so the ring-and-stub cog carries
the hole.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "8e974970-0198-4484-85aa-47bb0a455f4b"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1517-home-cog/home-cog_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24
APEX_Y = 6
EAVE_Y = 18
FLOOR_Y = 42
WALL_DX = 18        # walls at AXIS -/+ 18

COG_Y = 26          # cog centre (AXIS, COG_Y)
RING_R = 5
# Tooth roots on the r5 ring (3-4-5 integer points) and their stub tips,
# counter-clockwise on screen starting at the right-hand tooth.
TEETH = (
    ((5, 0), (7, 0)),
    ((3, -4), (4, -6)),
    ((-3, -4), (-4, -6)),
    ((-5, 0), (-7, 0)),
    ((-3, 4), (-4, 6)),
    ((3, 4), (4, 6)),
)


def at(offset):
    return (AXIS + offset[0], COG_Y + offset[1])


class HomeCogRedraw(Solo48):
    icon_id = "home-cog-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "buildings/home"
    aliases = ("house-cog", "home-settings", "house-gear")
    keywords = ("home", "house", "cog", "gear", "settings", "smart home", "preferences")

    def build(self) -> None:
        wl, wr = AXIS - WALL_DX, AXIS + WALL_DX
        self.add_polyline(
            "house",
            (wl, FLOOR_Y), (wl, EAVE_Y), (AXIS, APEX_Y), (wr, EAVE_Y), (wr, FLOOR_Y),
            closed=True,
        )

        # Ring split at every tooth root so each stub shares an endpoint.
        roots = [at(root) for root, _ in TEETH]
        arcs = []
        for i, start in enumerate(roots):
            name = f"ring-{i}"
            self.add_arc(name, start, roots[(i + 1) % len(roots)], radius_x=RING_R, sweep=False)
            arcs.append(name)
        self.add_contour("ring", *arcs, closed=True)

        for i, (root, tip) in enumerate(TEETH):
            name = f"tooth-{i}"
            self.add_line(name, at(root), at(tip))
            self.relate("connect", name, "ring")
