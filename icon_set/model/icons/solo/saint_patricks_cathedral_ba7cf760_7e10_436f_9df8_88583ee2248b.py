"""SQUARE (6,6)-(42,42) centerlines. Preserve cross-topped left entrance, pointed doorway, low connector and taller right spire. Omit tower window and small facade divisions. Deliberate asymmetric skyline follows the reference.
Lucide church and castle inform clear roof/wall structure and simple arch construction.
Re-authored on the active SOLO48 contract from the supplied landmark render.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ba7cf760-7e10-436f-9df8-88583ee2248b'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-01/saint patrick cathedral dublin 1_ba7cf760-7e10-436f-9df8-88583ee2248b.svg'
AUTHOR = 'gpt-6'


class Landmark(Solo48):
    icon_id = 'saint-patricks-cathedral'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "places/landmarks"
    aliases = ()
    keywords = ('saint patrick', 'dublin', 'cathedral', 'church', 'spire', 'gothic', 'landmark', 'religion')

    def build(self):
        self.add_polyline('outline',(6,42),(6,26),(16,18),(26,26),(26,33),(34,33),(34,22),(38,6),(42,22),(42,42),(34,42),(26,42),(20,42),(12,42),closed=True)
        self.add_polyline('cross-stem',(16,6),(16,10),(16,18))
        self.add_polyline('cross-bar',(12,10),(16,10),(20,10))
        self.relate('connect','cross-stem','cross-bar')
        self.relate('connect','cross-stem','outline')
        self.add_polyline('door',(12,42),(12,36),(16,32),(20,36),(20,42))
        self.relate('connect','door','outline')
