"""SQUARE (6,6)-(42,42) centerlines. Paired pointed towers and central gable flank an arched entrance. Omit the small interior cross and simplify the stepped gable for clear spacing. Mirrored about x=24.
Lucide church and castle inform clear roof/wall structure and simple arch construction.
Re-authored on the active SOLO48 contract from the supplied landmark render.
"""
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
        self.add_polyline('outline',(6,42),(6,16),(10,6),(14,16),(14,24),(24,14),(34,24),(34,16),(38,6),(42,16),(42,42),(28,42),(20,42),closed=True)
        self.add_line('door-left',(20,42),(20,35))
        self.add_arc('door-arch',(20,35),(28,35),radius_x=4)
        self.add_line('door-right',(28,35),(28,42))
        self.add_contour('door','door-left','door-arch','door-right')
        self.relate('connect','door','outline')
