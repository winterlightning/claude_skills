"""Musical Note: A single musical note has an oval lower-left head, a tall upright stem, and a curved flag extending down to the right. Generate this component alone; exclude Circle Frame.

Construction: A round note head attaches to a tall stem, with one open curved flag.
Keyshape: VRECT_L; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'eed5ac0e-32e6-4c3f-ae1c-f56578ca5fdb'
SOURCE_PATH = 'pictographic-primitives/state/circle music_eed5ac0e-32e6-4c3f-ae1c-f56578ca5fdb.svg'
AUTHOR = 'gpt-6'


class MusicalNote(Sub32):
    icon_id = 'musical-note'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('musical', 'note', 'single', 'oval', 'lower', 'left', 'head', 'tall')

    def build(self):
        def circle(name,cx,cy,radius):
            self.add_arc(name+"-top",(cx-radius,cy),(cx+radius,cy),radius_x=radius)
            self.add_arc(name+"-bottom",(cx+radius,cy),(cx-radius,cy),radius_x=radius)
            self.add_contour(name,name+"-top",name+"-bottom",closed=True)
        circle('note',12,24,6)
        self.add_line('stem',(18,24),(18,2))
        self.add_arc('flag',(18,2),(26,14),radius_x=8,radius_y=12)
        self.relate('connect','note','stem')
        self.relate('connect','stem','flag')
