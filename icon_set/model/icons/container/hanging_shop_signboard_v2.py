"""Tall hanging real-estate panel for a two-line SOLD label. SQUARE ink bounds (4,4)-(60,60). Shared panel radius and identical hangers; deliberate right support. Lucide signpost original and atomic-debug informed the attached support. Parent preserved."""

from ...keyshapes import Keyshape
from ._base import Container64
SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = 'gpt-6'

class HangingShopSignboardVariant2(Container64):
    icon_id = 'hanging-shop-signboard-v2'
    variant_of = 'hanging-shop-signboard'
    variant_label = 'Taller panel for wrapped shop text'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ()

    def build(self) -> None:
        # Tall panel with two identical hangers. The post remains on the right.
        # SQUARE ink (4,4)-(60,60); shared corner radius and attachment coordinates.
        left, right, top, bottom, radius = 6, 50, 14, 58, 4
        points = [(left+radius,top),(right-radius,top),(right,top+radius),
                  (right,bottom-radius),(right-radius,bottom),(left+radius,bottom),
                  (left,bottom-radius),(left,top+radius)]
        for i in range(8):
            a,b=points[i],points[(i+1)%8]
            if i%2: self.add_arc(f'panel-{i}',a,b,radius_x=radius)
            else: self.add_line(f'panel-{i}',a,b)
        self.add_contour('panel',*[f'panel-{i}' for i in range(8)],closed=True)
        self.add_line('arm',(12,6),(54,6))
        self.add_arc('turn',(54,6),(58,10),radius_x=4)
        self.add_line('post',(58,10),(58,58))
        self.add_contour('support','arm','turn','post')
        for x in (16,40):
            self.add_line(f'hanger-{x}',(x,6),(x,top))
            self.relate('connect','support',f'hanger-{x}')
            self.relate('connect','panel',f'hanger-{x}')
