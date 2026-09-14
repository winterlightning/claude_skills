"""A location pin with a central ring. VRECT_L extremes (8,6)-(40,42). Lucide map-pin informs the smooth arched silhouette and round opening. Preserve the downward point and bilateral symmetry."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1e5a0bbe-23e3-46f7-9120-24bf44c26e95'
SOURCE_PATH = 'pictographic-primitives/symbol/location pin_1e5a0bbe-23e3-46f7-9120-24bf44c26e95.svg'
AUTHOR = 'gpt-6'


class LocationPinRing(Solo48):
    icon_id = 'location-pin-ring'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('location', 'pin', 'map', 'place', 'marker', 'gps', 'destination', 'address')

    def build(self) -> None:
        self.add_arc('cap',(8,18),(40,18),radius_x=16,radius_y=14)
        self.add_arc('right-turn',(40,18),(36,30),radius_x=20,radius_y=20)
        self.add_line('right-tip',(36,30),(24,42))
        self.add_line('left-tip',(24,42),(12,30))
        self.add_arc('left-turn',(12,30),(8,18),radius_x=20,radius_y=20)
        self.add_contour('pin','cap','right-turn','right-tip','left-tip','left-turn',closed=True)
        cx, cy, radius = 24, 18, 5
        self.add_arc('ring-top', (cx-radius, cy), (cx+radius, cy), radius_x=radius)
        self.add_arc('ring-bottom', (cx+radius, cy), (cx-radius, cy), radius_x=radius)
        self.add_contour('ring', 'ring-top', 'ring-bottom', closed=True)
