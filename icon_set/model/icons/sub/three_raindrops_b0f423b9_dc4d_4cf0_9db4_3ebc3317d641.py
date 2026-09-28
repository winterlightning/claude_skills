"""Three Raindrops: Three outlined drops form a triangular group, with one centred above two evenly spaced lower drops. Each has a pointed top, curved sides, and a rounded lower bowl.

Construction: Three equal teardrops in a triangular series, each with a pointed top and circular lower bowl.
Keyshape: SQUARE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'b0f423b9-dc4d-4cf0-9db4-3ebc3317d641'
SOURCE_PATH = 'pictographic-primitives/state/rain drops_b0f423b9-dc4d-4cf0-9db4-3ebc3317d641.svg'
AUTHOR = 'gpt-6'


class ThreeRaindrops(Sub32):
    icon_id = 'three-raindrops'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('raindrops', 'outlined', 'drops', 'form', 'triangular', 'group', 'centred', 'evenly')

    def build(self):
        for name,x,y in (("upper",16,2),("left",6,20),("right",26,20)):
            self.add_line(name+"-left",(x,y),(x-4,y+6))
            self.add_arc(name+"-bowl",(x-4,y+6),(x+4,y+6),radius_x=4,sweep=False)
            self.add_line(name+"-right",(x+4,y+6),(x,y))
            self.add_contour(name,name+"-left",name+"-bowl",name+"-right",closed=True)
