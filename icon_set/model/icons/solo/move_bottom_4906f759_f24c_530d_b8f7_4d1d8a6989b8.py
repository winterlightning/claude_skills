'Move down: tangent rounded box above a centred arrow with a clear 5-unit ink gap.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4906f759-f24c-530d-b8f7-4d1d8a6989b8'
SOURCE_PATH = 'pictographic-primitives/arrows/move bottom_4906f759-f24c-530d-b8f7-4d1d8a6989b8.svg'
AUTHOR = 'gpt-6'

class MoveBottom(Solo48):
    icon_id = 'move-bottom'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    categories = ('arrows', 'primitives')
    aliases = ()
    keywords = ('move', 'bottom', 'arrows')

    def build(self) -> None:
        # A shared corner radius keeps all four turns tangent to their walls.
        left, top, right, bottom, radius = 8, 4, 40, 16, 3
        self.add_line('box-top', (left+radius,top), (right-radius,top))
        self.add_arc('box-tr', (right-radius,top), (right,top+radius), radius_x=radius)
        self.add_line('box-right', (right,top+radius), (right,bottom-radius))
        self.add_arc('box-br', (right,bottom-radius), (right-radius,bottom), radius_x=radius)
        self.add_line('box-bottom', (right-radius,bottom), (left+radius,bottom))
        self.add_arc('box-bl', (left+radius,bottom), (left,bottom-radius), radius_x=radius)
        self.add_line('box-left', (left,bottom-radius), (left,top+radius))
        self.add_arc('box-tl', (left,top+radius), (left+radius,top), radius_x=radius)
        self.add_contour('box', *('box-'+part for part in ('top','tr','right','br','bottom','bl','left','tl')), closed=True)

        self.add_line('shaft',(24,25),(24,44))
        self.add_polyline('head',(16,36),(24,44),(32,36))
        self.relate('connect','head','shaft')
