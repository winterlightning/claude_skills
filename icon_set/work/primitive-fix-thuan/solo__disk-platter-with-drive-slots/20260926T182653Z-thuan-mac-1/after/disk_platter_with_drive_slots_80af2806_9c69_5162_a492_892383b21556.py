"""Disk platter with drive slots: a round disk reel -- an outer rim, a central hub
ring and three windows opened between hub and rim.

Revision (disapproved, reason not recorded): the rejected drawing was a circle
with a centre dot and three short straight dashes, which reads as an electrical
wall socket; the original is a reel with a hub circle and three windows set
round it between hub and rim. The hub is a ring again and the three windows are
curved slots following the reel's circle, 120 degrees apart.

Symbol plan: rim radius 20 about (24,24) (CIRCLE keyshape). Hub: radius-3 ring
about the centre (small-circle exception). Windows: three slots, each one cubic
bending round the centre at radius 11-11.7 (8+ from the hub, 8+ from the rim),
with integer ends on 5-10 / 6-10 / 11-1 offsets: top (19,14)-(29,14), right
(35,25)-(30,34), left (18,34)-(13,25); controls lie on the circle's tangents.
A spoked variant (attempts/spokes-attempt.*) read as a steering wheel.
Omissions: the windows' trapezoid outlines (a closed window between hub and rim
needs about 22 units of radial room; the disk leaves 13), drawn as slots.
Lucide construction: 'disc' rim and hub.
Keyshape CIRCLE: rim radius 20.
"""
import math

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "80af2806-9c69-5162-a492-892383b21556"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__disk-platter-with-drive-slots/20260926T182653Z-thuan-mac-1/reference/floppy disk_80af2806-9c69-5162-a492-892383b21556.svg"
AUTHOR = "claude-opus-5-5"

C = 24


class DiskPlatterWithDriveSlots(Solo48):
    icon_id = "disk-platter-with-drive-slots"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "technology/storage"
    aliases = ("disk-reel", "floppy-disk", "platter")
    keywords = ("disk", "platter", "reel", "storage", "drive", "floppy", "hub")

    def slot(self, name, a, b):
        # Cubic approximating the circular arc about the centre from a to b.
        (ax, ay), (bx, by) = a, b
        ra, rb = math.hypot(ax - C, ay - C), math.hypot(bx - C, by - C)
        ta, tb = math.atan2(ay - C, ax - C), math.atan2(by - C, bx - C)
        sweep = (tb - ta + math.pi) % (2 * math.pi) - math.pi
        k = 4 / 3 * math.tan(sweep / 4)
        c1 = (ax - k * (ay - C), ay + k * (ax - C))
        c2 = (bx + k * (by - C), by - k * (bx - C))
        self.add_bezier(name, a, (tuple(round(v, 4) for v in c1), tuple(round(v, 4) for v in c2), b))

    def build(self) -> None:
        self.add_arc("rim-top", (C - 20, C), (C + 20, C), radius_x=20)
        self.add_arc("rim-bottom", (C + 20, C), (C - 20, C), radius_x=20)
        self.add_contour("rim", "rim-top", "rim-bottom", closed=True)
        r = 3
        self.add_arc("hub-a", (C - r, C), (C, C - r), radius_x=r)
        self.add_arc("hub-b", (C, C - r), (C + r, C), radius_x=r)
        self.add_arc("hub-c", (C + r, C), (C, C + r), radius_x=r)
        self.add_arc("hub-d", (C, C + r), (C - r, C), radius_x=r)
        self.add_contour("hub", "hub-a", "hub-b", "hub-c", "hub-d", closed=True)
        self.slot("window-top", (19, 14), (29, 14))
        self.slot("window-right", (35, 25), (30, 34))
        self.slot("window-left", (18, 34), (13, 25))
