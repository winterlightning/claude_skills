"""House with Rectangular Front Door; standalone reconstruction of the supplied reference.
Construction: Lucide house informed coherent contours and structural joins.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6f726eee-0b48-4d02-a8a9-94fafa29d0f0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/house_6f726eee-0b48-4d02-a8a9-94fafa29d0f0.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'house-with-rectangular-front-door'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/interface-essential"
    aliases = ()
    keywords = ('house', 'home', 'roof', 'door', 'building', 'entrance')

    def build(self):
        # Plan: mirrored house about x=24; SQUARE extremes (6,6)-(42,42).
        # Door and wall dimensions belong to the facade; roof shares exact wall nodes.
        axis=24
        left,right=10,38
        base=42
        self.add_polyline("roof", (6,24),(left,20),(axis,6),(right,20),(42,24))
        door_left,door_right=axis-5,axis+5
        self.add_line("left-upright",(left,20),(left,base-2))
        self.add_arc("left-corner",(left,base-2),(left+2,base),radius_x=2,sweep=False)
        self.add_line("left-foot",(left+2,base),(door_left,base))
        self.add_contour("wall-left","left-upright","left-corner","left-foot")
        self.add_line("right-foot",(door_right,base),(right-2,base))
        self.add_arc("right-corner",(right-2,base),(right,base-2),radius_x=2,sweep=False)
        self.add_line("right-upright",(right,base-2),(right,20))
        self.add_contour("wall-right","right-foot","right-corner","right-upright")
        self.add_polyline("door",(door_left,base),(door_left,27),(door_right,27),(door_right,base))
        for side in ("left","right"):
            self.relate("connect","wall-"+side,"roof")
            self.relate("connect","wall-"+side,"door")
        self.add_line("threshold",(door_left,base),(door_right,base))
        for part in ("wall-left","wall-right","door"):
            self.relate("connect","threshold",part)
