"""SQUARE (6,6)-(42,42) centerlines. Preserve cross-topped left gable, high connector, tall right spire and structural divisions. Keep facade blank as requested. Deliberate asymmetric skyline follows the reference.
Lucide church and castle inform clear roof/wall structure and simple arch construction.
Re-authored on the active SOLO48 contract from the supplied landmark render.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3ed24171-9732-4eaa-baa4-907916e32878'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-01/saint patrick cathedral dublin_3ed24171-9732-4eaa-baa4-907916e32878.svg'
AUTHOR = 'gpt-6'


class Landmark(Solo48):
    icon_id = 'gothic-church-with-side-spire'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "places/landmarks"
    aliases = ()
    keywords = ('church', 'cathedral', 'spire', 'gothic', 'cross', 'tower', 'religion', 'worship')

    def build(self):
        self.add_polyline('outline',(6,42),(6,26),(15,18),(24,26),(24,30),(32,30),(32,22),(37,6),(42,22),(42,42),(32,42),(24,42),closed=True)
        self.add_polyline('cross-stem',(15,6),(15,10),(15,18))
        self.add_polyline('cross-bar',(11,10),(15,10),(19,10))
        self.relate('connect','cross-stem','cross-bar')
        self.relate('connect','cross-stem','outline')
        self.add_polyline('nave-divider',(6,26),(24,26),(24,30),(24,42))
        self.add_polyline('tower-divider',(32,42),(32,30),(32,22),(42,22))
        self.relate('connect','nave-divider','outline')
        self.relate('connect','tower-divider','outline')
