"""House with Interior Door Stroke; standalone reconstruction of the supplied reference.
Construction: Lucide house informed coherent contours and structural joins.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '40ae9091-ac10-4c02-88bc-c04028f85e36'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/house_40ae9091-ac10-4c02-88bc-c04028f85e36.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'house-with-interior-door-stroke-40ae9091-ac10-4c02-88bc-c04028f85e36'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/interface-essential"
    aliases = ()
    keywords = ('house', 'home', 'roof', 'building', 'facade', 'door')

    def build(self):
        # Plan: mirrored house about x=24; SQUARE extremes (6,6)-(42,42).
        # Door and wall dimensions belong to the facade; roof shares exact wall nodes.
        axis=24
        left,right=10,38
        base=42
        self.add_polyline("roof", (6,24),(left,20),(axis,6),(right,20),(42,24))
        self.add_polyline("walls",(left,20),(left,base),(axis,base),(right,base),(right,20))
        self.relate("connect","roof","walls")
        self.add_line("interior-stroke",(axis,25),(axis,33))
