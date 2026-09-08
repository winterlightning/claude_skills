"""Havana Cathedral Facade. Rebuilt from the supplied silhouette."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '189b26f6-a537-476e-9cd3-8f0672ed5fca'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-01/cathedral of havana cuba_189b26f6-a537-476e-9cd3-8f0672ed5fca.svg'
AUTHOR = 'gpt-6'


class Landmark(Solo48):
    icon_id = 'havana-cathedral'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "places/landmarks"
    aliases = ()
    keywords = ('cathedral', 'havana', 'cuba', 'church', 'facade', 'towers', 'landmark', 'religion', 'baroque')

    def build(self):
        self.add_polyline('outline', (2, 46), (2, 12), (7, 2), (12, 12), (12, 22), (19, 16), (19, 10), (24, 5), (29, 10), (29, 16), (36, 22), (36, 12), (41, 2), (46, 12), (46, 46), (28, 46), (20, 46), closed=True)
        self.add_line("door-left", (20, 46), (20, 36))
        self.add_arc("door-arch", (20, 36), (28, 36), radius_x=4)
        self.add_line("door-right", (28, 36), (28, 46))
        self.add_contour("door", "door-left", "door-arch", "door-right")
        self.relate("connect", "door", "outline")
        self.add_polyline('cross-v', (24, 20), (24, 23), (24, 25), closed=False)
        self.add_polyline('cross-h', (21, 23), (24, 23), (27, 23), closed=False)
        self.relate("connect", "cross-v", "cross-h")
