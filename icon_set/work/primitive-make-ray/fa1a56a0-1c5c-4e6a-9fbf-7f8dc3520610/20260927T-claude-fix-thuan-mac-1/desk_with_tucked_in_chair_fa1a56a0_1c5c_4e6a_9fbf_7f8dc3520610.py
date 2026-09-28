"""Desk with tucked-in chair: a desk seen from the front with a chair pushed in
under it -- the chair's rounded back shows above the desktop, its seat and legs
below.

Revision (disapproved, reason not recorded): in the rejected drawing the desktop
slab was only 8 high and the chair posts closed a box with the seat only 8 high,
so both counters pinched shut at 48 and the seat read as a drawer frame. The
original shows a thick desktop, a seat that overhangs its posts and splayed
chair legs. The slab and the box under it are now 10 high and the seat
overhangs the posts.

Symbol plan: mirror axis x=24. Chair back: radius-8 arch about (24,16) (top 8)
standing on the desktop. Desktop: slab (4,16)-(44,26) with radius-4 top corners;
the desk legs run on from its sides to the ground y=40. Chair: posts x=16/32 from
the slab down to the seat y=36; the seat (12,36)-(36,36) overhangs them; the legs
splay from the posts to (14,40)/(34,40).
Omissions: the seat's rounded cushion outline (a closed pill needs 10 units of
height).
Lucide construction: 'armchair'/'lamp-desk' style legs; rounded slab corners.
Keyshape HRECT_L: centerline x 4..44 (desk), y 8 (chair back) .. 40.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "fa1a56a0-1c5c-4e6a-9fbf-7f8dc3520610"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__desk-with-tucked-in-chair/20260926T182653Z-thuan-mac-1/reference/chair table_fa1a56a0-1c5c-4e6a-9fbf-7f8dc3520610.svg"
AUTHOR = "claude-opus-5-5"

TOP, FRONT, GROUND, SEAT = 16, 26, 40, 36


class DeskWithTuckedInChair(Solo48):
    icon_id = "desk-with-tucked-in-chair"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "office"
    aliases = ("chair-table", "desk-and-chair")
    keywords = ("desk", "chair", "table", "furniture", "office", "seat", "workstation")

    def build(self) -> None:
        self.add_line("top-a", (8, TOP), (16, TOP))
        self.add_line("top-b", (16, TOP), (32, TOP))
        self.add_line("top-c", (32, TOP), (40, TOP))
        self.add_arc("corner-right", (40, TOP), (44, TOP + 4), radius_x=4)
        self.add_line("side-right", (44, TOP + 4), (44, FRONT))
        self.add_line("front-a", (44, FRONT), (32, FRONT))
        self.add_line("front-b", (32, FRONT), (16, FRONT))
        self.add_line("front-c", (16, FRONT), (4, FRONT))
        self.add_line("side-left", (4, FRONT), (4, TOP + 4))
        self.add_arc("corner-left", (4, TOP + 4), (8, TOP), radius_x=4)
        self.add_contour("desktop", "top-a", "top-b", "top-c", "corner-right", "side-right",
                         "front-a", "front-b", "front-c", "side-left", "corner-left", closed=True)
        self.add_line("desk-leg-left", (4, FRONT), (4, GROUND))
        self.add_line("desk-leg-right", (44, FRONT), (44, GROUND))
        self.relate("connect", "desktop", "desk-leg-left")
        self.relate("connect", "desktop", "desk-leg-right")

        self.add_arc("chair-back", (16, TOP), (32, TOP), radius_x=8)
        self.relate("connect", "desktop", "chair-back")

        self.add_line("seat-left", (12, SEAT), (16, SEAT))
        self.add_line("seat-mid", (16, SEAT), (32, SEAT))
        self.add_line("seat-right", (32, SEAT), (36, SEAT))
        self.add_contour("seat", "seat-left", "seat-mid", "seat-right")
        for side, x, foot in (("left", 16, 14), ("right", 32, 34)):
            self.add_line(f"post-{side}", (x, FRONT), (x, SEAT))
            self.add_line(f"leg-{side}", (x, SEAT), (foot, GROUND))
            self.relate("connect", f"post-{side}", "desktop")
            self.relate("connect", f"post-{side}", "seat")
            self.relate("connect", f"leg-{side}", "seat")
            self.relate("connect", f"leg-{side}", f"post-{side}")
