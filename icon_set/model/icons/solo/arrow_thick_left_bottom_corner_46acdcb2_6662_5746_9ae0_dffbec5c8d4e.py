'Directional arrow: equal-angle head with an explicit shared shaft endpoint and comfortable inset from its frame.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '46acdcb2-6662-5746-9ae0-dffbec5c8d4e'
SOURCE_PATH = 'icons-json/arrows/arrow thick left bottom corner_46acdcb2-6662-5746-9ae0-dffbec5c8d4e.json'
AUTHOR = 'gpt-6'

class ArrowThickLeftBottomCorner(Solo48):
    icon_id = 'arrow-thick-left-bottom-corner'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'thick', 'left', 'bottom', 'corner', 'arrows')

    def build(self) -> None:
        # A shared corner radius keeps all four turns tangent to their walls.
        left, top, right, bottom, radius = 6, 6, 42, 42, 4
        self.add_line('outline-top', (left+radius,top), (right-radius,top))
        self.add_arc('outline-tr', (right-radius,top), (right,top+radius), radius_x=radius)
        self.add_line('outline-right', (right,top+radius), (right,bottom-radius))
        self.add_arc('outline-br', (right,bottom-radius), (right-radius,bottom), radius_x=radius)
        self.add_line('outline-bottom', (right-radius,bottom), (left+radius,bottom))
        self.add_arc('outline-bl', (left+radius,bottom), (left,bottom-radius), radius_x=radius)
        self.add_line('outline-left', (left,bottom-radius), (left,top+radius))
        self.add_arc('outline-tl', (left,top+radius), (left+radius,top), radius_x=radius)
        self.add_contour('outline', *('outline-'+part for part in ('top','tr','right','br','bottom','bl','left','tl')), closed=True)

        self.add_polyline('head',(17,18),(17,31),(30,31))
        self.add_line('shaft',(17,31),(31,17))
        self.relate('connect','head','shaft')
