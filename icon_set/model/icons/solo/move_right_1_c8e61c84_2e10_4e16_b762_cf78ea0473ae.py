'Move right: rounded upright box and connected arrow separated by 5 units of ink.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c8e61c84-2e10-4e16-b762-cf78ea0473ae'
SOURCE_PATH = 'pictographic-primitives/interface-essential/move right 1_c8e61c84-2e10-4e16-b762-cf78ea0473ae.svg'
AUTHOR = 'gpt-6'

class MoveRight1(Solo48):
    icon_id = 'move-right-1'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('move', 'right', 'interface-essential')

    def build(self) -> None:
        # A shared corner radius keeps all four turns tangent to their walls.
        left, top, right, bottom, radius = 4, 8, 17, 40, 3
        self.add_line('box-top', (left+radius,top), (right-radius,top))
        self.add_arc('box-tr', (right-radius,top), (right,top+radius), radius_x=radius)
        self.add_line('box-right', (right,top+radius), (right,bottom-radius))
        self.add_arc('box-br', (right,bottom-radius), (right-radius,bottom), radius_x=radius)
        self.add_line('box-bottom', (right-radius,bottom), (left+radius,bottom))
        self.add_arc('box-bl', (left+radius,bottom), (left,bottom-radius), radius_x=radius)
        self.add_line('box-left', (left,bottom-radius), (left,top+radius))
        self.add_arc('box-tl', (left,top+radius), (left+radius,top), radius_x=radius)
        self.add_contour('box', *('box-'+part for part in ('top','tr','right','br','bottom','bl','left','tl')), closed=True)

        self.add_line('shaft',(26,24),(44,24))
        self.add_polyline('head',(37,17),(44,24),(37,31))
        self.relate('connect','head','shaft')
