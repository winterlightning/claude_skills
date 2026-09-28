"""Bunch of Bananas."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '01dfab52-1214-532b-8f84-ea5dce7a2998'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__banana-bunch/20260927T150749Z-thuan-mac-1/reference/banana_01dfab52-1214-532b-8f84-ea5dce7a2998.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'banana-bunch'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('banana', 'fruit', 'bunch', 'tropical', 'produce', 'food', 'stem')

    def build(self):
        # Three outward tips share a stem; the far-left crescent stays open.
        self.add_polyline('stem',(30,10),(30,4),(38,4),(38,10))
        self.add_bezier('outer',(38,10),((40,12),(40,18),(40,22)),((40,36),(27,44),(18,44)),((12,44),(8,42),(8,40)))
        self.add_line('tip',(8,40),(14,34))
        self.add_bezier('inner',(14,34),((10,34),(8,31),(8,28)),((20,29),(30,23),(30,10)))
        self.add_bezier('back-fruit',(30,10),((24,20),(19,24),(10,24)))
        for a,b in (('stem','outer'),('outer','tip'),('tip','inner'),('inner','stem'),('back-fruit','stem')):
            self.relate('connect',a,b)
