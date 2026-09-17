"""House with Chimney; standalone reconstruction of the supplied reference.
Construction: Lucide house informed coherent contours and structural joins.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '48ea3c6c-5c29-50ff-bdb7-99895f95d856'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/house chimney_48ea3c6c-5c29-50ff-bdb7-99895f95d856.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'house-with-chimney-reference'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/interface-essential"
    aliases = ()
    keywords = ('house', 'home', 'chimney', 'roof', 'door', 'building')

    def build(self):
        # Plan: mirrored house about x=24; SQUARE extremes (6,6)-(42,42).
        # Door and wall dimensions belong to the facade; roof shares exact wall nodes.
        axis=24
        left,right=10,38
        base=42
        # Keep the original detached angular chimney; close tiny eave breaks.
        self.add_polyline("roof",(6,32),(10,28),(24,14),(38,28),(42,32))
        self.add_polyline("chimney",(34,6),(42,6),(42,14))
        door_left,door_right=axis-5,axis+5
        self.add_line("left-upright",(left,28),(left,base-2))
        self.add_arc("left-corner",(left,base-2),(left+2,base),radius_x=2,sweep=False)
        self.add_line("left-foot",(left+2,base),(door_left,base))
        self.add_contour("wall-left","left-upright","left-corner","left-foot")
        self.add_line("right-foot",(door_right,base),(right-2,base))
        self.add_arc("right-corner",(right-2,base),(right,base-2),radius_x=2,sweep=False)
        self.add_line("right-upright",(right,base-2),(right,28))
        self.add_contour("wall-right","right-foot","right-corner","right-upright")
        self.add_line("door-left", (door_left,base),(door_left,33))
        self.add_arc("door-arch", (door_left,33),(door_right,33),radius_x=5)
        self.add_line("door-right", (door_right,33),(door_right,base))
        self.add_contour("door", "door-left","door-arch","door-right")
        for side in ("left","right"):
            self.relate("connect","wall-"+side,"roof")
            self.relate("connect","wall-"+side,"door")
