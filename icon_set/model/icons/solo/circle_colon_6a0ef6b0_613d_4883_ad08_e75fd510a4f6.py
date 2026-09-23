"""circle colon. Standalone reconstruction of supplied reference.
Plan: preserve the whole composition; CIRCLE bounds (2, 2, 46, 46).
Construction reference: Lucide circle-arrow-down, round joins and coherent symbol contours.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6a0ef6b0-613d-4883-ad08-e75fd510a4f6'
SOURCE_PATH = 'icon_set/work/todo-references/circle colon_6a0ef6b0-613d-4883-ad08-e75fd510a4f6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'circle-colon'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('circle', 'colon')

    def build(self):

        # A circular enclosure owns the centre and radius; two tangent semicircles.
        cx = cy = 24
        radius = 20
        self.add_arc('ring-top', (cx-radius,cy), (cx+radius,cy), radius_x=radius)
        self.add_arc('ring-bottom', (cx+radius,cy), (cx-radius,cy), radius_x=radius)
        self.add_contour('ring', 'ring-top', 'ring-bottom', closed=True)

        # Open C and diagonal slash form the currency symbol; intersections are
        # explicit shared endpoints rather than a clearance waiver.
        self.add_arc('c-upper',(29,16),(19,16),radius_x=5,radius_y=3,sweep=False)
        self.add_arc('c-left',(19,16),(19,32),radius_x=4,radius_y=8,sweep=False)
        self.add_arc('c-lower',(19,32),(29,32),radius_x=5,radius_y=3,sweep=False)
        self.add_contour('currency-c','c-upper','c-left','c-lower')
        self.add_line('slash',(29,16),(19,32))
        self.relate('connect','currency-c','slash')
