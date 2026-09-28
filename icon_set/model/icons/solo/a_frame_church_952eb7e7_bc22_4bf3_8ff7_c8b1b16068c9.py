"""HRECT_XL (6,8)-(42,40) centerlines. Preserve cross, projecting roof eaves and single entrance mark. Shared roof/wall attachment nodes lie on the same straight roof runs. Mirrored about x=24.
Lucide church and castle inform clear roof/wall structure and simple arch construction.
Re-authored on the active SOLO48 contract from the supplied landmark render.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '952eb7e7-bc22-4bf3-8ff7-c8b1b16068c9'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-01/church_952eb7e7-bc22-4bf3-8ff7-c8b1b16068c9.svg'
AUTHOR = 'gpt-6'


class Landmark(Solo48):
    icon_id = 'a-frame-church'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "landmarks"
    categories = ("landmarks", "primitives")
    aliases = ()
    keywords = ('church', 'chapel', 'cross', 'religion', 'worship', 'a-frame', 'roof', 'christian')

    def build(self):
        self.add_polyline('roof',(4,30),(9,27),(24,18),(39,27),(44,30))
        self.add_polyline('walls',(9,27),(9,40),(24,40),(39,40),(39,27))
        self.relate('connect','roof','walls')
        self.add_polyline('cross-stem',(24,8),(24,11),(24,18))
        self.add_polyline('cross-bar',(20,11),(24,11),(28,11))
        self.relate('connect','cross-stem','cross-bar')
        self.relate('connect','cross-stem','roof')
        self.add_line('entrance',(24,40),(24,32))
        self.relate('connect','entrance','walls')
