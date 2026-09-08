"""A kitchen oven with three circular controls above its large door.

Keyshape SQUARE: centerline extremes recorded in build below.
Lucide smartphone informs quarter-circle enclosure corners. The source render supplies the three controls and shared door divider; no extra inset window is added.
Hosting (compose.py): plus invalid, heart invalid, check review.
"""

from ...keyshapes import Keyshape
from ._base import Container64


class KitchenOvenAppliance(Container64):
    icon_id = 'kitchen-oven-appliance'
    keyshape = Keyshape.SQUARE
    aliases = ('oven',)
    keywords = ('kitchen', 'oven', 'appliance')

    def build(self) -> None:
        # SQUARE centerline extremes: (2,2)-(62,62).
        self.add_line("top", (6,2), (58,2))
        self.add_arc("nw", (2,6), (6,2), radius_x=4)
        self.add_line("left-header", (2,24), (2,6))
        self.add_contour("header-left", "left-header", "nw")
        self.add_arc("ne", (58,2), (62,6), radius_x=4)
        self.add_line("right-header", (62,6), (62,24))
        self.add_contour("header-right", "ne", "right-header")
        self.add_line("divider", (2,24), (62,24))
        self.add_line("right-door", (62,24), (62,58))
        self.add_arc("se", (62,58), (58,62), radius_x=4)
        self.add_line("bottom", (58,62), (6,62))
        self.add_arc("sw", (6,62), (2,58), radius_x=4)
        self.add_line("left-door", (2,58), (2,24))
        self.add_contour("door", "right-door", "se", "bottom", "sw", "left-door")
        for a,b in (("top","header-left"),("top","header-right"),("divider","header-left"),("divider","header-right"),("divider","door"),("door","header-left"),("door","header-right")):
            self.relate("connect",a,b)
        for x in (18,32,46):
            name=f"knob-{x}"
            self.add_arc(name+"-upper",(x-3,13),(x+3,13),radius_x=3)
            self.add_arc(name+"-lower",(x+3,13),(x-3,13),radius_x=3)
            self.add_contour(name,name+"-upper",name+"-lower",closed=True)
