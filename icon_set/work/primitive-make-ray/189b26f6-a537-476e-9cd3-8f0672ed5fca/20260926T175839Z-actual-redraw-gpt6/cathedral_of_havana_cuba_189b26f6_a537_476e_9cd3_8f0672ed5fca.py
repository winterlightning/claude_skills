"""SQUARE (6,6)-(42,42) centerlines. Paired pointed towers and central gable flank an arched entrance. Add a compact cross at the central roof peak and simplify the stepped gable for clear spacing. Mirrored about x=24.
Lucide church and castle inform clear roof/wall structure and simple arch construction.
Re-authored on the active SOLO48 contract from the supplied landmark render.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '189b26f6-a537-476e-9cd3-8f0672ed5fca'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__havana-cathedral/20260926T172218Z-thuan-mac-1/reference/cathedral of havana cuba_189b26f6-a537-476e-9cd3-8f0672ed5fca.svg'
AUTHOR = 'gpt-6'


class Landmark(Solo48):
    icon_id = 'havana-cathedral'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "landmarks"
    categories = ("landmarks", "primitives")
    aliases = ()
    keywords = ('cathedral', 'havana', 'cuba', 'church', 'facade', 'towers', 'landmark', 'religion', 'baroque')

    def build(self):
        self.add_polyline('outline',(6,42),(6,16),(10,6),(14,16),(14,24),(24,12),(34,24),(34,16),(38,6),(42,16),(42,42),(28,42),(20,42),closed=True)
        self.add_line('door-left',(20,42),(20,35))
        self.add_arc('door-arch',(20,35),(28,35),radius_x=4)
        self.add_line('door-right',(28,35),(28,42))
        self.add_contour('door','door-left','door-arch','door-right')
        self.relate('connect','door','outline')
        self.add_line('cross-stem',(24,6),(24,12))
        self.add_line('cross-bar',(21,8),(27,8))
        self.relate('connect','cross-stem','cross-bar')
        self.relate('connect','cross-stem','outline')

