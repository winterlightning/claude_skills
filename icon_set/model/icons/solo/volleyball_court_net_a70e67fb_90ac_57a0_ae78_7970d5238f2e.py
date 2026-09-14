'A volleyball net suspended between tall posts.\nConstruction: Horizontal centerlines (6,8)-(42,40). Equal three-bay mesh; remove the second mesh row and foot caps.\nLucide: No useful exact match; repeated straight mesh bays and shared attachment nodes.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a70e67fb-90ac-57a0-ae78-7970d5238f2e'
SOURCE_PATH = 'pictographic-primitives/sports/volleyball net_a70e67fb-90ac-57a0-ae78-7970d5238f2e.svg'
AUTHOR = 'gpt-6'

class VolleyballCourtNet(Solo48):
    icon_id = 'volleyball-court-net'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/sports"
    aliases = ()
    keywords = ('volleyball', 'court', 'net', 'sport')

    def build(self):
        self.add_polyline('left-post', (6, 8), (6, 16), (6, 28), (6, 40), closed=False)
        self.add_polyline('right-post', (42, 8), (42, 16), (42, 28), (42, 40), closed=False)
        self.add_polyline('top', (6, 16), (17, 16), (31, 16), (42, 16), closed=False)
        self.relate("connect", 'top', 'left-post')
        self.relate("connect", 'top', 'right-post')
        self.add_polyline('bottom', (6, 28), (17, 28), (31, 28), (42, 28), closed=False)
        self.relate("connect", 'bottom', 'left-post')
        self.relate("connect", 'bottom', 'right-post')
        self.add_line('mesh-17', (17, 16), (17, 28))
        self.relate("connect", 'mesh-17', 'top')
        self.relate("connect", 'mesh-17', 'bottom')
        self.add_line('mesh-31', (31, 16), (31, 28))
        self.relate("connect", 'mesh-31', 'top')
        self.relate("connect", 'mesh-31', 'bottom')
