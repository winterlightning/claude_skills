"""A broad domed igloo with central arched entrance and summit pennant. Mirrored dome; flag deliberately extends right."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b7749894-8ff4-5c21-bb51-e79ba0249d19'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-06/igloo_b7749894-8ff4-5c21-bb51-e79ba0249d19.svg'
AUTHOR = 'gpt-6'


class IglooWithFlag(Solo48):
    icon_id = 'igloo-with-flag'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "places/landmarks"
    aliases = ()
    keywords = ('igloo', 'snow', 'arctic', 'shelter', 'dome', 'winter', 'flag', 'expedition')

    def build(self) -> None:
        # Centerline extremes (2,2)-(46,46).
        self.add_arc("dome-left", (2,46), (24,20), radius_x=22, radius_y=26)
        self.add_arc("dome-right", (24,20), (46,46), radius_x=22, radius_y=26)
        self.add_line("ground-right", (46,46), (31,46))
        self.add_line("door-right", (31,46), (31,39))
        self.add_arc("door", (31,39), (17,39), radius_x=7, sweep=False)
        self.add_line("door-left", (17,39), (17,46))
        self.add_line("ground-left", (17,46), (2,46))
        self.add_contour("shelter", "dome-left", "dome-right", "ground-right", "door-right", "door", "door-left", "ground-left", closed=True)
        self.add_polyline("pennant", (24,20), (24,16), (24,2), (42,9), (24,16))
        self.relate("connect", "pennant", "shelter")
