"""House with Central Interior Stroke; standalone reconstruction of the supplied reference.
Construction: Lucide house informed coherent contours and structural joins.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2faa75f6-6a10-40dd-b1b2-1d2767155368'
SOURCE_PATH = 'pictographic-primitives/interface-essential/house_2faa75f6-6a10-40dd-b1b2-1d2767155368.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'house-with-central-interior-stroke'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    categories = ("interface-essential", "primitives")
    tags = ('sub icon',)
    aliases = ()
    keywords = ('house', 'home', 'roof', 'building', 'facade', 'outline')

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
