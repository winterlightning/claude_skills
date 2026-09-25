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
    category = "sports"
    aliases = ()
    keywords = ('volleyball', 'court', 'net', 'sport')

    def build(self):
        self.add_polyline('left-post', (4, 8), (4, 16), (4, 28), (4, 40), closed=False)
        self.add_polyline('right-post', (44, 8), (44, 16), (44, 28), (44, 40), closed=False)
        self.add_polyline('top', (4, 16), (17, 16), (31, 16), (44, 16), closed=False)
        self.relate("connect", 'top', 'left-post')
        self.relate("connect", 'top', 'right-post')
        self.add_polyline('bottom', (4, 28), (17, 28), (31, 28), (44, 28), closed=False)
        self.relate("connect", 'bottom', 'left-post')
        self.relate("connect", 'bottom', 'right-post')
        self.add_line('mesh-17', (17, 16), (17, 28))
        self.relate("connect", 'mesh-17', 'top')
        self.relate("connect", 'mesh-17', 'bottom')
        self.add_line('mesh-31', (31, 16), (31, 28))
        self.relate("connect", 'mesh-31', 'top')
        self.relate("connect", 'mesh-31', 'bottom')
