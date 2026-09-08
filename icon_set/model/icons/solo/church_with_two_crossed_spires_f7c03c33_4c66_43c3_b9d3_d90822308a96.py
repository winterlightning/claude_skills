"""Church with Two Crossed Spires. Rebuilt from the supplied silhouette."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f7c03c33-4c66-43c3-b9d3-d90822308a96'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-01/saint patrick cathedral dublin_f7c03c33-4c66-43c3-b9d3-d90822308a96.svg'
AUTHOR = 'gpt-6'


class Landmark(Solo48):
    icon_id = 'church-with-two-crossed-spires'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "places/landmarks"
    aliases = ()
    keywords = ('church', 'cathedral', 'spire', 'cross', 'towers', 'gothic', 'religion', 'worship')

    def build(self):
        self.add_polyline('outline', (2, 46), (2, 25), (12, 17), (22, 25), (22, 32), (34, 32), (34, 24), (40, 14), (46, 24), (46, 46), (16, 46), (8, 46), closed=True)
        self.add_polyline('cross-stem', (12, 5), (12, 9), (12, 17), closed=False)
        self.add_polyline('cross-bar', (8, 9), (12, 9), (16, 9), closed=False)
        self.relate("connect", "cross-stem", "cross-bar")
        self.relate("connect", "cross-stem", 'outline')
        self.add_polyline('left-block', (2, 25), (22, 25), (22, 46), closed=False)
        self.add_polyline('right-block', (34, 46), (34, 32), (34, 24), (46, 24), closed=False)
        self.relate("connect", "outline", "left-block")
        self.relate("connect", "outline", "right-block")
        self.add_polyline('window-left', (12, 33), (12, 38), closed=False)
        self.add_polyline('right-cross-stem', (40, 2), (40, 6), (40, 14), closed=False)
        self.add_polyline('right-cross-bar', (36, 6), (40, 6), (44, 6), closed=False)
        self.relate("connect", "right-cross-stem", "right-cross-bar")
        self.relate("connect", "right-cross-stem", 'outline')
        self.add_polyline('window-right', (40, 32), (40, 37), closed=False)
