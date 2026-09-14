"""A teardrop map pin with a dot and short stem. VRECT_L centerline extremes (8,6)-(40,42). Lucide map-pin informs the rounded cap and tapered point; preserve the source solid dot and attached stem. Bilateral symmetry with coherent elliptical shoulders."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7e254e98-4921-4444-a7ec-5db1643e078a'
SOURCE_PATH = 'pictographic-primitives/symbol/map pin_7e254e98-4921-4444-a7ec-5db1643e078a.svg'
AUTHOR = 'gpt-6'


class MapPinStem(Solo48):
    icon_id = 'map-pin-stem'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('map', 'pin', 'location', 'marker', 'place', 'gps', 'destination', 'point')

    def build(self) -> None:
        self.add_arc('cap',(8,16),(40,16),radius_x=16,radius_y=12)
        self.add_arc('right-turn',(40,16),(36,25),radius_x=20,radius_y=15)
        self.add_line('right-tip',(36,25),(24,37))
        self.add_line('left-tip',(24,37),(12,25))
        self.add_arc('left-turn',(12,25),(8,16),radius_x=20,radius_y=15)
        self.add_contour('pin','cap','right-turn','right-tip','left-tip','left-turn',closed=True)
        self.add_dot('center',(24,16))
        self.add_line('stem',(24,37),(24,42))
        self.relate('connect','pin','stem')
