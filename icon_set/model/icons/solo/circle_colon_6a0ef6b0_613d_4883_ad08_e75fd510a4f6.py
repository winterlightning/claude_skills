"""A slashed C currency symbol within a circle.
Construction: No useful local match for the currency glyph; circle-play informs only enclosure.
Lucide construction reference: circle-play; coherent arcs and independent enclosed content.
Keyshape CIRCLE: radial ink radius 22, centre (24,24).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6a0ef6b0-613d-4883-ad08-e75fd510a4f6'
SOURCE_PATH = 'icon_set/work/todo-references/circle colon_6a0ef6b0-613d-4883-ad08-e75fd510a4f6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'circle-colon'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('combination', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('circle', 'colon')

    def build(self):
        # Circle symbol owns its centre and radius; independent inner content.
        cx, cy, r = 24, 24, 20
        self.add_arc('ring-top', (cx-r,cy), (cx+r,cy), radius_x=r)
        self.add_arc('ring-bottom', (cx+r,cy), (cx-r,cy), radius_x=r)
        self.add_contour('ring', 'ring-top', 'ring-bottom', closed=True)
        # Open C currency mark and rising slash crossing at its endpoints.
        self.add_arc('c-upper',(29,14),(15,24),radius_x=10,radius_y=10,sweep=False)
        self.add_arc('c-lower',(15,24),(29,34),radius_x=10,radius_y=10,sweep=False)
        self.add_contour('currency-c','c-upper','c-lower')
        self.add_line('slash',(18,33),(29,14))
        self.relate('connect','currency-c','slash')

