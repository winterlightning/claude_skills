"""A Lao kip currency mark within a circle.
Construction: No useful local match for the currency glyph; circle-play informs only enclosure.
Lucide construction reference: circle-play; coherent arcs and independent enclosed content.
Keyshape CIRCLE: radial ink radius 22, centre (24,24).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'abcbb9db-f5c8-434b-b898-b6580cddb672'
SOURCE_PATH = 'icon_set/work/todo-references/circle kips_abcbb9db-f5c8-434b-b898-b6580cddb672.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'circle-kips'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases = ()
    keywords = ('circle', 'kips')

    def build(self):
        # Circle symbol owns its centre and radius; independent inner content.
        cx, cy, r = 24, 24, 20
        self.add_arc('ring-top', (cx-r,cy), (cx+r,cy), radius_x=r)
        self.add_arc('ring-bottom', (cx+r,cy), (cx-r,cy), radius_x=r)
        self.add_contour('ring', 'ring-top', 'ring-bottom', closed=True)
        # Kip currency letter with central junction and a horizontal crossing bar.
        self.add_line('stem-upper',(19,14),(19,24))
        self.add_line('stem-lower',(19,24),(19,34))
        self.add_line('arm-upper',(19,24),(30,15))
        self.add_line('arm-lower',(19,24),(30,33))
        self.add_line('bar-left',(14,24),(19,24))
        self.add_line('bar-right',(19,24),(33,24))
        members=['stem-upper','stem-lower','arm-upper','arm-lower','bar-left','bar-right']
        for i,a in enumerate(members):
            for b in members[i+1:]: self.relate('connect',a,b)

