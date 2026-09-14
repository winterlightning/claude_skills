'Circuit lock: round shackle, clear central keyhole and two distinct outgoing arrows, preserving the branching security symbol.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aad274a9-6341-4a33-9772-7b8d5f95c1bd'
SOURCE_PATH = 'icons-json/products/circuit lock_aad274a9-6341-4a33-9772-7b8d5f95c1bd.json'
AUTHOR = 'gpt-6'

class CircuitLock(Solo48):
    icon_id = 'circuit-lock'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'products'
    aliases = ()
    keywords = ('circuit', 'lock', 'products')

    def build(self) -> None:
        # A shared corner radius keeps all four turns tangent to their walls.
        left, top, right, bottom, radius = 4, 19, 24, 37, 3
        self.add_line('lock-top', (left+radius,top), (right-radius,top))
        self.add_arc('lock-tr', (right-radius,top), (right,top+radius), radius_x=radius)
        self.add_line('lock-right', (right,top+radius), (right,bottom-radius))
        self.add_arc('lock-br', (right,bottom-radius), (right-radius,bottom), radius_x=radius)
        self.add_line('lock-bottom', (right-radius,bottom), (left+radius,bottom))
        self.add_arc('lock-bl', (left+radius,bottom), (left,bottom-radius), radius_x=radius)
        self.add_line('lock-left', (left,bottom-radius), (left,top+radius))
        self.add_arc('lock-tl', (left,top+radius), (left+radius,top), radius_x=radius)
        self.add_contour('lock', *('lock-'+part for part in ('top','tr','right','br','bottom','bl','left','tl')), closed=True)

        self.add_line('shackle-left',(8,19),(8,14))
        self.add_arc('shackle-top',(8,14),(20,14),radius_x=6)
        self.add_line('shackle-right',(20,14),(20,19))
        self.add_contour('shackle','shackle-left','shackle-top','shackle-right')
        self.relate('connect','shackle','lock')
        self.add_dot('keyhole',(14,28))
        self.add_polyline('upper',(33,18),(44,8))
        self.add_polyline('upper-head',(38,8),(44,8),(44,14))
        self.relate('connect','upper','upper-head')
        self.add_polyline('lower',(33,30),(44,40))
        self.add_polyline('lower-head',(38,40),(44,40),(44,34))
        self.relate('connect','lower','lower-head')
