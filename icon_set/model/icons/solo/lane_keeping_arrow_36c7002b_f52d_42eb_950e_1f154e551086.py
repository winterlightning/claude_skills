"""Lane Keeping Arrow, re-authored from its reference on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '36c7002b-f52d-42eb-950e-1f154e551086'
SOURCE_PATH = 'pictographic-primitives/transportation/lane departing prevent system_36c7002b-f52d-42eb-950e-1f154e551086.svg'
AUTHOR = 'gpt-6'

class LaneKeepingArrow(Solo48):
    icon_id = 'lane-keeping-arrow'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    aliases = ()
    keywords = ('lane assist', 'lane keeping', 'lane departure', 'road', 'arrow', 'driving', 'dashboard', 'safety')

    def build(self) -> None:
        # Current contract centerline extremes: (8,6)-(40,42).
        for x in (8,40):self.add_line(f'lane-{x}',(x,4),(x,44))
        self.add_polyline('arrowhead',(18,12),(24,6),(30,12))
        self.add_line('shaft-top',(24,6),(24,16))
        self.add_arc('wiggle-a',(24,16),(27,22),radius_x=3,radius_y=6,sweep=False)
        self.add_arc('wiggle-b',(27,22),(30,28),radius_x=3,radius_y=6)
        self.add_arc('wiggle-c',(30,28),(27,34),radius_x=3,radius_y=6)
        self.add_arc('wiggle-d',(27,34),(24,40),radius_x=3,radius_y=6,sweep=False)
        self.add_line('shaft-bottom',(24,40),(24,42))
        self.add_contour('shaft','shaft-top','wiggle-a','wiggle-b','wiggle-c','wiggle-d','shaft-bottom')
        self.relate('connect','arrowhead','shaft')
