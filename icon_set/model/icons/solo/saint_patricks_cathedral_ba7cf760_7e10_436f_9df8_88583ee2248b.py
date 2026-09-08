"""Saint Patrick's Cathedral. Rebuilt from the supplied silhouette."""
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
        self.add_polyline('outline', (2, 46), (2, 25), (12, 17), (22, 25), (22, 32), (34, 32), (34, 24), (40, 2), (46, 24), (46, 46), (16, 46), (8, 46), closed=True)
        self.add_polyline('cross-stem', (12, 5), (12, 9), (12, 17), closed=False)
        self.add_polyline('cross-bar', (8, 9), (12, 9), (16, 9), closed=False)
        self.relate("connect", "cross-stem", "cross-bar")
        self.relate("connect", "cross-stem", 'outline')
        self.add_polyline('left-block', (2, 25), (22, 25), (22, 46), closed=False)
        self.add_polyline('right-block', (34, 46), (34, 32), (34, 24), (46, 24), closed=False)
        self.relate("connect", "outline", "left-block")
        self.relate("connect", "outline", "right-block")
        self.add_polyline('door', (8, 46), (8, 37), (12, 33), (16, 37), (16, 46), closed=False)
        self.relate("connect", "door", "outline")
        self.add_polyline('window-right', (40, 32), (40, 37), closed=False)
