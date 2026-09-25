"""House with Open Rectangular Entrance; standalone reconstruction of the supplied reference.
Construction: Lucide house informed coherent contours and structural joins.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '359d205e-3e65-4681-9176-4cc7661ec8be'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/house_359d205e-3e65-4681-9176-4cc7661ec8be.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'house-with-open-rectangular-entrance'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
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
        self.add_polyline("wall-left", (left,20),(left,base),(door_left,base))
        self.add_polyline("wall-right", (door_right,base),(right,base),(right,20))
        self.add_polyline("door",(door_left,base),(door_left,27),(door_right,27),(door_right,base))
        for side in ("left","right"):
            self.relate("connect","wall-"+side,"roof")
            self.relate("connect","wall-"+side,"door")
