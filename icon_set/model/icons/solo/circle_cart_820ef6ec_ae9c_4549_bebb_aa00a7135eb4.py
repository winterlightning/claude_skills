"""A shopping cart basket and two wheels within a circle.
Construction: All defining parts retained; wheels remain dots as in reference.
Lucide construction reference: shopping-cart; coherent arcs and independent enclosed content.
Keyshape CIRCLE: radial ink radius 22, centre (24,24).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '820ef6ec-ae9c-4549-bebb-aa00a7135eb4'
SOURCE_PATH = 'icon_set/work/todo-references/circle cart_820ef6ec-ae9c-4549-bebb-aa00a7135eb4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'circle-cart'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases = ()
    keywords = ('circle', 'cart')

    def build(self):
        # Circle symbol owns its centre and radius; independent inner content.
        cx, cy, r = 24, 24, 20
        self.add_arc('ring-top', (cx-r,cy), (cx+r,cy), radius_x=r)
        self.add_arc('ring-bottom', (cx+r,cy), (cx-r,cy), radius_x=r)
        self.add_contour('ring', 'ring-top', 'ring-bottom', closed=True)
        # Basket quadrilateral with handle continuing the right slope; paired wheel dots.
        self.add_polyline('basket',(15,19),(31,19),(28,27),(18,27),closed=True)
        self.add_line('handle',(31,19),(32,16))
        self.relate('connect','basket','handle')
        for i,x in enumerate((20,28)):
            self.add_dot(f'wheel-{i}',(x,35))

