"""circle kips. Standalone reconstruction of supplied reference.
Plan: preserve the whole composition; CIRCLE bounds (2, 2, 46, 46).
Construction reference: Lucide circle-arrow-down, round joins and coherent symbol contours.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'abcbb9db-f5c8-434b-b898-b6580cddb672'
SOURCE_PATH = 'icon_set/work/todo-references/circle kips_abcbb9db-f5c8-434b-b898-b6580cddb672.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'circle-kips'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('circle', 'kips')

    def build(self):

        # A circular enclosure owns the centre and radius; two tangent semicircles.
        cx = cy = 24
        radius = 20
        self.add_arc('ring-top', (cx-radius,cy), (cx+radius,cy), radius_x=radius)
        self.add_arc('ring-bottom', (cx+radius,cy), (cx-radius,cy), radius_x=radius)
        self.add_contour('ring', 'ring-top', 'ring-bottom', closed=True)

        # Kip sign: upright K, diagonal arms and a continuous crossing crossbar.
        self.add_polyline('stem',(20,14),(20,24),(20,34))
        self.add_polyline('arms',(30,14),(20,24),(30,34))
        self.add_polyline('bar',(14,24),(20,24),(32,24))
        self.relate('connect','stem','arms','bar')

