"""circle cart. Standalone reconstruction of supplied reference.
Plan: preserve the whole composition; CIRCLE bounds (2, 2, 46, 46).
Construction reference: Lucide shopping-cart, round joins and coherent symbol contours.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '820ef6ec-ae9c-4549-bebb-aa00a7135eb4'
SOURCE_PATH = 'icon_set/work/todo-references/circle cart_820ef6ec-ae9c-4549-bebb-aa00a7135eb4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'circle-cart'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('circle', 'cart')

    def build(self):

        # A circular enclosure owns the centre and radius; two tangent semicircles.
        cx = cy = 24
        radius = 20
        self.add_arc('ring-top', (cx-radius,cy), (cx+radius,cy), radius_x=radius)
        self.add_arc('ring-bottom', (cx+radius,cy), (cx-radius,cy), radius_x=radius)
        self.add_contour('ring', 'ring-top', 'ring-bottom', closed=True)

        # Sloping open trolley basket, raised right handle and two wheel dots.
        self.add_polyline('basket',(14,18),(30,18),(28,26),(18,26),closed=True)
        self.add_line('handle',(30,18),(32,16))
        self.relate('connect','basket','handle')
        for i,x in enumerate((19,28)):
            self.add_dot(f'wheel-{i}',(x,34))

