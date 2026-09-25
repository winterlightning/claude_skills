'Rooster head: smooth crown and comb with a clear eye and beak; the comb meets the head at actual shared endpoints.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '221f89e4-4362-5f43-aa0a-e270a4269e65'
SOURCE_PATH = 'pictographic-primitives/animals/rooster_221f89e4-4362-5f43-aa0a-e270a4269e65.svg'
AUTHOR = 'gpt-6'


class RoosterHead(Solo48):
    icon_id = 'rooster-head'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('rooster', 'cockerel', 'head', 'comb', 'wattle', 'beak', 'farm', 'poultry')

    def build(self) -> None:
        self.add_line('left',(6,42),(6,31))
        self.add_bezier('crown',(6,31),((6,21),(12,15),(19,15)),((26,15),(30,18),(33,22)))
        self.add_polyline('beak',(33,22),(42,35),(36,35))
        self.add_bezier('wattle',(36,35),((36,38),(35,41),(32,42)))
        self.add_contour('head','left','crown')
        self.relate('connect','head','beak')
        self.relate('connect','beak','wattle')
        self.add_bezier('comb',(19,15),((15,15),(11,6),(16,6)),((20,6),(22,6),(24,10)),((26,7),(28,6),(31,6)),((38,6),(38,15),(33,22)))
        self.relate('connect','head','comb')
        self.relate('connect','beak','comb')
        self.add_dot('eye',(25,27))
